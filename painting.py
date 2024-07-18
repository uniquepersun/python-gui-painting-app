import tkinter as tk
from PIL import Image

class PaintApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Drawing App")

    self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
    self.canvas.pack(fill=tk.BOTH, expand=True)

    self.drawing = False
    self.selected_shape = "line"
    self.last_x = None
    self.last_y = None
    self.brush_color = "black"
    self.brush_size = 5

    self.canvas.bind("<Button-1>", self.start_drawing)
    self.canvas.bind("<B1-Motion>", self.draw)
    self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    self.color_picker_button = tk.Button(self.root,text="pick a nice color..", command=self.pick_color)
    self.color_picker_button.pack(side=tk.LEFT)
    
    self.shape_options = tk.StringVar(self.root)
    self.shape_options.set("line")
    shape_frame = tk.Frame(self.root)
    shape_frame.pack(side=tk.LEFT)
    for shape in ["line","rectangle","oval"]:
      shape_button = tk.Radiobutton(shape_frame, text=shape,variable=self.shape_options,value=shape,command=lambda s = shape:self.shape_options(s))
      shape_button.pack(side=tk.LEFT)

    self.clear_button = tk.Button(self.root, text="clear",command=self.clear_canvas)
    self.clear_button.pack(side=tk.LEFT)

    self.brush_size_label = tk.Label(self.root, text="Brush Size")
    self.brush_size_label.pack(side=tk.LEFT)
    self.brush_size_slider = tk.Scale(self.root, from_=1, to=20,orient=tk.HORIZONTAL,command=self.brush_size)
    self.brush_size_slider.set(self.brush_size)
    self.brush_size_slider.pack(side=tk.LEFT)

    self.save_button = tk.Button = tk.Button(self.root,text="save",command=self.save_drawing)
    self.save_button.pack(side=tk.LEFT)


  def start_drawing(self, event):
    self.drawing = True
    self.last_x = event.x
    self.last_y = event.y

  def draw(self, event):
    if self.drawing:
      shape = self.selected_shape
      if shape == "line":
        self.canvas.create_line(self.last_x,self.last_y,event.x,event.y,fill=self.brush_color,width=self.brush_size)
      elif shape == "rectangle":
        self.canvas.create_rectangle(self.last_x,self.last_y,event.x,event.y,fill=self.brush_color,width=self.brush_size)
      elif shape == "oval":
        self.canvas.create_oval(self.last_x,self.last_y,event.x,event.y,fill="",outline=self.brush_color,width=self.brush_size)
      self.last_x = event.x
      self.last_y = event.y

  def clear_canvas(self):
    self.canvas.delete("all")

  def stop_drawing(self):
    self.drawing = False

  def pick_color(self):
        color_picker = tk.Toplevel(self.root)
        color_picker.title("Pick Color")

        colors = ["red", "green", "blue", "yellow", "black", "white"]

        def set_color(color):
            self.brush_color = color
            color_picker.destroy()

        for color in colors:
            color_button = tk.Button(color_picker, text=color.capitalize(),command=lambda c=color: set_color(c))
            color_button.pack(side=tk.LEFT)

  def save_drawing(self):
    image_data = self.canvas.postscript(colormode='color')
    image = Image.frombytes('RGB', (self.canvas.winfo_width(), self.canvas.winfo_height()), image_data)

    save_path = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])

    if save_path:
      try:
        image.save(save_path)
        print("Drawing saved successfully!")
      except Exception as e:
        print("Error saving image:", e)
        
root = tk.Tk()
app = PaintApp(root)

root.mainloop()
