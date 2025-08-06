import pandas as pd
from pystdf.Importer import STDF2DataFrame

class STDFProcessor:
    @staticmethod
    def consolidate_retests(file_paths, final_file):
        combined = {}
        for path in file_paths:
            ptr_dict = STDF2DataFrame(path)
            for section, df in ptr_dict.items():
                if not isinstance(df, pd.DataFrame):
                    continue
                if path != final_file and 'TEST_FLG' in df.columns:
                    df = df[df['TEST_FLG'] == 0]
                if section not in combined:
                    combined[section] = df.copy()
                else:
                    combined[section] = pd.concat([combined[section], df], ignore_index=True)
        return combined

    @staticmethod
    def tests(ptr_dict):
        return ptr_dict['PTR'][['TEST_TXT', 'RESULT']].dropna(subset=['TEST_TXT'])

    @staticmethod
    def shared_tests(ptr1, ptr2):
        names1 = set(ptr1['TEST_TXT'].dropna())
        names2 = set(ptr2['TEST_TXT'].dropna())
        return sorted(names1.intersection(names2))
