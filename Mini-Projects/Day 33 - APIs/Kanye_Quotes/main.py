from tkinter import *
import requests


def get_quote():
    url = r"https://api.kanye.rest/"
    resp = requests.get(url)
    resp.raise_for_status()

    quote = resp.json()["quote"]
    print(len(quote))
    canvas.itemconfig(quote_text, text=quote)
    if len(quote)>100:
        canvas.itemconfig(quote_text, font=("Arial", 13, "bold"))
    if len(quote)>180:
        canvas.itemconfig(quote_text, font=("Arial", 12, "bold"))
    else:
        canvas.itemconfig(quote_text, font=("Arial", 17, "bold"))


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="...", width=250, font=("Arial", 17, "bold"), fill="black")
canvas.grid(row=0, column=0)
get_quote()

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()