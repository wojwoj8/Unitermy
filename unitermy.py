import tkinter as tk


def draw_input1():
    input_text = entry1.get()
    elements = input_text.split(";")
    draw_elements(elements, input_text, canvas1)


def draw_input2():
    input_text = entry2.get()
    elements = input_text.split(";")
    draw_arc_over_elements(elements, input_text, canvas2)
    create_dropdown(elements)


def create_dropdown(elements):
    dropdown_label.config(text="Choose an element:")
    dropdown_menu["menu"].delete(0, "end")  # Clear previous options
    for element in elements:
        dropdown_menu["menu"].add_command(
            label=element, command=lambda e=element: set_selected_element(e)
        )


def draw_canvas3(
    elements, input_text, replaced_text, first_canvas, canvas, selected_element=None
):
    alone_elem = replaced_text.replace(selected_element, "")
    canvas.delete("all")
    width = 18
    x = 50
    w = 25

    for element in elements:
        x += width

    for elem in first_canvas:
        w += width
    # Draw the arc
    canvas.create_arc(
        10, 10, x, 40, start=20, extent=140, outline="black", width=2, style="arc"
    )

    # # Draw the line under the arc
    # canvas.create_line(10, 62, x - 10, 62, fill="black")  # solid line under dashes
    # # Draw the "|" symbols at the ends of the line
    # canvas.create_text(10, 60, text="|", anchor="w", font=("Helvetica", 20))
    # canvas.create_text(x - 10, 60, text="|", anchor="e", font=("Helvetica", 20))

    # Draw the input text
    canvas.create_text(
        (x + 5) / 2, 30, text=alone_elem, font=("Helvetica", 12), anchor="center"
    )

    if selected_element is not None:
        # Draw the selected element text under the arc
        canvas.create_text(
            w / 2 - 15, 80, text=first_canvas, font=("Helvetica", 12), anchor="center"
        )
        # Draw the line under the selected element (shorter than the arc)
        canvas.create_line(
            10, 62, w / 2, 62, fill="black"
        )  # shorter line under the arc
        # Draw the "|" symbols at the ends of the line
        canvas.create_text(10, 60, text="|", anchor="w", font=("Helvetica", 20))
        canvas.create_text(w / 2, 60, text="|", anchor="e", font=("Helvetica", 20))


def replace_element():
    input_text = entry2.get()
    first_canvas = entry1.get()
    replaced_text = input_text.replace(selected_element.get(), entry1.get())
    elements = replaced_text.split(";")
    draw_canvas3(
        elements,
        replaced_text,
        input_text,
        first_canvas,
        canvas3,
        selected_element=selected_element.get(),
    )


# Modify the set_selected_element function to call replace_element without arguments
def set_selected_element(element):
    selected_element.set(element)
    replace_element()


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

# Dropdown menu for selecting elements
selected_element = tk.StringVar()
dropdown_label = tk.Label(root, text="")
dropdown_label.pack()
# In the root.mainloop() part, change the line that binds the selected element to the OptionMenu:
dropdown_menu = tk.OptionMenu(root, selected_element, "", command=set_selected_element)
dropdown_menu.pack()

# Canvas to show replaced element from canvas2
canvas3 = tk.Canvas(root, width=300, height=120)
canvas3.pack()

root.mainloop()
