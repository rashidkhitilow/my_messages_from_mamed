import os, random, time, json, tkinter
def randomColor():
    letters = '0123456789ABCDEF'
    color = '#'
    for i in range(6):
        color += letters[int(random.random() * 16)]
    return color

def showMsg(msg, header="Message", font="Quicksand 50 bold", color="white", bgcolor="black", duration_seconds=5):
    if color == 'random': color = randomColor()
    if bgcolor == 'random': bgcolor = randomColor()
    root = tkinter.Tk()
    root.wm_title(header)
    root.wm_attributes("-topmost", 1)
    root.eval('tk::PlaceWindow . center')
    widget = tkinter.Label(root, text=msg, fg=color, bg=bgcolor, justify=tkinter.CENTER, anchor=tkinter.CENTER, font="Quicksand 50 bold").pack(expand=True, fill=tkinter.BOTH, ipadx=50, ipady=25)
    root.after(duration_seconds*1000, lambda: root.destroy())
    root.mainloop()


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

    showMsg(message['message'], message['header'], message['font'], message['text_color'], message['background_color'], message['display_duration_in_seconds'])

    time.sleep(interval_in_seconds_between_messages)