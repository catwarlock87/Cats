from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
from  tkinter import ttk
# import certifi


allowed_tegs = ['sleep', 'jump',
                'fight', 'black',
                'white', 'orange',
                'siamese', 'cute']


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
    teg = teg_combobox.get()
    url_teg = f"https://cataas.com/cat/{teg}" if teg else "https://cataas.com/cat"

    img = load_image(url_teg)

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

label_teg = Label(text="Выбери тег")
label_teg.pack()

teg_combobox = ttk.Combobox(values=allowed_tegs)
teg_combobox.pack()

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()

window.mainloop()
