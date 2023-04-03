# Importing libraries
import pyttsx3
import PySimpleGUI as sg

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Layout of App
layout = [
    [
        sg.Input(default_text="Enter text here", key='Text'),
        sg.Button(button_text="Speak", key="Speak")
    ],
    [
        sg.Text(text='Select Voice Type:'),
        sg.Radio(group_id='gen', text='Male', default=True, key='male'),
        sg.Radio(group_id='gen', text='Female', key="female")
    ]
]

# Window
myApp = sg.Window(title='Text To Speech App',
                  layout=layout,
                  margins=(200, 100))


# Create an event loop
while True:
    event, values = myApp.read()
    print(event, values)
    if event == "Speak":
        if values['female']:
            engine.setProperty('voice', voices[1].id)
        if values['male']:
            engine.setProperty('voice', voices[0].id)
        engine.say(values['Text'])
    engine.runAndWait()
    # End program if user closes window or
    if event == sg.WIN_CLOSED:
        break

# for voice in voices:
#
#     engine.say('The quick brown fox jumped over the lazy dog.')
#     print(voice)
# engine.runAndWait()
# print(voices[1])


myApp.close()
