from tkinter import *
from PIL import ImageTk, Image
def forward(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()
    label = Label(image=List_images[img_no - 1], width=200, height=300)
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text=">>",
                        command=lambda: forward(img_no + 1))
    if img_no == 2:
        button_forward = Button(root, text=">>",
                                state=DISABLED)
    button_back = Button(root, text="<<", command=lambda: back(img_no - 1))
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)


def back(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()
    label = Label(image=List_images[img_no - 1], width=200, height=300)
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text=">>",
                            command=lambda: forward(img_no + 1))
    button_back = Button(root, text="<<",
                         command=lambda: back(img_no - 1))
    print(img_no)
    if img_no == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)


root = Tk()
root.title("Photo Viewer")
root.geometry("700x700")


image_no_2 = ImageTk.PhotoImage(Image.open("test2.png"))
image_no_1 = ImageTk.PhotoImage(Image.open("test1.png"))
List_images = [image_no_1, image_no_2]
label = Label(image=image_no_1,width=200, height=300)
label.grid(row=1, column=0, columnspan=3)

button_back = Button(root, text='<<', background='white', foreground='blue',command = back,
                     state=DISABLED)
button_forward = Button(root, text='>>', background='white', foreground='blue',command = lambda: forward(1))
button_exit = Button(root, text='Exit Program', background='white', foreground='blue', command=root.quit)
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)
root.iconbitmap("test_axe.ico")
root.mainloop()