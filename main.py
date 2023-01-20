from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd


window = Tk()
first_window = Frame(window)
second_window = Frame(window)


def increase_text():
    input.place(x=0, y=150)
    submit_text.place(x=0, y=200)


def more_text():
    canvas.delete("label")
    text = input.get()
    canvas.create_text(300, 300, text=text, fill="#FFFFFF", font=("Comic Sans MS", 20, "bold"), tags='label')


def open_image():
    global canvas, img, first_image, new_img
    file_name = fd.askopenfilename()
    new_img = ImageTk.PhotoImage(Image.open(file_name))
    canvas.itemconfig(first_image, image=new_img)


def clear_all():
    global new_img
    canvas.delete('label')
    new_img = ImageTk.PhotoImage(Image.open("welcome.jfif"))
    canvas.itemconfig(first_image, image=new_img)
    submit_text.place_forget()
    input.place_forget()


def close_app():
    window.destroy()


def change_to_first_window():
    input.place_forget()
    submit_text.place_forget()
    back.place_forget()
    add_text.place_forget()
    add_images.place(x=200, y=0)
    next_step.place(x=450, y=0)
    close_app.place(x=0, y=0)
    first_window.pack(fill='both', expand=1)
    second_window.pack_forget()


def change_to_second_window():
    add_images.place_forget()
    back.place(x=75, y=0)
    add_text.place(x=175, y=0)
    next_step.place_forget()
    close_app.place(x=0, y=0)
    second_window.pack(fill='both', expand=1)
    first_window.pack_forget()


window.minsize(width=650, height=500)
window.title("Watermarking App")

clear = Button(text="Clear", command=clear_all)
clear.place(x=400, y=0)

close_app = Button(text="Close App", command=close_app)
close_app.place(x=0, y=0)

next_step = Button(window, text="Next Step", command=change_to_second_window)
next_step.place(x=450, y=0)

add_images = Button(text="Add Images", command=open_image)
add_images.place(x=200, y=0)

back = Button(window, text="<Back", command=change_to_first_window)
canvas = Canvas(window, width=400, height=350)
canvas.place(x=125, y=90)

input = Entry()

add_text = Button(text="Add Text", command=increase_text)


submit_text = Button(text="Add text", command=more_text)

text = input.get()
watermark = Label(text=f"{text}", font=("Comic Sans MS", 20, "bold"))


img = ImageTk.PhotoImage(Image.open("html.jpg"))
first_image = canvas.create_image(100, 100, image=img, tags='img1')

window.mainloop()

