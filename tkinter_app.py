import tkinter as tk

def on_click():
    print("Button clicked in Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Application")
root.geometry("300x200")

# Create a button and attach the click event
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()