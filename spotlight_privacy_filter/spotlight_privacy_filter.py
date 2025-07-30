import tkinter as tk
import pyautogui
from screeninfo import get_monitors
import threading
import time
import keyboard
import pystray
from PIL import Image, ImageDraw

# Config
SPOTLIGHT_RADIUS = 300
UPDATE_INTERVAL = 0.01
TOGGLE_HOTKEY = 'ctrl+alt+s'

class PrivacySpotlight:
    def __init__(self):
        self.running = True
        self.visible = True  # For toggle

        monitor = get_monitors()[0]
        self.screen_width = monitor.width
        self.screen_height = monitor.height

        # Create root window (hidden)
        self.root = tk.Tk()
        self.root.withdraw()

        # Create overlay
        self.overlay = tk.Toplevel()
        self.overlay.overrideredirect(True)
        self.overlay.attributes('-topmost', True)
        self.overlay.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.overlay.config(bg='magenta')
        self.overlay.attributes('-transparentcolor', 'magenta')

        # Canvas
        self.canvas = tk.Canvas(self.overlay, width=self.screen_width, height=self.screen_height,
                                bg='magenta', highlightthickness=0)
        self.canvas.pack()

        # Exit Button (small red circle in top-right)
        self.exit_btn = self.canvas.create_oval(
            self.screen_width - 40, 10, self.screen_width - 10, 40,
            fill='red', outline='white'
        )
        self.canvas.tag_bind(self.exit_btn, "<Button-1>", lambda e: self.exit())

        # Bind Esc key
        self.overlay.bind("<Escape>", lambda e: self.exit())

        # Start threads
        threading.Thread(target=self.update_loop, daemon=True).start()
        threading.Thread(target=self.register_hotkey, daemon=True).start()
        threading.Thread(target=self.create_tray_icon, daemon=True).start()

        self.overlay.mainloop()

    def update_loop(self):
        while self.running:
            if self.visible:
                x, y = pyautogui.position()
                self.root.after(0, self.draw_spotlight, x, y)
            time.sleep(UPDATE_INTERVAL)

    def draw_spotlight(self, x, y):
        self.canvas.delete("all")

        # Black overlay
        self.canvas.create_rectangle(0, 0, self.screen_width, self.screen_height, fill='black', outline='black')

        # Spotlight hole (transparent)
        self.canvas.create_oval(
            x - SPOTLIGHT_RADIUS, y - SPOTLIGHT_RADIUS,
            x + SPOTLIGHT_RADIUS, y + SPOTLIGHT_RADIUS,
            fill='magenta', outline='magenta'
        )

        # Red exit button
        self.exit_btn = self.canvas.create_oval(
            self.screen_width - 40, 10, self.screen_width - 10, 40,
            fill='red', outline='white'
        )
        self.canvas.tag_bind(self.exit_btn, "<Button-1>", lambda e: self.exit())

    def register_hotkey(self):
        keyboard.add_hotkey(TOGGLE_HOTKEY, self.toggle_visibility)

    def toggle_visibility(self):
        if self.visible:
            self.overlay.withdraw()
            self.visible = False
        else:
            self.overlay.deiconify()
            self.visible = True

    def create_tray_icon(self):
        icon_img = self.create_icon_image()
        menu = pystray.Menu(
            pystray.MenuItem('Toggle (Ctrl+Alt+S)', lambda: self.toggle_visibility()),
            pystray.MenuItem('Exit', lambda: self.exit())
        )
        self.icon = pystray.Icon("PrivacySpotlight", icon_img, "Privacy Spotlight", menu)
        self.icon.run()

    def create_icon_image(self):
        size = (64, 64)
        img = Image.new("RGB", size, "black")
        draw = ImageDraw.Draw(img)
        draw.ellipse((8, 8, 56, 56), fill="white")
        draw.ellipse((16, 16, 48, 48), fill="black")
        return img

    def exit(self):
        self.running = False
        self.icon.stop()
        self.overlay.destroy()

if __name__ == "__main__":
    PrivacySpotlight()
