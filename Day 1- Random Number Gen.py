import PySimpleGUI as sg 
import random
import pandas as pd


# def randomnum(range):
#     range = int(range)
#     return random.randrange(1,range)


# sg.theme("DarkAmber")

# layout = [   
#     [sg.Text("Select a range for a random number")],
#     [sg.Spin([i for i in range(1,100)], initial_value=10, k='-SPIN-'), sg.Text('Spin')],
#     [sg.Button("Done")]
#           ]


# window = sg.Window("Chore Chart", layout)

# while True:             # Event Loop
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     if event == "Done":
#         range1 = window['-SPIN-']
#         print(type(range1))
#         range2 = int(range1) # call the "Callback" function


import random
import PySimpleGUI as sg

sg.theme('DarkBlue17')

#import PySimpleGUI as sg

sg.ChangeLookAndFeel('DarkBlue17')

form = sg.FlexForm('Lucky RandomNumbers', default_element_size=(40, 1))


layout = [
            [sg.Text('Lucky Number Generator', size=(30, 1), font=("Helvetica", 25))],
    [sg.Text('Enter low value'), sg.InputText('',size=(5, 3),key='low_end'), sg.Text('Enter high value'), sg.InputText('',size=(5, 3), key='high_end')],
    [sg.Submit(), sg.Cancel()]
    ]
event, values = form.Layout(layout).Read()
randomlist = random.sample(range(int(values['low_end']), int(values['high_end'])), 5)

sg.Popup(randomlist, ' ')