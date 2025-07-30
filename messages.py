import json
import os
import random
import time
import PySimpleGUI as sg

def randomColor():
    letters = '0123456789ABCDEF'
    color = '#'
    for _ in range(6):
        color += letters[int(random.random() * 16)]
    return color

def showMsg(msg, font="Quicksand 50 bold", color="white", bgcolor="black", duration_seconds=5):
    if color == 'random': 
        color = randomColor()
    if bgcolor == 'random': 
        bgcolor = randomColor()
    sg.PopupNoButtons(
        msg,
        background_color=bgcolor,
        text_color=color,
        auto_close=True,
        auto_close_duration=duration_seconds,
        font=font,
        grab_anywhere=True,
        keep_on_top=True,
        modal=True,
        no_titlebar=True
    )

curr_idx = -1
while True:
    # Load configuration
    dir = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(dir, 'my_configuration.json')
    if not os.path.exists(config_file):
        config_file = os.path.join(dir, 'configuration.json')

    if not os.path.exists(config_file):
        print("Configuration file not found. Please ensure 'my_configuration.json' or 'configuration.json' exists.")
        break

    with open(config_file, "r", encoding="utf8") as f:
        config = json.load(f)

    # Extract settings
    interval_in_seconds_between_messages = config.get('interval_in_seconds_between_messages', 5)
    show_messages_in_given_order = config.get('show_messages_in_given_order', 'no')
    show_messages_in_random_order = config.get('show_messages_in_random_order', 'no')
    messages = config.get('messages', [])

    # Validate messages
    if not messages:
        print("No messages available in the configuration file.")
        break

    # Ensure at least one mode is enabled
    if show_messages_in_given_order != 'yes' and show_messages_in_random_order != 'yes':
        print("Neither 'show_messages_in_given_order' nor 'show_messages_in_random_order' is enabled.")
        break

    # Select a message
    message = {}
    if show_messages_in_given_order == 'yes':
        curr_idx += 1
        if curr_idx >= len(messages):
            curr_idx = 0  # Reset to the first message
        message = messages[curr_idx]
    elif show_messages_in_random_order == 'yes':
        message = random.choice(messages)

    # Display the message
    if not message:
        print("No valid message found.")
        break

    print(f"Displaying message: {message}")
    showMsg(
        message.get('message', ''),
        message.get('font', "Quicksand 50 bold"),
        message.get('text_color', 'white'),
        message.get('background_color', 'black'),
        message.get('display_duration_in_seconds', 5)
    )

    # Wait for the interval before showing the next message
    time.sleep(interval_in_seconds_between_messages)
