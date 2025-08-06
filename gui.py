import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from data_processing import STDFProcessor
from excel_export import ExcelExporter

T0_data = None
Tn_data = None
selected_test_names = []

def load_tests():
    global selected_test_names, T0_data, Tn_data
    pathsT0 = entry_file1.get().split(';')
    pathsTn = entry_file2.get().split(';')
    final_T0 = combo_final_T0.get()
    final_Tn = combo_final_Tn.get()

    if not pathsT0 or not pathsTn or not final_T0 or not final_Tn:
        messagebox.showerror("Error", "Please select both STDF file groups and final re-test files.")
        return

    try:
        T0_data = STDFProcessor.consolidate_retests(pathsT0, final_T0)
        Tn_data = STDFProcessor.consolidate_retests(pathsTn, final_Tn)

        T0_ptr = STDFProcessor.tests(T0_data)
        Tn_ptr = STDFProcessor.tests(Tn_data)
        common_names = STDFProcessor.shared_tests(T0_ptr, Tn_ptr)

        listbox.delete(0, tk.END)
        for name in common_names:
            listbox.insert(tk.END, name)

        selected_test_names = common_names

    except Exception as e:
        messagebox.showerror("Error", str(e))

def export_to_excel():
    global T0_data, Tn_data
    if T0_data is None or Tn_data is None:
        messagebox.showerror("Error", "Please load both STDF file groups first.")
        return

    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("No Selection", "Please select one or more tests from the list.")
        return

    selected_names = [listbox.get(i) for i in selected_indices]

    output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if not output_file:
        return

    ExcelExporter.export(selected_names, T0_data, Tn_data, output_file)

def browse_files(entry, combo):
    filenames = filedialog.askopenfilenames(
        title="Select STDF Files",
        filetypes=[("STDF files", "*.stdf"), ("All files", "*.*")]
    )
    if filenames:
        entry.delete(0, tk.END)
        entry.insert(0, ';'.join(filenames))
        combo['values'] = filenames
        combo.set(filenames[-1])

root = tk.Tk()
root.title("Parametric Drift Analysis Tool")

style = ttk.Style()
style.theme_use("clam")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

ttk.Label(frame, text="STDF Files T0:").grid(row=0, column=0, sticky="e")
entry_file1 = ttk.Entry(frame, width=60)
entry_file1.grid(row=0, column=1)
ttk.Button(frame, text="Browse", command=lambda: browse_files(entry_file1, combo_final_T0)).grid(row=0, column=2)

ttk.Label(frame, text="STDF Files Tn:").grid(row=1, column=0, sticky="e")
entry_file2 = ttk.Entry(frame, width=60)
entry_file2.grid(row=1, column=1)
ttk.Button(frame, text="Browse", command=lambda: browse_files(entry_file2, combo_final_Tn)).grid(row=1, column=2)

ttk.Label(frame, text="Select Final Re-Test File for T0:").grid(row=2, column=0, sticky="e")
combo_final_T0 = ttk.Combobox(frame, width=60, state="readonly")
combo_final_T0.grid(row=2, column=1)

ttk.Label(frame, text="Select Final Re-Test File for Tn:").grid(row=3, column=0, sticky="e")
combo_final_Tn = ttk.Combobox(frame, width=60, state="readonly")
combo_final_Tn.grid(row=3, column=1)

ttk.Button(frame, text="Load Tests", command=load_tests).grid(row=4, column=1, pady=10)

ttk.Label(frame, text="Matching Tests:").grid(row=5, column=0, sticky="ne")
listbox = tk.Listbox(frame, width=80, height=12, selectmode=tk.MULTIPLE)
listbox.grid(row=5, column=1, pady=5)

ttk.Button(frame, text="Export to Excel", command=export_to_excel).grid(row=6, column=1, pady=10)

root.mainloop()
