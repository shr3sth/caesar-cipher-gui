import tkinter as tk


# The main cipher function that takes in the text and shift value!
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            # %26 ensures it wraps around the alphabet i.e. 25 unique/non-redundant shifts!!!! hell yeah!
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char

    return result


def update_output(event=None):  # Thi one to update the output in real-time!
    text = text_input.get("1.0", "end-1c")
    shift = shift_slider.get()

    result = caesar_cipher(text, shift)

    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", result)
    output_text.config(state="disabled")


def copy_output():  # Copies the output to clipboard!
    text = output_text.get("1.0", "end-1c")

    root.clipboard_clear()  # clear the clipboard
    root.clipboard_append(text)
    root.update()


def clear_all():  # Clears the input and output fields and resets the shift slider!
    text_input.delete("1.0", "end")
    shift_slider.set(0)


root = tk.Tk()  # start the GUI

root.title("Super Cool Cipher Tool")
root.geometry("700x650")  # size of the window
root.resizable(False, False)
root.configure(bg="#1e1e1e")  # black black!

text_label = tk.Label(
    root,
    text="Enter Text:",
    bg="#1e1e1e",
    fg="white"
)
text_label.pack(pady=(10, 5))

text_input = tk.Text(   # Input field
    root,
    width=60,
    height=10,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
text_input.pack(pady=5)
text_input.bind("<KeyRelease>", update_output)

shift_slider = tk.Scale(  # Shift slider
    root,
    from_=-25,
    to=25,
    orient="horizontal",
    label="Shift Value",
    length=500,
    bg="#1e1e1e",
    fg="white",
    highlightthickness=0,
    command=update_output
)
shift_slider.pack(pady=10)
shift_slider.set(0)

output_label = tk.Label(
    root,
    text="Output:",
    bg="#1e1e1e",
    fg="white"
)
output_label.pack(pady=(10, 5))

output_text = tk.Text(  # Output Field
    root,
    width=60,
    height=10,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
output_text.pack(pady=5)
output_text.config(state="disabled")

button_frame = tk.Frame(   # This one to keep the buttons together rather than one below another
    root,
    bg="#1e1e1e"
)

button_frame.pack(pady=10)

copy_button = tk.Button(         # copy button
    button_frame,
    text="📋 Copy Output",
    command=copy_output,
    bg="#3a3a3a",
    fg="white",
    activebackground="#505050",
    activeforeground="white"
)

copy_button.pack(side="left", padx=10)

clear_button = tk.Button(       # clear button!
    button_frame,
    text="🗑 Clear",
    command=clear_all,
    bg="#3a3a3a",
    fg="white",
    activebackground="#505050",
    activeforeground="white"
)

clear_button.pack(side="left", padx=10)

root.mainloop()  # keeps the GUI alive! and responsive!
