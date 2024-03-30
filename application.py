import os
import tkinter

from mainWindow import MainWindow

application = tkinter.Tk()
path = os.path.join(os.path.dirname(__file__), "images/")

icon = path + "interest.ico"

application.iconbitmap(icon)
application.title("Interest")
window = MainWindow(application)
application.protocol("WM_DELETE_WINDOW", window.quit)
application.mainloop()