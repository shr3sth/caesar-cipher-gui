import tkinter as tk


def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char

    return result


def update_output(event=None):
    text = text_input.get("1.0", "end-1c")
    shift = shift_slider.get()

    result = caesar_cipher(text, shift)

    output_text.config(state="normal")

    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)

    output_text.config(state="disabled")


def copy_output():
    text = output_text.get("1.0", "end-1c")

    root.clipboard_clear()

    root.clipboard_append(text)

    root.update()


root = tk.Tk()

root.title("Caesar Cipher Explorer")
root.geometry("700x600")
root.resizable(False, False)

# Dark Theme
root.configure(bg="#1e1e1e")

# Input Label
text_label = tk.Label(
    root,
    text="Enter Text:",
    bg="#1e1e1e",
    fg="white"
)
text_label.pack(pady=(10, 5))

# Input Text Box
text_input = tk.Text(
    root,
    width=60,
    height=10,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
text_input.pack(pady=5)

text_input.bind("<KeyRelease>", update_output)

# Slider
shift_slider = tk.Scale(
    root,
    from_=-25,
    to=25,
    orient="horizontal",
    label="Shift Value",
    length=500,
    bg="#1e1e1e",
    fg="white",
    highlightthickness=0
)

shift_slider.pack(pady=10)
shift_slider.set(0)

shift_slider.config(
    command=lambda value: update_output()
)

# Output Label
output_label = tk.Label(
    root,
    text="Output:",
    bg="#1e1e1e",
    fg="white"
)
output_label.pack(pady=(10, 5))

# Output Text Box
output_text = tk.Text(
    root,
    width=60,
    height=10,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

output_text.pack(pady=5)

copy_button = tk.Button(
    root,
    text="📋 Copy Output",
    command=copy_output,
    bg="#3a3a3a",
    fg="white",
    activebackground="#505050",
    activeforeground="white"
)

copy_button.pack(pady=10)


# Make output read-only
output_text.config(state="disabled")

root.mainloop()