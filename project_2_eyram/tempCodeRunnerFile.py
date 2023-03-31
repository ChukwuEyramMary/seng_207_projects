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
        # if the female is true :
        engine.say(values['Text'])
    engine.runAndWait()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break