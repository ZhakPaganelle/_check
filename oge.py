import PySimpleGUI as sg
import re

def start_window():
    global window
    start_layout = [[sg.InputText(key='text')], [sg.Button('Enter')]]

    window = sg.Window('Start', start_layout)
    process()

def main_window():
    global window
    
    text = window['text'].get()
    text = re.sub('\s?\(?\d\)', '', text)
    text = text.split()
    
    main_layout = [[sg.Text(word, key=word, enable_events=True, right_click_menu=['Right', [f'{word},', f'{word}|,']]) for word in text[:len(text)//3]],
                   [sg.Text(word, key=word, enable_events=True, right_click_menu=['Right', [f'{word},', f'{word}|,']]) for word in text[len(text)//3:len(text)*2//3]],
                   [sg.Text(word, key=word, enable_events=True, right_click_menu=['Right', [f'{word},', f'{word}|,']]) for word in text[len(text)*2//3:]]]
    
    window.close()
    window = sg.Window('Main', main_layout)
    
    
def process():
    global window

    while True:
            event, values = window.read()
            if event in (None, 'Cancel'):
                window.close()
                break
            elif event == 'Enter':
                main_window()
            elif event[-1] == ',':
                point(event)
            else:
                collapse(event)

def point(word):
    global window
    if '|' in word:
        window[word[:-2]](word[:-2])
        return
    window[word[:-1]](word)

def collapse(word):
    global window

    if window[word].get_size()[0] == 12:
        window[word].set_size((0, 1))
        window[word](background_color='#64778D')
    else:
        window[word].set_size((1, 1))
        window[word](background_color='White')
    
    
start_window()
