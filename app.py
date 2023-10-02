import tkinter as tk
from PIL import Image, ImageTk

# Define fixed window size
window_width = 320
window_height = 240

# Define initial position
x_pos = 0
y_pos = 0

# Define initial velocity
x_velocity = 0
y_velocity = 0

def move_image(event):
    global x_pos, y_pos, x_velocity, y_velocity
    
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
    
    # Clear the canvas
    canvas.delete("all")
    
    # Draw the black background
    canvas.create_rectangle(0, 0, window_width, window_height, fill="black")
    
    # Draw the image at the updated position
    canvas.create_image(x_pos, y_pos, anchor=tk.NW, image=tk_image)

def release_key(event):
    global x_velocity, y_velocity
    
    # Reset velocity when an arrow key is released
    if event.keysym in {"Right", "Left"}:
        x_velocity = 0
    elif event.keysym in {"Down", "Up"}:
        y_velocity = 0

window = tk.Tk()
window.title("Move Image with Arrow Keys")

# Set the window size to a fixed value
window.geometry(f"{window_width}x{window_height}")

# Load the image
image = Image.open("assets/sprites/Ship.png")  # Replace with your image file path
tk_image = ImageTk.PhotoImage(image)

# Create a Canvas widget with the fixed window size
canvas = tk.Canvas(window, width=window_width, height=window_height)
canvas.pack()

# Draw the black background
canvas.create_rectangle(0, 0, window_width, window_height, fill="black")

# Draw the image on the Canvas
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
