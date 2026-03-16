from app.io.input import input_console, input_file, read_pandas
from app.io.output import output_console, output_in_file


def main():
    console_text = input_console()
    file_text = input_file("data/input.txt")
    pandas_text = read_pandas("data/input.csv")
    output_console(console_text)
    output_console(file_text)
    output_console(pandas_text)

    combined_text = f"{console_text}\n{file_text}\n{pandas_text}"

    output_in_file("data/output.txt", combined_text)


if __name__ == "__main__":
    main()