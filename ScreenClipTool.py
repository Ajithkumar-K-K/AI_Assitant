import tkinter as tk
from PIL import Image, ImageGrab, ImageTk
import os
import tempfile

class ScreenClipTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screen Clipper")
        self.root.attributes("-fullscreen", True)  # Fullscreen mode
        self.root.bind("<ButtonPress-1>", self.on_mouse_press)
        self.root.bind("<B1-Motion>", self.on_mouse_drag)
        self.root.bind("<ButtonRelease-1>", self.on_mouse_release)

        self.start_x = self.start_y = 0
        self.rect = None
        self.screenshot_path = None  # Variable to store the screenshot path
        self.cropped_image_path = None  # Variable to store the cropped image path
        self.original_image = None  # Variable to store the original image

        # Create a canvas to draw the rectangle
        self.canvas = tk.Canvas(self.root, cursor="cross", bd=0, highlightthickness=0)  # Removed border and highlight thickness
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Capture the screen
        self.screenshot_path = self.capture_screen()

        self.load_background_image()  # Load and display the screenshot as background

        self.root.mainloop()

    def capture_screen(self):
        # Capture the screenshot and save it to a temporary file
        screenshot = ImageGrab.grab()
        temp_dir = tempfile.gettempdir()
        screenshot_path = os.path.join(temp_dir, "full_screenshot.png")
        screenshot.save(screenshot_path)
        return screenshot_path

    def load_background_image(self):
        self.original_image = Image.open(self.screenshot_path)
        self.resize_and_display_background_image()

    def resize_and_display_background_image(self):
        # Get the screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Resize the image to fit within the screen dimensions without losing quality
        self.background_image = self.original_image.resize((screen_width, screen_height), Image.LANCZOS)

        # Update the canvas size to fill the screen
        self.canvas.config(width=screen_width, height=screen_height)

        # Convert the image to PhotoImage and display it on the canvas
        self.bg_photo = ImageTk.PhotoImage(self.background_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)

        # Store the ratio to calculate the original coordinates later
        self.width_ratio = self.original_image.width / screen_width
        self.height_ratio = self.original_image.height / screen_height

    def on_mouse_press(self, event):
        self.start_x, self.start_y = event.x, event.y
        if self.rect:
            self.canvas.delete(self.rect)
        # Create rectangle with fluorescent green outline and thinner width
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='lime', width=1)

    def on_mouse_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_mouse_release(self, event):
        end_x, end_y = event.x, event.y
        # Calculate original coordinates based on the ratios
        orig_x1 = int(self.start_x * self.width_ratio)
        orig_y1 = int(self.start_y * self.height_ratio)
        orig_x2 = int(end_x * self.width_ratio)
        orig_y2 = int(end_y * self.height_ratio)
        bbox = (orig_x1, orig_y1, orig_x2, orig_y2)

        self.cropped_image_path = self.save_selection(bbox)

    def save_selection(self, bbox):
        x1, y1, x2, y2 = bbox
        # Open the original image to ensure quality
        cropped_image = self.original_image.crop(bbox)

        # Save the cropped image in the system's temp directory
        temp_dir = tempfile.gettempdir()
        self.cropped_image_path = os.path.join(temp_dir, "selected_area.png")
        cropped_image.save(self.cropped_image_path)

        os.remove(self.screenshot_path)  # Remove the full screenshot

        self.root.destroy()
        return self.cropped_image_path

if __name__ == "__main__":
    ScreenClipTool()
