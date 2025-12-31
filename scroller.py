"""
How to Run It

Open Terminal (search for it in Spotlight).
Navigate to your script's folder: cd /path/to/your/folder (e.g., cd ~/Desktop).
Run: python3 ticker.py.

If Python isn't installed, download it from python.org (it's free and quick).
The window will open with the scrolling text. Close it with Cmd+Q or the window's close button.



Customizations

Direction: To scroll left-to-right (text enters from left), change x_position -= 3 to x_position += 3, and reset with if x_position > window_width: x_position = -text_width.
Speed: Change 3 in x_position -= 3 (pixels per frame).
Text/Style: Edit scroll_text, font, colors in the Label.
Fullscreen: Set root.attributes('-fullscreen', True) and remove root.geometry.
Quit Key: Add root.bind('<Escape>', lambda e: root.quit()) after root.mainloop() for Esc to exit.

This is lightweight, runs smoothly, and uses no external libraries beyond what's built into Python.
Step 2: Save as an Executable (.app)
To bundle this into a standalone macOS app (no Python needed to run), use PyInstaller. It's the simplest tool for this on iMac.
Install PyInstaller

In Terminal: pip3 install pyinstaller (installs via Python's package manager; takes ~1 minute).

Build the Executable

In Terminal, navigate to your ticker.py folder: cd /path/to/your/folder.
Run:
text

"""

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Text Ticker")
root.configure(bg='#87CEEB')
root.attributes('-fullscreen', False)  # Set to True for fullscreen if desired
root.geometry("800x100")  # Window size: width x height (adjust as needed)

# Read scrolling text from file (create ticker_text.txt in the same folder)
try:
    with open('/Users/lightstar/python/ticker_text.txt', 'r') as f:
        scroll_text = f.read().strip() + " "  # Add space for smooth looping
    if not scroll_text:
        scroll_text = "Default message: Edit ticker_text.txt to customize."
except FileNotFoundError:
    scroll_text = "Error: ticker_text.txt not found. Create it in the same folder."

# Create the label for the text
label = tk.Label(root, text=scroll_text, font=("Arial", 16, "bold"), bg="#87CEEB", fg="yellow", anchor="w")
label.pack(expand=True)

# Get initial dimensions
root.update()  # Force update to get accurate widths
window_width = root.winfo_width()
text_width = label.winfo_reqwidth()

# If text is shorter than window, repeat it to make it scrollable
if text_width < window_width:
    repeats = (window_width // len(scroll_text)) + 2
    scroll_text *= repeats
    label.config(text=scroll_text)
    root.update()
    text_width = label.winfo_reqwidth()

# Starting position: text starts off-screen to the left
x_position = -text_width

def scroll_text():
    global x_position
    x_position += 6  # Positive for left-to-right scroll; adjust speed here
    
    # Reset position when text has fully scrolled off right
    if x_position > window_width:
        x_position = -text_width
    
    # Reposition the label
    label.place(x=x_position, y=30)  # y=30 centers vertically; adjust if needed
    
    # Schedule next frame (20ms for smooth ~50 FPS)
    root.after(20, scroll_text)

# Start the scrolling
scroll_text()

# Run the app
root.mainloop()