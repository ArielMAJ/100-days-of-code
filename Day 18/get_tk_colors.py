import requests


def in_tcltk_website(text):
    """Receives the tcltk website text string and returns the range where the colors are written."""
    start = text.find('<PRE>') + len('<PRE>')
    end = text.find('</PRE>')
    colors = text[start:end]
    return colors


def to_txt_file(file_name = 'tk_colors'):
    """Better avoid this one and use 'as_simple_file_list()'.
Makes a txt file with what's returned from 'in_tcltk_website()'."""
    url = "https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html"
    response = requests.get(url)
    text = response.text

    colors = in_tcltk_website(text)
    with open(f'{file_name}.txt','w') as page_text:
        page_text.write(colors)


def as_string():
    """Return a string with the colors in 'bad formatting'."""
    url = "https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html"
    response = requests.get(url)
    return in_tcltk_website(response.text)


def colors_list_from_website() -> list:
    """Gets the colors from the tk_colors.txt when it exists, else from the website.
Turns the text into a nice, clean, list and returns it."""
    file_name = 'tk_colors'
    try:
        with open(f"{file_name}.txt", 'r') as txt:
            lst = txt.read().split('\n')
    except:
        lst = as_string().split('\n')
    colors_pretty_list = [line.split('  ')[0] for line in lst[1:]]
    return colors_pretty_list


def colors_list() -> list:
    """Returns a tk color list from colors.txt when it exists, else returns 'colors_list_from_website()'."""
    try:
        with open(f"colors.txt", 'r') as txt:
            return txt.read().split('\n')
    except:
        return colors_list_from_website()


def as_simple_file_list():
    """Creates a file with the colors. One color per line. ("good formatting")."""
    with open(f"colors.txt", 'w') as txt:
        txt.write('\n'.join(colors_list()))


def main():
    """Simply runs 'as_simple_file_list()'."""
    # to_txt_file()
    as_simple_file_list()


if __name__ == "__main__":
    main()