import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os


class App:
    def __init__(self, master, filename):
        self.master = master
        self.image = None
        self.filename = 'img/' + filename
        self.canvas = tk.Canvas(master, width=900, height=900)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.count = 0

        self.open_image()

    def open_image(self):
        self.image = Image.open(self.filename)
        print(self.filename)
        self.canvas.config(width=900, height=900)

        w, h = self.image.size
        if w > 900:
            h = int(h * 900 / w)
            w = 900
        if h > 900:
            w = int(w * 900 / h)
            h = 900
        self.image = self.image.resize((w, h))

        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1, outline='red')

    def on_move_press(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        x = min(self.start_x, self.canvas.canvasx(event.x))
        y = min(self.start_y, self.canvas.canvasy(event.y))
        w = abs(self.start_x - self.canvas.canvasx(event.x))
        h = abs(self.start_y - self.canvas.canvasy(event.y))
        if w and h:
            # Ask user if top or bottom piece
            response = tk.messagebox.askquestion("Piece Position", "Is this a top or bottom piece?\n"
                                                                   "yes if top, no if bottom")
            if response == 'yes':
                piece_position = 'top'
            else:
                piece_position = 'btm'

            # Save the cropped image with a filename suffix
            file_name = os.path.splitext(os.path.basename(self.filename))[0]
            folder_name = 'cropped'
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            file_path = os.path.join(folder_name, f"{file_name}_cropped_{piece_position}.png")
            self.image.crop((x, y, x + w, y + h)).save(file_path)
            self.count += 1

            # Display the original image on canvas
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)
        self.rect = None
