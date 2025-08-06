import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from openpyxl.utils.dataframe import dataframe_to_rows
from tkinter import messagebox
from plotting import Plotter

class ExcelExporter:
    @staticmethod
    def export(selected_names, T0_data, Tn_data, output_file):
        try:
            os.makedirs("plots", exist_ok=True)
            wb = Workbook()
            wb.remove(wb.active)

            for idx, test_name in enumerate(selected_names, start=1):
                sheet_name = f"Sheet{idx}"
                ws = wb.create_sheet(title=sheet_name)

                r1 = T0_data['PTR'].loc[T0_data['PTR']['TEST_TXT'] == test_name, 'RESULT'].dropna()
                r2 = Tn_data['PTR'].loc[Tn_data['PTR']['TEST_TXT'] == test_name, 'RESULT'].dropna()

                if r1.empty or r2.empty:
                    ws.append([f"No data available for test '{test_name}'"])
                    continue

                stats_data = {
                    "Statistic": ["Mean", "Median", "Std Dev", "Min", "Max"],
                    "T0": [r1.mean(), r1.median(), r1.std(), r1.min(), r1.max()],
                    "Tn": [r2.mean(), r2.median(), r2.std(), r2.min(), r2.max()]
                }
                stats_df = pd.DataFrame(stats_data)
                stats_df["Δ"] = stats_df["Tn"] - stats_df["T0"]
                stats_df["% Change"] = stats_df.apply(
                    lambda row: (row["Δ"] / row["T0"] * 100) if row["T0"] != 0 else None, axis=1
                )

                for r in dataframe_to_rows(stats_df, index=False, header=True):
                    ws.append(r)

                kde_path = f"plots/{sheet_name}_kde.png"
                cum_path = f"plots/{sheet_name}_cumulative.png"

                Plotter.plot_kde(r1, 'T0', r2, 'Tn', test_name, kde_path)
                Plotter.plot_cumulative(r1, 'T0', r2, 'Tn', test_name, cum_path)

                img_kde = XLImage(kde_path)
                img_cum = XLImage(cum_path)

                img_kde.anchor = 'A10'
                img_cum.anchor = 'O10'

                ws.add_image(img_kde)
                ws.add_image(img_cum)

            wb.save(output_file)
            messagebox.showinfo("Success", f"Excel report saved to: {output_file}")

        except Exception as e:
            messagebox.showerror("Export Error", str(e))
