"""
UI
"""
import tkinter as tk
import customtkinter as ctk  # type: ignore[import]
from PIL import Image, ImageTk  # type: ignore[import]

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class MainWindow(ctk.CTk):
    """
    App's main window class.
    """

    def __init__(self):
        super().__init__()
        self.widgets: dict = {}
        self.images: dict = {}

        self.var_score = tk.StringVar()
        self.current_question = tk.StringVar()
        self.current_question.set("This isn't a question yet.")
        self.score = -1

        self.images["true"] = ImageTk.PhotoImage(Image.open("images/true.png"))
        self.images["false"] = ImageTk.PhotoImage(Image.open("images/false.png"))

        self.title("Quizzler")
        self.geometry("340x450")
        self.resizable(False, False)

        self._place_widgets()
        self._update_score()

    def _update_score(self):
        self.score += 1
        self.var_score.set(f"Score: {self.score}")

    def _place_widgets(self):

        self.frame = ctk.CTkFrame(
            master=self,
            width=300,
            height=250,
            corner_radius=20,
        )
        self.frame.grid(
            row=2,
            column=1,
            columnspan=2,
            sticky="nswe",
            padx=20,
            pady=(0, 20),
        )

        self.widgets["lbl_question"] = ctk.CTkLabel(
            width=300,
            height=220,
            master=self.frame,
            textvariable=self.current_question,
            text_font="Arial 16 italic",
            wraplength=430,
            bg_color=None,
        )
        self.widgets["lbl_question"].grid(
            row=0,
            column=0,
            sticky="NEWS",
            pady=15,
        )

        self.widgets["lbl_score"] = ctk.CTkLabel(
            textvariable=self.var_score,
        )
        self.widgets["lbl_score"].grid(
            row=1,
            column=2,
            sticky="NEWS",
            pady=20,
        )

        self.widgets["btn_true"] = ctk.CTkButton(
            text="",
            width=0,
            image=self.images["true"],
            fg_color=None,
            command=lambda: print("True"),
        )
        self.widgets["btn_true"].grid(
            row=3,
            column=1,
            pady=20,
            padx=30,
        )

        self.widgets["btn_false"] = ctk.CTkButton(
            text="",
            width=0,
            image=self.images["false"],
            fg_color=None,
            command=lambda: print("False"),
        )
        self.widgets["btn_false"].grid(
            row=3,
            column=2,
            pady=20,
            padx=30,
        )


def main():
    """
    Main function for easily running the app.
    """
    root = MainWindow()
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
