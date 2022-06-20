import io
import math

import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from PlotData import PlotData


def semi_cubical_parabola(a, x):
    return a * pow(x, 1.5)


def half_of_16_task(window):
    x = []
    y = []

    i = np.linspace(-200, 200, 1050)

    for i in i:
        r = math.sin(0.99 * math.pi * i)
        x.append(r * math.cos(math.pi * i))
        y.append(r * math.sin(math.pi * i))

    plt.title('R(a) = sin(0.99a)')

    plt.plot(x, y, linewidth=0.1)

    load_image_to_label(Image.open(save_figure_to_image()), window)


def parce_input_data(values):
    try:
        a = float(values[0])
        min_x = int(values[1])
        max_x = int(values[2])
        number_of_dots = int(values[3])
    except:
        print('Incorrect input data')
        return PlotData(0, 0, 1, 1)

    if number_of_dots > 0:
        if min_x > max_x:
            min_x, max_x = max_x, min_x

        if min_x >= 0:
            plot_data = PlotData(a, min_x, max_x, number_of_dots)
            return plot_data

    print('Incorrect input data')
    return PlotData(0, 0, 1, 1)


def load_image_to_label(image, window):
    try:
        window['image'].update(data=ImageTk.PhotoImage(image))
    except:
        print('Unable to open image')


def configurate_plt():
    plt.title('Парабола Нейля')
    plt.grid()


def add_graph_to_plot(values, window):
    plot_data = parce_input_data(values)

    x = np.linspace(plot_data.get_min_x(), plot_data.get_max_x(), plot_data.get_number_of_dots())
    y = semi_cubical_parabola(plot_data.get_a(), x)
    zero = np.linspace(0, 0, plot_data.get_number_of_dots())

    if y[len(y) - 1] > 0:
        plt.plot(x, y, color='blue')
    else:
        plt.plot(x, y, color='red')

    plt.plot(x, zero, color='black')
    plt.plot(zero, y, color='black')
    plt.plot([-1, 0], [0, 0], color='black')
    plt.plot([0, 0], [-2, 0], color='black')

    load_image_to_label(Image.open(save_figure_to_image()), window)


def generate_layout():
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
        [sg.Save(), sg.Save('Task16')],
        [sg.Submit('Add'), sg.Cancel('Clear')]
    ]
    return layout


def save_figure_to_image():
    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)

    return image


def main():
    sg.theme('Purple')
    layout = generate_layout()
    window = sg.Window('Khomichenko Graphs', layout)

    configurate_plt()

    while True:
        event, values = window.read()

        if event in (None, 'Exit'):
            break

        if event == 'Clear':
            plt.clf()
            configurate_plt()

            load_image_to_label(Image.open(save_figure_to_image()), window)

        if event == 'Add':
            add_graph_to_plot(values, window)

        if event == 'Save':
            plt.savefig('semiCubicalParabola.png')

        if event == 'Task16':
            plt.clf()
            configurate_plt()

            half_of_16_task(window)


main()
