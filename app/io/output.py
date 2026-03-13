def output_console(text):
    print(text)



def output_in_file(filepath, text):
    with open(filepath, "w") as f:
        f.write(text)