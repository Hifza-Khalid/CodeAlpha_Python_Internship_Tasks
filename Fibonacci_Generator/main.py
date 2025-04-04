import tkinter as tk
from tkinter import messagebox, filedialog
import pyperclip
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

# Global variables
fibonacci_series = []
dark_mode = True  # Default to dark mode

def generate_fibonacci():
    """Generate Fibonacci sequence and display it."""
    try:
        n = int(entry.get().strip())
        if n < 0:
            output_text.config(state=tk.NORMAL)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "Enter a positive integer")
            output_text.config(state=tk.DISABLED)
            return

        global fibonacci_series
        fibonacci_series = [0, 1][:max(1, n)]
        for _ in range(n - 2):
            fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])

        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, " → ".join(map(str, fibonacci_series)))
        output_text.config(state=tk.DISABLED)

    except ValueError:
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Invalid input! Please enter a number.")
        output_text.config(state=tk.DISABLED)

def copy_to_clipboard():
    """Copy Fibonacci sequence to clipboard."""
    if fibonacci_series:
        pyperclip.copy(" → ".join(map(str, fibonacci_series)))
        messagebox.showinfo("Copied", "Fibonacci sequence copied to clipboard!")

def save_to_file():
    """Save Fibonacci sequence to a text file."""
    if fibonacci_series:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("Fibonacci Sequence:\n")
                file.write(" → ".join(map(str, fibonacci_series)))
            messagebox.showinfo("Saved", f"Fibonacci sequence saved to {file_path}")

def plot_fibonacci():
    """Plot Fibonacci sequence growth."""
    if fibonacci_series:
        plt.figure(figsize=(8, 5), facecolor=("white" if not dark_mode else "#0A192F"))
        plt.plot(fibonacci_series, marker='o', linestyle='-', color='#007BFF', markersize=8, linewidth=2)
        plt.title("Fibonacci Sequence Growth", fontsize=14, color=("black" if not dark_mode else "white"))
        plt.xlabel("Index", fontsize=12, color=("black" if not dark_mode else "white"))
        plt.ylabel("Value", fontsize=12, color=("black" if not dark_mode else "white"))
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.gca().set_facecolor("white" if not dark_mode else "#0A192F")
        plt.xticks(color=("black" if not dark_mode else "white"))
        plt.yticks(color=("black" if not dark_mode else "white"))
        plt.show()

def toggle_theme():
    """Toggle between light and dark mode."""
    global dark_mode
    dark_mode = not dark_mode
    
    if dark_mode:
        root.configure(bg="#0A192F")
        label.config(bg="#0A192F", fg="#4CA1AF")
        entry.config(bg="#112D4E", fg="white", insertbackground="white")
        output_text.config(bg="#112D4E", fg="white")
        button_frame.config(bg="#0A192F")
        theme_button.config(image=moon_img, bg="#0A192F")
        
        for widget in button_frame.winfo_children():
            widget.config(bg="#1B4965", fg="white")
    else:
        root.configure(bg="white")
        label.config(bg="white", fg="black")
        entry.config(bg="white", fg="black", insertbackground="black")
        output_text.config(bg="white", fg="black")
        button_frame.config(bg="white")
        theme_button.config(image=sun_img, bg="white")
        
        for widget in button_frame.winfo_children():
            widget.config(bg="#E0E0E0", fg="black")

# Create the main window
root = tk.Tk()
root.title("Fibonacci Generator")
root.geometry("500x550")
root.configure(bg="#0A192F")  # Default dark mode
root.resizable(False, False)

# Load images
def load_image(path, size):
    img = Image.open(path).resize((size, size))
    return ImageTk.PhotoImage(img)

img_size = 30
sun_img = load_image("sun.png", img_size)
moon_img = load_image("moon.png", img_size)

theme_button = tk.Button(root, image=moon_img, command=toggle_theme, borderwidth=0, bg="#0A192F", highlightthickness=0)
theme_button.place(relx=0.95, rely=0.05, anchor="ne")

# UI Elements
container = tk.Frame(root, bg="#0A192F")
container.pack(expand=True)

label = tk.Label(container, text="Fibonacci Generator", font=("Arial", 16, "bold"), bg="#0A192F", fg="#4CA1AF")
label.pack(pady=10)

entry = tk.Entry(container, width=10, font=("Arial", 14), bg="#112D4E", fg="white", insertbackground="white")
entry.pack(pady=5)

generate_button = tk.Button(container, text="Generate", command=generate_fibonacci, bg="#1B4965", fg="white", font=("Arial", 12))
generate_button.pack(pady=10)

output_text = tk.Text(container, height=4, width=50, font=("Arial", 12), state=tk.DISABLED, wrap=tk.WORD, bg="#112D4E", fg="white")
output_text.pack(pady=10)

button_frame = tk.Frame(container, bg="#0A192F")
button_frame.pack()

buttons = [
    ("Copy", copy_to_clipboard),
    ("Save", save_to_file),
    ("Plot", plot_fibonacci)
]

for text, command in buttons:
    btn = tk.Button(button_frame, text=text, command=command, bg="#1B4965", fg="white", font=("Arial", 12))
    btn.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
