import tkinter as tk
# import random
# from tkinter_custom import tkinterCustom


def main():
    font = ("Arial", 15)

    def button_clicked():
        my_label3_result.config(text=f"{float(miles_input.get())*1.609344:.2f}", font=font)

    window = tk.Tk()
    window.title("Program")
    # window.minsize(width=800//3, height=600//3)
    window.config(padx=20, pady=20)

    miles_input = tk.Entry()
    miles_input.insert(tk.END, '0')
    miles_input.config(width=5)
    miles_input.grid(column=1, row=0)

    my_label1 = tk.Label(text="Miles", font=font)
    my_label1.grid(column=2, row=0)

    my_label2 = tk.Label(text="is equal to", font=font)
    my_label2.grid(column=0, row=1)

    my_label3_result = tk.Label(text="0", font=font)
    my_label3_result.grid(column=1, row=1)

    my_label4 = tk.Label(text="Km", font=font)
    my_label4.grid(column=2, row=1)

    button = tk.Button(text="Calculate", command=button_clicked)
    button.grid(column=1, row=2)

    window.mainloop()


if __name__ == "__main__":
    main()
