import tkinter as tk


def draw_input1():
    input_text = entry1.get()
    elements = input_text.split(";")
    draw_elements(elements, input_text, canvas1)


def draw_input2():
    input_text = entry2.get()
    elements = input_text.split(";")
    draw_arc_over_elements(elements, input_text, canvas2)


def draw_elements(elements, input_text, canvas):
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


def draw_arc_over_elements(elements, input_text, canvas):
    canvas.delete("all")
    width = 18
    x = 20
    for element in elements:
        x += width

    canvas.create_arc(
        10, 10, x, 40, start=20, extent=140, outline="black", width=2, style="arc"
    )
    canvas.create_text(
        (x + 5) / 2, 30, text=input_text, font=("Helvetica", 12), anchor="center"
    )  # Positioning text under the arc


root = tk.Tk()
root.title("Drawing Program")

# First Input Field
label1 = tk.Label(root, text="Enter semicolon-separated input for canvas 1:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

button1 = tk.Button(root, text="Draw Canvas 1", command=draw_input1)
button1.pack()

canvas1 = tk.Canvas(root, width=300, height=120)
canvas1.pack()

# Second Input Field
label2 = tk.Label(root, text="Enter semicolon-separated input for canvas 2:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button2 = tk.Button(root, text="Draw Arc Over Elements", command=draw_input2)
button2.pack()

canvas2 = tk.Canvas(root, width=300, height=120)
canvas2.pack()

root.mainloop()
