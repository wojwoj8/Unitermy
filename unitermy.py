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
    # for correct width
    f_canvas = first_canvas.split(";")
    canvas.delete("all")
    width = 18
    x = 60
    # ARC WIDTH
    for element in elements:
        x += width
    w = 20

    # LINE WIDTH
    for el in f_canvas:
        w += width

    print(w)
    # Draw the arc
    canvas.create_arc(
        10, 10, x, 40, start=20, extent=140, outline="black", width=2, style="arc"
    )

    # Draw line
    #
    canvas.create_line(10, 62, w - 10, 62, fill="black")  # solid line under dashes
    canvas.create_text(10, 60, text="|", anchor="w", font=("Helvetica", 20))
    canvas.create_text(w - 10, 60, text="|", anchor="e", font=("Helvetica", 20))

    canvas1_text = canvas.create_text(
        w / 2, 80, text=first_canvas, font=("Helvetica", 12), anchor="center"
    )
    print(canvas.bbox(canvas1_text))


######################################
# if A;
# if alone_elem.index(";") == 1:

#     # Draw the input text
#     canvas.create_text(
#         w - 20,
#         35,
#         text=alone_elem,
#         font=("Helvetica", 12),
#         anchor="center",
#     )

#     ##################################################

#     canvas.create_line(
#         (w - 25) * 3, 37, w, 37, fill="black"
#     )  # solid line under dashes
#     canvas.create_text(10 * 3, 35, text="|", anchor="w", font=("Helvetica", 20))
#     canvas.create_text(
#         (w - 25) * 3, 35, text="|", anchor="e", font=("Helvetica", 20)
#     )

#     canvas.create_text(
#         (w / 2 - 9) * 3,
#         45,
#         text=first_canvas,
#         font=("Helvetica", 12),
#         anchor="center",
#     )
#     # if ;A
# else:
#     # Draw the input text
#     canvas.create_text(
#         w,
#         35,
#         text=alone_elem,
#         font=("Helvetica", 12),
#         anchor="center",
#     )
#     ##################################################

#     canvas.create_line(20, 37, w - 15, 37, fill="black")  # solid line under dashes
#     canvas.create_text(20, 35, text="|", anchor="w", font=("Helvetica", 20))
#     canvas.create_text(w - 15, 35, text="|", anchor="e", font=("Helvetica", 20))

#     canvas.create_text(
#         w / 2, 45, text=first_canvas, font=("Helvetica", 12), anchor="center"
#     )


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

    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    text_width = canvas_width / 2
    text_height = canvas_height / 2

    text = canvas.create_text(
        text_width,
        text_height,
        text=input_text,
        font=("Helvetica", 12),
        anchor="center",
    )
    bbox = canvas.bbox(text)
    canvas.create_line(bbox[0], bbox[1] - 5, bbox[2], bbox[1] - 5)
    canvas.create_line(bbox[0], bbox[1], bbox[0], bbox[1] - 10)
    canvas.create_line(bbox[2], bbox[1], bbox[2], bbox[1] - 10)


def draw_arc_over_elements(elements, input_text, canvas):
    canvas.delete("all")

    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    text_width = canvas_width / 2
    text_height = canvas_height / 2

    text = canvas.create_text(
        text_width,
        text_height,
        text=input_text,
        font=("Helvetica", 12),
        anchor="center",
    )
    bbox = canvas.bbox(text)

    x1, y1, x2, y2 = bbox

    # Calculate the center point of the bounding box
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2

    # Calculate the radius of the circle based on the bounding box dimensions
    radius = (x2 - x1) / 3

    # Calculate the start and end angles for the arc
    start_angle = 20
    end_angle = 160

    # Create the arc using the bounding box dimensions and angles
    canvas.create_arc(
        x1,
        center_y - radius,
        x2,
        center_y + radius,
        start=start_angle,
        extent=end_angle - start_angle,
        outline="black",
        width=2,
        style="arc",
    )

    # canvas.create_arc(
    #      10, 10, x, 40, start=20, extent=140, outline="black", width=2, style="arc"
    #  )
    # Positioning text under the arc


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
