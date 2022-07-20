import customtkinter as ctk

root = ctk.CTk()
root.config(background="white")
root.geometry("540x340")

widgets = {}
corner_radius = 30

widgets["frame_for_card"] = ctk.CTkFrame(
    master=root,
    width=500,
    height=300,
    corner_radius=0,
    fg_color=None,
)
widgets["frame_for_card"].grid(
    row=1,
    column=0,
    columnspan=2,
    pady=20,
    padx=20,
)

widgets["frame_card_shadow"] = ctk.CTkFrame(
    master=widgets["frame_for_card"],
    width=495,
    height=295,
    corner_radius=corner_radius,
    fg_color="black",
    bg_color=None,
)
widgets["frame_card_shadow"].place(
    relx=1,
    rely=1,
    anchor="se",
)

widgets["frame_card_main"] = ctk.CTkFrame(
    master=widgets["frame_for_card"],
    width=495,
    height=295,
    corner_radius=corner_radius,
    bg_color=None,
    fg_color="red",
)
widgets["frame_card_main"].place(
    relx=0,
    rely=0,
    anchor="nw",
)

bottom = 700
right = 400

widgets["frame_card_main"].canvas.create_rectangle(
    corner_radius + 5,
    corner_radius + 5,
    bottom,
    right + 50,
    fill="black",
)
widgets["frame_card_main"].canvas.create_rectangle(
    corner_radius + 5,
    corner_radius + 5,
    bottom + 50,
    right,
    fill="black",
)
widgets["frame_card_main"].canvas.create_oval(
    *(i + 6 for i in widgets["frame_card_shadow"].canvas.bbox(4)),
    fill="black",
)
widgets["frame_card_main"].canvas.create_oval(
    *(i + 6 for i in widgets["frame_card_shadow"].canvas.bbox(6)),
    fill="black",
)
widgets["frame_card_main"].canvas.create_oval(
    *(i + 6 for i in widgets["frame_card_shadow"].canvas.bbox(8)),
    fill="black",
)

widgets["frame_card_main"].canvas.tag_lower(11)
widgets["frame_card_main"].canvas.tag_lower(12)
widgets["frame_card_main"].canvas.tag_lower(13)
widgets["frame_card_main"].canvas.tag_lower(14)
widgets["frame_card_main"].canvas.tag_lower(15)


widgets["frame_card_main"].configure(fg_color="gray")

# If you call "configure" you'll probably have to lower all the new canvas widgets.
widgets["frame_card_main"].canvas.tag_lower(11)
widgets["frame_card_main"].canvas.tag_lower(12)
widgets["frame_card_main"].canvas.tag_lower(13)
widgets["frame_card_main"].canvas.tag_lower(14)
widgets["frame_card_main"].canvas.tag_lower(15)
root.mainloop()
