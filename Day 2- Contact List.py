import json

def save_contact(contact: dict, filename: str):
    with open(filename, "a") as f:
        json.dump(contact, f)



import random
import PySimpleGUI as sg

sg.theme('DarkBlue17')

#import PySimpleGUI as sg

sg.ChangeLookAndFeel('DarkBlue17')

form = sg.FlexForm('Contact Creator', default_element_size=(40, 1))


layout = [
            [sg.Text('Contact Creater', size=(30, 1), font=("Helvetica", 25))],
    [sg.Text('First Name'), sg.InputText('',size=(10, 10),key='first-name'), sg.Text('Last Name'), sg.InputText('',size=(10, 10), key='last-name')],
    [sg.Text('Email'), sg.InputText('',size=(10, 10),key='email'), sg.Text('Phone'), sg.InputText('',size=(10, 10), key='phone')],
    [sg.Submit(), sg.Cancel()]
    ]
event, values = form.Layout(layout).Read()
first_name= str(values['first-name'])
last_name = str(values['last-name'])
email = str(values['email'])
phone = str(values['phone'])

contact_dict= {
    "first_name":first_name,
    'last_name': last_name,
    'email':email,
    "phone": phone
}

save_contact(contact_dict, "contacts.json")

sg.Popup( 'contact saved ')       