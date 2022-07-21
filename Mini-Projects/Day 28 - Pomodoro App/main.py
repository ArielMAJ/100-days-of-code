import tkinter as tk
from PIL import Image, ImageTk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

def load_img(path,size):
    return ImageTk.PhotoImage(Image.open(path).resize(size))

class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window_bg_color = YELLOW
        self.labels = {}
        self.buttons = {}
        self.title_font = (FONT_NAME, 50, "bold")
        self.timer_id="start_timer"
        self.timer = None
        self.time = 0
        self.focusing = True

        self.canvas = tk.Canvas(width=200, height=224, bg=self.window_bg_color, highlightthickness=0)
        self.checkmark = "✓"

        self.sessions = 0

        self.WORK_SEC= 25*60 # 25*60
        self.SHORT_BREAK_SEC = 5*60 # 5*60
        self.LONG_BREAK_SEC = 15*60 #15*60

    # ---------------------------- TIMER RESET ------------------------------- #
    def reset_timer(self):
        if self.timer != None:
            self.window.after_cancel(self.timer)
            self.timer = None
        self.canvas.itemconfig(self.timer_id, text="Press\nplay")
        self.labels["title"].config(text="Timer", fg = GREEN, font = self.title_font)
        self.time = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start_timer(self):
        if self.timer is not None:
            self.window.after_cancel(self.timer)
            self.timer = None
            return
        elif self.time == 0:
            self.labels["title"].config(text="Focusing", fg=GREEN)  # , font = (FONT_NAME, 35, "bold"))
            self.time = self.WORK_SEC
            self.focusing = True
            self.count_down()
        else:
            self.count_down()


    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def count_down(self):
        if self.time>0:
            self.canvas.itemconfig(self.timer_id, text=f"{str(self.time // 60).zfill(2)}:{str(self.time % 60).zfill(2)}")
            self.time -= 1
            self.timer = self.window.after(1000, self.count_down)
        elif self.time<=0 and self.focusing:
            self.canvas.itemconfig(self.timer_id, text=f"{str(self.time // 60).zfill(2)}:{str(self.time % 60).zfill(2)}")
            self.sessions += 1
            self.labels["checkmarks"].config(text=self.checkmark*self.sessions)
            self.labels["title"].config(text="Pause")
            self.focusing = False
            if self.sessions % 4 == 0:
                self.labels["title"]['fg']=RED
                self.time = self.LONG_BREAK_SEC
            else:
                self.labels["title"]['fg']=PINK
                self.time = self.SHORT_BREAK_SEC
            self.count_down()
        elif self.time<=0 and not self.focusing:
            self.canvas.itemconfig(self.timer_id, text=f"{str(self.time // 60).zfill(2)}:{str(self.time % 60).zfill(2)}")
            self.labels["title"].config(text="Finished", fg=GREEN)
            self.timer = None


    # ---------------------------- UI SETUP ------------------------------- #
    def main(self):
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)
        tomato_img = tk.PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=tomato_img, anchor="center")
        self.canvas.create_text(100, 138, text="Press\nplay", justify="center", fill="white", font=(FONT_NAME, 35, "bold"), tags=self.timer_id)
        self.canvas.grid(row=1, column=1)

        self.labels["title"] = tk.Label(text="Timer", fg=GREEN, bg=self.window_bg_color, font=self.title_font, width= 10)
        self.labels["title"].grid(row=0, column=1)

        img_play = load_img("play.png",(80,80))
        self.buttons["start"] = tk.Button(image=img_play, command=self.start_timer, border=0, bg=self.window_bg_color, activebackground=self.window_bg_color)
        self.buttons["start"].grid(row=2, column=0)

        img_reset = load_img("restart.png",(90,90))
        self.buttons["reset"] = tk.Button(image=img_reset, command=self.reset_timer, border=0, bg=self.window_bg_color, activebackground=self.window_bg_color)
        self.buttons["reset"].grid(row=2, column=2)

        self.labels["checkmarks"] = tk.Label(text=self.checkmark*self.sessions, fg=GREEN, bg=self.window_bg_color, font=(FONT_NAME, 20, 'bold'))
        self.labels["checkmarks"].grid(row=3, column=1)

        self.window.mainloop()


if __name__ == "__main__":
    gui = Main()
    gui.main()
