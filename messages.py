import json, os, random, time
import PySimpleGUI as sg

dir = os.path.dirname(os.path.realpath(__file__))

def randomColor():
    letters = '0123456789ABCDEF'
    color = '#'
    for _ in range(6):
        color += letters[int(random.random() * 16)]
    return color

def showMsg(msg, font="Quicksand 50 bold", color="white", bgcolor="black", duration_seconds=5):
    if color == 'random': color = randomColor()
    if bgcolor == 'random': bgcolor = randomColor()
    #layout = [  [sg.Text(msg, font=font, text_color=color, background_color=bgcolor )] ]
    #sg.Window(header, layout, background_color=bgcolor, text_justification="center",
    #keep_on_top=True, grab_anywhere=True, element_justification="center").read() 

    sg.PopupNoButtons(msg,
            background_color = bgcolor,
            text_color = color,
            auto_close = True,
            auto_close_duration = duration_seconds,
            font = font,
            grab_anywhere = True,
            keep_on_top = True,
            modal = True,
            no_titlebar = True
    )

curr_idx = -1
while True:
    dir = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(os.path.join(dir, 'my_configuration.json')): config = json.load(open(os.path.join(dir, 'my_configuration.json'), "r", encoding="utf8"))
    else: config = json.load(open(os.path.join(dir, 'configuration.json'), "r", encoding="utf8"))

    interval_in_seconds_between_messages = config['interval_in_seconds_between_messages']
    show_messages_in_given_order = config['show_messages_in_given_order']
    show_messages_in_random_order = config['show_messages_in_random_order']
    messages = config['messages'][:-1]

    message = {}
    if show_messages_in_given_order == 'yes':
        curr_idx += 1
        message = messages[curr_idx]
    if show_messages_in_random_order == 'yes':
        message = random.choice(messages)

    showMsg(message['message'], message['font'], message['text_color'], message['background_color'], message['display_duration_in_seconds'])
    
    time.sleep(interval_in_seconds_between_messages)