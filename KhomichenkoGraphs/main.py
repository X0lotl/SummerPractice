import io
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk


def load_image_to_label(image, window):
    try:
        window['image'].update(data=ImageTk.PhotoImage(image))
    except:
        print('Unable to open image')


def main():
    min_x = 0
    max_x = 0
    number_of_dots = 0

    sg.theme('Purple')

    plt.title('Парабола Нейля')
    plt.grid()

    layout = [

        [sg.Text('Введіть значення парметру a'), sg.InputText(),
         ],
        [sg.Text('Введіть нижню границю функції'), sg.InputText(),
         ],
        [sg.Text('Введіть верхню границю функції'), sg.InputText(),
         ],
        [sg.Text('Введіть кількість точок'), sg.InputText(),
         ],
        [sg.Image(key='image')],
        [sg.Save()],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Парабола Нейля', layout)
    while True:
        event, values = window.read()

        if event in (None, 'Exit', 'Cancel'):
            break
        if event == 'Submit':
            try:
                a = float(values[0])
                min_x = int(values[1])
                max_x = int(values[2])
                number_of_dots = int(values[3])
            except:
                print('Incorrect input')

            x = np.linspace(min_x, max_x, number_of_dots)
            y = a * pow(x, 1.5)

            if y[len(y) - 1] > 0:
                plt.plot(x, y, color='blue')
            else:
                plt.plot(x, y, color='red')

            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)

            load_image_to_label(Image.open(buf), window)

        if event == 'Save':
            plt.savefig('semiCubicalParabola.png')


main()