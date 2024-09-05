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


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img


def quit():
    window.destroy()


window = Tk()
window.title("Cats!")
window.geometry('600x520')

mainmanu = Menu(window)
window.config(menu=mainmanu)

filemenu = Menu(mainmanu, tearoff=0)
filemenu.add_command(label="Обновить", command=set_image)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=quit)
mainmanu.add_cascade(label="Файл", menu=filemenu)

label = Label()
label.pack()

url = "https://cataas.com/cat"

set_image()

window.mainloop()
