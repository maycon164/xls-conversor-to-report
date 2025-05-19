from datetime import time, datetime
import pandas as pd

def read_file(file, cols):
    content = pd.read_excel(file,usecols=cols)
    rows = []
    for index, row in content.iterrows():
        rows.append(row.to_dict())
    return rows
