def output_console(text):
    """
      Print text to the console.
      Arguments: text that will be displayed in the console.
      """
    print(text)

def output_in_file(filepath, text):
    """
       Write text to a file using built-in tools.
       Arguments: filepath (str): path to the file where text will be saved,text (str): text that should be written down into the file"""
    with open(filepath, "w") as f:
        f.write(text)