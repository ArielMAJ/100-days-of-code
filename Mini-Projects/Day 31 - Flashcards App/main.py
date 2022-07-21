"""
Flash cards app.
"""

import customtkinter  # type: ignore[import]
from PIL import Image, ImageTk  # type: ignore[import]
import pandas as pd  # type: ignore[import]

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class MainWindow(customtkinter.CTk):
    """
    All the app's main functionality should be acessible through this window.
    """

    def __init__(self):
        super().__init__()
        self.widgets: dict = {}
        self.images: dict = {}
        self.background_color: str = "#B1DDC6"
        self.data = None

        self._load_app()
        self.flip_timer = self.after(0, self._next_card)

    def _load_app(self):
        """
        This function will call subfunctions to load the app.
        """
        # self.withdraw()
        self._basic_configs()
        self._place_widgets()
        self._place_window_on_screen()
        # self.deiconify()

    def _basic_configs(self):
        """
        This function should contain all basic configurations such as:
            - All basic tk window configurations;
            - Loading images/files/etc;
        """
        self.title("Flashy")
        self.resizable(width=False, height=False)
        self.config(background=self.background_color)

        self.images["card_front"] = ImageTk.PhotoImage(
            Image.open("./images/card_front.png").resize((800, 526))
        )
        self.images["card_back"] = ImageTk.PhotoImage(
            Image.open("./images/card_back.png").resize((800, 526))
        )
        self.images["cross"] = ImageTk.PhotoImage(
            Image.open("./images/cross_white.png").resize((60, 60))
        )
        self.images["check"] = ImageTk.PhotoImage(
            Image.open("./images/check_white.png").resize((60, 60))
        )

        self.data = pd.read_csv("./data/french_words.csv")
        self.data = self.data.sort_values(by=["Correct", "Total"])

        self.bind("<space>", self.flip_card)
        self.bind("1", self.correct_btn)
        self.bind("2", self.incorrect_btn)

    def _place_widgets(self):
        """
        This function handles creating and placing of widgets.
        """

        self.widgets["frame_for_card"] = customtkinter.CTkFrame(
            master=self,
            width=535,
            height=350,
            fg_color=None,
        )
        self.widgets["frame_for_card"].grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(30, 0),
            padx=40,
        )
        self.widgets["frame_for_card"].canvas.bind("<Button-1>", self.flip_card)

        self.widgets["canvas_image_item"] = self.widgets[
            "frame_for_card"
        ].canvas.create_image(
            0,
            0,
            image=self.images["card_front"],
            anchor="nw",
        )
        self.widgets["canvas_title_item"] = self.widgets[
            "frame_for_card"
        ].canvas.create_text(
            400,
            150,
            text="Title",
            fill="black",
            font=("Arial 30 italic"),
            anchor="center",
        )
        self.widgets["canvas_word_item"] = self.widgets[
            "frame_for_card"
        ].canvas.create_text(
            400,
            263,
            text="Word",
            fill="black",
            font=("Arial 50 bold"),
            anchor="center",
        )

        self.widgets["btn_V"] = customtkinter.CTkButton(
            self,
            corner_radius=21,
            text="",
            width=70,
            height=70,
            fg_color="#07B36E",
            hover_color="#51C956",
            image=self.images["check"],
            command=self.correct_btn,
        )
        self.widgets["btn_V"].grid(
            row=2,
            column=0,
            pady=(5, 15),
            padx=(100, 0),
        )
        self.widgets["btn_X"] = customtkinter.CTkButton(
            self,
            corner_radius=21,
            text="",
            width=70,
            height=70,
            fg_color="#D33A40",
            hover_color="#ED3458",
            image=self.images["cross"],
            command=self.incorrect_btn,
        )
        self.widgets["btn_X"].grid(
            row=2,
            column=1,
            pady=(5, 15),
            padx=(0, 100),
        )

    def _place_window_on_screen(self):
        self.update()

        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        offset = {
            "x": int(0.5 * self.winfo_screenwidth() - width // 2),
            "y": int(0.5 * self.winfo_screenheight() - height // 2 - 20),
        }

        self.geometry(f"{width}x{height}+{offset['x']}+{offset['y']}")
        self.set_scaling(1, 1, 1)

    @property
    def canvas_title(self):
        """
        Returns current title on canvas.
        """
        return self.widgets["frame_for_card"].canvas.itemcget(
            self.widgets["canvas_title_item"], "text"
        )

    @canvas_title.setter
    def canvas_title(self, canvas_title):
        """
        Sets title on canvas.
        """
        self.widgets["frame_for_card"].canvas.itemconfig(
            self.widgets["canvas_title_item"], text=canvas_title
        )

    @property
    def canvas_word(self):
        """
        Returns current word on canvas.
        """
        return self.widgets["frame_for_card"].canvas.itemcget(
            self.widgets["canvas_word_item"], "text"
        )

    @canvas_word.setter
    def canvas_word(self, canvas_word):
        """
        Sets word on canvas.
        """
        self.widgets["frame_for_card"].canvas.itemconfig(
            self.widgets["canvas_word_item"], text=canvas_word
        )

    @property
    def canvas_image(self):
        """
        Returns current word on canvas.
        """
        return self.widgets["frame_for_card"].canvas.itemcget(
            self.widgets["canvas_image_item"], "image"
        )

    @canvas_image.setter
    def canvas_image(self, canvas_image):
        """
        Sets word on canvas.
        """
        self.widgets["frame_for_card"].canvas.itemconfig(
            self.widgets["canvas_image_item"], image=canvas_image
        )

    def _next_card(self):
        self.after_cancel(self.flip_timer)

        self.canvas_image = self.images["card_front"]
        self.canvas_title = "French"
        self.canvas_word = self.data.at[0, "French"]

        self.flip_timer = self.after(3000, self.flip_card)

    def flip_card(self, _event=None):
        """
        This is called after 3 seconds that a new card is shown or upon pressing space bar.
        It will flip the card.
        """
        self.after_cancel(self.flip_timer)

        if self.canvas_title == self.data.columns[0]:
            self.canvas_image = self.images["card_back"]
            self.canvas_title = "English"
            self.canvas_word = self.data.at[0, "English"]
        else:
            self.canvas_image = self.images["card_front"]
            self.canvas_title = "French"
            self.canvas_word = self.data.at[0, "French"]

    def correct_btn(self, _event=None):
        """
        This function is called by either pressing "1" or clicking on the green button.
        It will add the correct&total counter and go to the next card.
        """
        self.data.at[0, "Correct"] += 1
        self.data.at[0, "Total"] += 1
        self.save_to_csv()
        self._next_card()

    def incorrect_btn(self, _event=None):
        """
        This function is called by either pressing "2" or clicking on the red button.
        It will add only to the total counter and go to the next card.
        """
        self.data.at[0, "Total"] += 1
        self.save_to_csv()
        self._next_card()

    def save_to_csv(self):
        """
        Saves the current state of the dataframe back to its original path.
        """
        self.data = self.data.sort_values(by=["Correct", "Total"])
        self.data.to_csv("./data/french_words.csv", index=False)
        self.data.reset_index(inplace=True, drop=True)


def main() -> int:
    """
    This function will run the app.
    """
    root = MainWindow()
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
