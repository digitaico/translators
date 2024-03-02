# https://www.geeksforgeeks.org/real-time-translation-app-using-python/
# https://www.codewithfaraz.com/python/20/creating-a-user-friendly-language-converter-in-python
# pip install googletrans==4.0.0rc1 
# https://py-googletrans.readthedocs.io/en/latest/
# mejor version; https://towardsdev.com/language-translator-using-googletrans-python-2b6489f3df24

from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry("1100x320")
root.resizable(False, False)
root["bg"] = "salmon"
root.title("Real-Time Translator")

Label(root, text="Digitai Language Translator", font="Arial 20 bold").pack()
Label(root, text="Ingrese Texto", font="arial 13 bold", bg="white smoke").place(
    x=165, y=90
)

Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)

Label(root, text="Salida", font="arial 13 bold", bg="white smoke").place(x=780, y=90)
Output_text = Text(root, font="arial 10", height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)

language = list(LANGUAGES.values())
dest_lang= ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=130,y=180)
dest_lang.set('Seleccione Lenguaje')


def Translate():
    try:
        translator = Translator()
        translation = translator.translate(Input_text.get(), dest=dest_lang.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END, translation.text)
    except Exception as e:
        print(f"Error de Traduccion: {e}")

trans_btn = Button(root, text='Traducir', font='arial 12 bold', pady=5, command=Translate, bg='orange', activebackground=
                   'green')
trans_btn.place(x=445, y=180)

root.mainloop()

