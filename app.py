import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Boykisser Adventure")

# Define fixed window size
window_width = 320
window_height = 240
# CurFrame
curframe = 0
# Define initial position
x_pos = 0
y_pos = 0
# Defines Default background
BgImage = Image.open("assets/sprites/fakeBag.png")
CurBg = ImageTk.PhotoImage(BgImage)
def UpdateBG(path):
    BgImage = Image.open(path)
    CurBg = ImageTk.PhotoImage(BgImage)

# Define initial velocity
x_velocity = 0
y_velocity = 0
def renderbg():
    canvas.create_image(0, 0, anchor=tk.NW, image=CurBg)
def move_image(event):
    global x_pos, y_pos, x_velocity, y_velocity,curframe
    
    # Adjust the velocity based on the arrow key pressed
    if event.keysym == "Right":
        x_velocity = 10
        
    elif event.keysym == "Left":
        x_velocity = -10
    elif event.keysym == "Down":
        y_velocity = 10

    elif event.keysym == "Up":
        y_velocity = -10
    
    # Update the position based on velocity
    x_pos += x_velocity
    y_pos += y_velocity
    print(x_pos)
    print(y_pos)
    # Clear the canvas
    canvas.delete("all")
    
    # Draw the black background
    canvas.create_rectangle(0, 0, window_width, window_height, fill="black")
    renderbg()
    # Draw the image at the updated position
    canvas.create_image(x_pos, y_pos, anchor=tk.NW, image=tk_image)

def release_key(event):
    global x_velocity, y_velocity
    
    # Reset velocity when an arrow key is released
    if event.keysym in {"Right", "Left"}:
        x_velocity = 0
    elif event.keysym in {"Down", "Up"}:
        y_velocity = 0


img2 = Image.open("assets/sprites/bg/grass.png")
CurBg = ImageTk.PhotoImage(img2)

# Set the window size to a fixed value
window.geometry(f"{window_width}x{window_height}")

# Load the image

image = Image.open("assets/sprites/Boykisser.png")  # Replace with your image file path
tk_image = ImageTk.PhotoImage(image)

# Create a Canvas widget with the fixed window size
canvas = tk.Canvas(window, width=window_width, height=window_height)
canvas.pack()

# Draw the black background
canvas.create_rectangle(0, 0, window_width, window_height, fill="black")
# Draw the image on the Canvas
renderbg()

canvas.create_image(x_pos, y_pos, anchor=tk.NW, image=tk_image)

# Make the window non-resizable
window.resizable(False, False)

# Bind arrow key presses and releases to move_image and release_key functions
window.bind("<Right>", move_image)
window.bind("<Left>", move_image)
window.bind("<Down>", move_image)
window.bind("<Up>", move_image)
window.bind("<KeyRelease-Right>", release_key)
window.bind("<KeyRelease-Left>", release_key)
window.bind("<KeyRelease-Down>", release_key)
window.bind("<KeyRelease-Up>", release_key)

window.mainloop()
