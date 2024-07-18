import tkinter as tk

class PaintApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Drawing App")

    self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
    self.canvas.pack(fill=tk.BOTH, expand=True)

    self.last_x = None
    self.last_y = None
    self.brush_color = "black"
    self.brush_size = 5

    self.canvas.bind("<Button-1>", self.start_drawing)
    self.canvas.bind("<B1-Motion>", self.draw)
    self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

  def start_drawing(self, event):
    self.drawing = True
    self.last_x = event.x
    self.last_y = event.y

  def draw(self, event):
    if self.drawing:
      self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                              fill=self.brush_color, width=self.brush_size)
      self.last_x = event.x
      self.last_y = event.y

  def stop_drawing(self):
    self.drawing = False

root = tk.Tk()
app = PaintApp(root)

root.mainloop()
