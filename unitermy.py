import tkinter as tk


def draw_input():
    input_text = entry.get()
    elements = input_text.split(";")
    draw_elements(elements, input_text)


def draw_elements(elements, input_text):
    canvas.delete("all")
    width = 18
    x = 20
    for element in elements:
        x += width

    canvas.create_line(10, 62, x - 10, 62, fill="black")  # solid line under dashes
    canvas.create_text(10, 60, text="|", anchor="w", font=("Helvetica", 20))
    canvas.create_text(x - 10, 60, text="|", anchor="e", font=("Helvetica", 20))

    canvas.create_text(
        x / 2, 80, text=input_text, font=("Helvetica", 12), anchor="center"
    )


root = tk.Tk()
root.title("Drawing Program")

label = tk.Label(root, text="Enter semicolon-separated input:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Draw", command=draw_input)
button.pack()

canvas = tk.Canvas(root, width=300, height=120)
canvas.pack()

root.mainloop()
