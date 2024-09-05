from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
# import certifi


def load_image(url):
    try:
        response = requests.get(url, timeout=5) # timeout=5 - увеличили время ожидания
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def open_new_window():
    img = load_image(url)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img


def quit():
    window.destroy()


window = Tk()
window.title("Cats!")
window.geometry('600x520')

mainmanu = Menu(window)
window.config(menu=mainmanu)

filemenu = Menu(mainmanu, tearoff=0)
filemenu.add_command(label="Загрузить фото", command=open_new_window)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=quit)
mainmanu.add_cascade(label="Файл", menu=filemenu)


url = "https://cataas.com/cat"

set_image()

window.mainloop()
