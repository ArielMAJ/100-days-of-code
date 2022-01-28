import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from passwordGenerator import generate_password
from DBConnection import *


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.labels = {}
        self.buttons = {}
        self.inputs = {}
        self.style = ttk.Style(self)
        self.db_connection = create_connection("./passwords.db")

    # def change_theme(self):
    #     # themes = self.style.theme_names()
    #     # themes = ('winnative', "xpnative", "vista")
    #     current_theme = self.style.theme_use()
    #     self.style.theme_use(themes[themes.index(current_theme)-1])
    #     print(self.style.theme_use())

    def new_password(self):
        self.inputs["tb_password"].delete(0, tk.END)
        password = f"{generate_password()}"
        self.inputs["tb_password"].insert(tk.END, password)
        self.clipboard_clear()
        self.clipboard_append(password)

    def save_to_db(self):
        values = (
            self.inputs["tb_website"].get(),
            self.inputs["tb_username"].get(),
            self.inputs["tb_password"].get()
        )

        for value in values:
            if len(value)<4:
                self.inputs[("tb_website","tb_username","tb_password")[values.index(value)]].focus()
                messagebox.showinfo("Error","Every text box should have at least 4 characters.")
                return

        ok_to_save = messagebox.askokcancel(
            title=values[0],
            message=f"Username: {values[1]}\nPassword: {values[2]}\nPress ok to save.")

        if not ok_to_save:
            return

        insert_data_into_DB(self.db_connection, values)
        messagebox.showinfo("Success","Successfully saved to database.")
        self.inputs['tb_website'].delete(0,tk.END)
        self.inputs['tb_password'].delete(0,tk.END)

    def main(self):
        self.title("Password Manager")
        self.config(padx=30, pady=30)
        self.resizable(width=False, height=False)
        self.style.theme_use("vista")
        amountOfRows=2
        rows = [tk.Frame(self) for _ in range(amountOfRows)]
        [row.pack(side=tk.TOP) for row in rows]

        w=h=200
        logo_img = tk.PhotoImage(file="logo.png")
        self.canvas = tk.Canvas(width=w, height=h, highlightthickness=0)
        self.canvas.create_image(w//2, h//2, image=logo_img, anchor="center")
        self.canvas.pack(in_=rows[0])

        self.labels["lb_website"] = ttk.Label(text="Website:", width=15, anchor='e')
        self.labels["lb_website"].grid(in_=rows[1], row=1, column=0)

        self.labels["lb_username"] = ttk.Label(text="Email/Username:", width=15, anchor='e')
        self.labels["lb_username"].grid(in_=rows[1], row=2, column=0)

        self.labels["lb_password"] = ttk.Label(text="Password:", width=15, anchor='e')
        self.labels["lb_password"].grid(in_=rows[1], row=3, column=0)

        self.inputs["tb_website"] = ttk.Entry(width=40)
        self.inputs["tb_website"].grid(in_=rows[1], row=1, column=1, pady=1)
        self.inputs["tb_website"].focus()

        self.inputs["tb_username"] = ttk.Entry(width=40)
        self.inputs["tb_username"].grid(in_=rows[1], row=2, column=1, pady=1)
        self.inputs["tb_username"].insert(tk.END, "ariel.maj@hotmail.com")

        self.inputs["tb_password"] = ttk.Entry(width=19)
        self.inputs["tb_password"].grid(in_=rows[1], row=3, column=1, sticky="w", padx=1.51, pady=1)

        self.buttons["btn_generate"] = ttk.Button(text="Generate Password", width=19, command=self.new_password)
        self.buttons["btn_generate"].grid(in_=rows[1], row=3, column=1, sticky="e", padx=.5)

        self.buttons["btn_add"] = ttk.Button(text="Add", width=40, command=self.save_to_db)
        self.buttons["btn_add"].grid(in_=rows[1], row=4, column=1)

        # self.buttons["btn_theme"] = ttk.Button(text="Change theme", width=40, command=self.change_theme)
        # self.buttons["btn_theme"].grid(in_=rows[1], row=5, column=1)

        self.mainloop()


if __name__ == "__main__":
    gui = Main()
    gui.main()
