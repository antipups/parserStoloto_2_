import threading
from time import sleep
from tkinter import *
from main import get_static, parse_every_page, every_parsing


autoupdate = True


def timer():
    print('sexix')
    while autoupdate:
        every_parsing()
        sleep(60)


class MyApp(Tk):
    def __init__(self):
        super().__init__()
        threading.Thread(target=timer, daemon=True).start()
        self.create_widgets()

    def create_widgets(self):
        self.ls_of_buttons = []
        btn = Button(text='Перепарсить',
                     font=('Ubuntu', 15))
        label = Label(text='', font=('Ubuntu', 15))

        def parse(event):
            global autoupdate
            autoupdate = False
            label['text'] = '0%'
            threading.Thread(target=parse_every_page, args=(5000, label, self.ls_of_buttons)).start()
            self.disable_all()

        btn.bind('<Button-1>', parse)
        btn.grid(row=0, columnspan=4)
        self.ls_of_buttons.append(btn)
        label.grid(row=2, columnspan=4)

        for index, btn_text in enumerate(('500', '1000', '2500', '5000')):
            btn = Button(text=btn_text, font=('Ubuntu', 15))

            def on_press(event):
                label['text'] = 'Обработка начата.'
                threading.Thread(target=get_static, args=(int(event.widget.cget('text')), label, self.ls_of_buttons)).start()
                self.disable_all()

            btn.bind('<Button-1>', on_press)
            btn.grid(row=1, column=index)
            self.ls_of_buttons.append(btn)

    def disable_all(self):
        for btn in self.ls_of_buttons:
            btn['state'] = 'disabled'


if __name__ == '__main__':
    MyApp().mainloop()
