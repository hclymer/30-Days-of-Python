import random
import PySimpleGUI as sg 

sg.theme('DarkBlue17')

#import PySimpleGUI as sg
number = random.randint(1,10)
number_of_guesses = 0

sg.ChangeLookAndFeel('DarkBlue17')

form = sg.FlexForm('Number Guessing Game', default_element_size=(40, 1))


layout = [
            [sg.Text('Number Guessing Game', size=(30, 1), font=("Helvetica", 25))],
    [sg.Text('Guessed Number:'), sg.InputText('',size=(5, 3), key='guessed_num')],
    [sg.Submit(), sg.Exit()]
    ]

window = sg.Window('ORIGINAL').Layout(layout)
while number_of_guesses < 5:             # Event Loop
    event, values = window.Read()
    guess = int()
    number_of_guesses += 1
    guessed_num = int(values["guessed_num"])
    if event in (None, 'Exit'):
        break
    if guessed_num < number:
        sg.Popup("Your guess is too low")
    if guessed_num > number:
        sg.Popup("Your guess is too high")
    if guessed_num == number:
        break
window.Close()

if guessed_num == number:
    sg.Popup('You guessed the number in ' + str(number_of_guesses) + " tries!")
else:
    print('You did not guess the number, The number was ' + str(number))