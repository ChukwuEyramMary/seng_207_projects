# Importing libraries
import qrcode
import PySimpleGUI as sg

# layout of App
layout = [
    [
        sg.Input(default_text="Enter URL", key='URL'),
    ],
    [
        sg.Button(button_text="Create", key="Create")
    ],
    [
        sg.Image(source='', key='Scan')
    ]
]
# Window
myApp = sg.Window(title='qrcode generator',
                  layout=layout,
                  margins=(200, 100))
# Create an event loop

while True:
    event, values = myApp.read()
    print(event, values)
    if event == "Create":
        print(values['URL'])
        img = qrcode.make(values['URL'])
        img.save("QRcode.png")
        myApp['Scan'].update(source='QRcode.png')
    if event == sg.WIN_CLOSED:
        break
