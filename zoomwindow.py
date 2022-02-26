import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk


class HiddenScrollbar(ttk.Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
        ttk.Scrollbar.set(self, lo, hi)


class ZoomWindow(ttk.Frame):
    def __init__(self, base_frame, image_path):
        """
        This function renders the main window
        :param base_frame: The parent widget
        :param image_path: Image path
        """
        ttk.Frame.__init__(self, master=base_frame)
        self.master.title('Image Zoom by Mouse Wheel')
        vertical_scroll_bar = HiddenScrollbar(self.master, orient='vertical')
        horizontal_scroll_bar = HiddenScrollbar(self.master, orient='horizontal')
        vertical_scroll_bar.grid(row=0, column=1, sticky='ns')
        horizontal_scroll_bar.grid(row=1, column=0, sticky='we')
        self.image = Image.open(image_path)
        self.canvas = tk.Canvas(self.master, xscrollcommand=horizontal_scroll_bar.set, highlightthickness=0,
                                yscrollcommand=vertical_scroll_bar.set)
        self.canvas.grid(row=0, column=0, sticky='news')
        vertical_scroll_bar.configure(command=self.canvas.yview)
        horizontal_scroll_bar.configure(command=self.canvas.xview)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.canvas.bind('<ButtonPress-1>', self.move_mouse_from)
        self.canvas.bind('<B1-Motion>', self.move_mouse_to)
        self.canvas.bind('<MouseWheel>', self.scroll_wheel)
        self.canvas.bind('<Button-5>', self.scroll_wheel)
        self.canvas.bind('<Button-4>', self.scroll_wheel)
        self.im_scale = 1.0
        self.image_id = None
        self.delta = 0.75
        self.text = self.canvas.create_text(0, 0, anchor='nw', text='Scroll to zoom')
        self.render_image()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def move_mouse_from(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def move_mouse_to(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def scroll_wheel(self, event):
        scale = 1.0
        if event.num == 5 or event.delta == -120:
            scale *= self.delta
            self.im_scale *= self.delta
        if event.num == 4 or event.delta == 120:
            scale /= self.delta
            self.im_scale /= self.delta
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.canvas.scale('all', x, y, scale, scale)
        self.render_image()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def render_image(self):
        if self.image_id:
            self.canvas.delete(self.image_id)
            self.image_id = None
            self.canvas.image_tk = None
        width, height = self.image.size
        new_size = int(self.im_scale * width), int(self.im_scale * height)
        image_tk = ImageTk.PhotoImage(self.image.resize(new_size))
        self.image_id = self.canvas.create_image(self.canvas.coords(self.text), anchor='nw', image=image_tk)
        self.canvas.lower(self.image_id)
        self.canvas.image_tk = image_tk


