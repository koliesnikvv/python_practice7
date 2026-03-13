import pandas as pd


def input_console():
    txt = input("enter text: ")
    return txt

def input_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def read_pandas(filepath):
    df = pd.read_csv(filepath)
    return df.to_string()


