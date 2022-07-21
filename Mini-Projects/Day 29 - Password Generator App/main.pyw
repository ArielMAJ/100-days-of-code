import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from passwordGenerator import generate_password
import DBConnection


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.labels = {}
        self.buttons = {}
        self.inputs = {}
        self.style = ttk.Style(self)
        self.db_connection = DBConnection.create_connection("./passwords.db")
        self.searchResults = []
        self.table = None
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
            title="Confirm the information",
            message=f"Website: {values[0]}\nUsername: {values[1]}\nPassword: {values[2]}\n\nPress ok to save.")

        if not ok_to_save:
            return

        DBConnection.insert_data_into_DB(self.db_connection, values)
        messagebox.showinfo("Success","Successfully saved to database.")
        self.inputs['tb_website'].delete(0,tk.END)
        self.inputs['tb_password'].delete(0,tk.END)

    def from_db_to_table(self):
        self.searchResults = DBConnection.fetch_data_from_DB(self.db_connection, self.inputs['tb_searchWord'].get())
        self.table.delete(*self.table.get_children())

        for row in self.searchResults:
            self.table.insert(parent='',index='end',iid=row[0],text='',
            values=row)

    def cpyRowInfo(self,info_to_copy):
        row_number = self.table.focus()
        full_row_data = self.table.item(row_number)
        row_as_in_db = full_row_data['values']
        self.clipboard_clear()
        self.clipboard_append(row_as_in_db[info_to_copy])

    def deleteSelectedRow(self):
        row_number = self.table.focus()
        full_row_data = self.table.item(row_number)
        values = full_row_data['values'][1:]

        ok_to_delete = messagebox.askokcancel(
            title="Confirm the information",
            message=f"Website: {values[0]}\nUsername: {values[1]}\nPassword: {values[2]}\n\nPress ok to delete.")
        if not ok_to_delete:
            self.inputs['tb_searchWord'].focus()
            return

        DBConnection.delete_data_from_DB(self.db_connection, row_number)
        self.from_db_to_table()
        self.inputs['tb_searchWord'].focus()
        
    def passwords_table(self):
        topLevel = tk.Tk()
        topLevel.attributes('-topmost', True)
        topLevel.update()

        amountOfRows = 3
        rows = [tk.Frame(topLevel) for _ in range(amountOfRows)]
        [row.pack(in_=topLevel, side=tk.TOP) for row in rows]

        topLevel.title("Passwords")
        this_style = ttk.Style(topLevel)
        this_style.theme_use("vista")
        topLevel.resizable(width=False, height=False)

        self.table = ttk.Treeview(topLevel, selectmode="browse")

        self.inputs['tb_searchWord'] = ttk.Entry(topLevel, width=75)
        self.inputs['tb_searchWord'].pack(in_=rows[0])
        self.buttons['btn_search'] = ttk.Button(
            topLevel,
            text="Search Website's Password",
            command=self.from_db_to_table,
            width=74
        )
        self.buttons['btn_search'].pack(in_=rows[0])
        self.from_db_to_table()
        self.table.pack(in_=rows[0])

        self.table['columns']= ('id', 'website','username',"password")
        self.table.column("#0", width=0,  stretch=tk.NO)
        self.table.column("id",anchor=tk.CENTER, width=30)
        self.table.column("website",anchor=tk.CENTER, width=120)
        self.table.column("username",anchor=tk.CENTER, width=150)
        self.table.column("password",anchor=tk.CENTER, width=150)



        self.table.heading("#0",text="",anchor=tk.CENTER)
        self.table.heading("id",text="ID",anchor=tk.CENTER)
        self.table.heading("website",text="Website",anchor=tk.CENTER)
        self.table.heading("username",text="Username",anchor=tk.CENTER)
        self.table.heading("password",text="Password",anchor=tk.CENTER)



        self.buttons['btn_cpyWeb'] = ttk.Button(
            topLevel,
            text="Copy Website",
            command=lambda:self.cpyRowInfo(1),
            width=20
        )
        self.buttons['btn_cpyWeb'].pack(in_=rows[1], side=tk.LEFT)


        self.buttons['btn_cpyAcc'] = ttk.Button(
            topLevel,
            text="Copy Account",
            command=lambda:self.cpyRowInfo(2),
            width=20
        )
        self.buttons['btn_cpyAcc'].pack(in_=rows[1], side=tk.LEFT)


        self.buttons['btn_cpyPass'] = ttk.Button(
            topLevel,
            text="Copy Password",
            command=lambda:self.cpyRowInfo(3),
            width=30
        )
        self.buttons['btn_cpyPass'].pack(in_=rows[1], side=tk.LEFT)


        self.buttons['btn_deleteRow'] = ttk.Button(
            topLevel,
            text="Delete Selected Row",
            command=self.deleteSelectedRow,
            width=74
        )
        self.buttons['btn_deleteRow'].pack(in_=rows[2], side=tk.LEFT)


    def main(self):
        self.title("Password Manager")
        self.config(padx=30, pady=30)
        self.resizable(width=False, height=False)
        self.style.theme_use("vista")

        amountOfRows=2
        rows = [tk.Frame(self) for _ in range(amountOfRows)]
        [row.pack(side=tk.TOP) for row in rows]

        w=h=200
        lock_img = tk.PhotoImage(file="lock.png")
        self.iconphoto(True, lock_img)
        self.canvas = tk.Canvas(width=w, height=h, highlightthickness=0)
        logo_img = tk.PhotoImage(file="logo.png")
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

        self.buttons["btn_openDB"] = ttk.Button(rows[1], text="Open DB", width=40, command=self.passwords_table)
        self.buttons["btn_openDB"].grid(in_=rows[1], row=5, column=1)

        self.mainloop()


if __name__ == "__main__":
    gui = Main()
    gui.main()
