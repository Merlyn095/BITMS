import pandas as pd


def add_id(id_number):
    df = pd.read_excel('progress.xlsx')
   
    new_row = {'ID': id_number}
    df = df._append(new_row, ignore_index=True)

   
    df.to_excel('progress.xlsx', index=False)
