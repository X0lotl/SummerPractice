import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
import shutil

PATH_TO_TEMPORARY_PNG = 'temporaryFiles/test.png'


def load_image(path, window):
    try:
        image = Image.open(path)
        image.thumbnail((640, 480))
        photo_img = ImageTk.PhotoImage(image)
        window['image'].update(data=photo_img)
    except:
        print(f'Unable to open {path}')


def main():
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
    while True:  # The Event Loop
        event, values = window.read()

        if event in (None, 'Exit', 'Cancel'):
            break
        if event == 'Submit':
            a = int(values[0])
            minX = int(values[1])
            maxX = int(values[2])
            numberOfDots = int(values[3])

            x = np.linspace(minX, maxX, numberOfDots)
            y = a * pow(x, 1.5)

            plt.grid()
            plt.title('Парабола Нейля')
            plt.plot(x, y)

            plt.savefig(PATH_TO_TEMPORARY_PNG)
            load_image(PATH_TO_TEMPORARY_PNG, window)
        if event == 'Save':
            shutil.copy(PATH_TO_TEMPORARY_PNG, 'semicubicalParabola.png')


main()