import pandas as pd


def input_console():
    """
        Read text input from the console.
        Returns: text entered by the user in the console.
        """
    txt = input("enter text: ")
    return txt

def input_file(filepath):
    """
       Read text from a file using built-in python tools.
       arguments: filepath (str): path to the file that should be read
       Returns: content of the file as a string.
       """
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def read_pandas(filepath):
    """
      Read file content using pandas.
      arguments: filepath (str): path to a CSV file.
      Returns: file content converted to string
      """
    df = pd.read_csv(filepath)
    return df.to_string()


