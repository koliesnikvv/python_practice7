from app.io.input import(input_console, input_file, read_pandas)
from app.io.output import (
output_console,
output_in_file
)

def main():
    input_console = input_console.input_console()
    input_file = input_file.input_file("data/input.txt")
    read_pandas = read_pandas.read_pandas("data/input.csv")
    output_console = output_console.output_console("data/output.csv")

