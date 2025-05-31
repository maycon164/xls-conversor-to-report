import pandas as pd


class ReportXLSXReader:

    def read_file(self, file, cols):
        content = pd.read_excel(file, usecols=cols)
        rows = []
        for index, row in content.iterrows():
            rows.append(row.to_dict())
        return self.sanitize_rows(rows)

    def sanitize_rows(self, rows: list):
        if len(rows) != 0:
            rows.pop()
        return rows