import PySimpleGUI as sg
import random
from array import array

sg.theme("Topanga")
layout = [[sg.Text('Размер массива:')],
          [sg.Slider(range=(1, 50), default_value=25, enable_events=True, orientation='horizontal', key='-ARRELEMS-', size=(30, 20),expand_x=True)],
          [sg.Text('Кратность:')], [sg.Slider(range=(1, 50), default_value=5, enable_events=True, orientation='horizontal', key='-DIVIDED-',size=(30, 20),expand_x=True)],
          [sg.Button('Генерация', key='-generate-', size=(15, 1), pad=((5, 0), (10, 0))), sg.Button('Выйти', size=(15, 1), pad=((14, 0), (10, 0)))],
          [sg.Text('Сгенерированный массив:'), sg.Text(key='-OUTPUTARRAY-',size=(70,2))],
          [sg.Text('Элементы % :', key='KR', size=(20, 1)), sg.Text(key='-DIVIDEDARRAY-',size=(70,2))]]

def generateArray():
    sizeArray = int(values['-ARRELEMS-'])
    dividedBy = int(values['-DIVIDED-'])

    arr = [None] * sizeArray

    for i in range(len(arr)):
        arr[i] = random.randrange(101)

    arrayDivided5 = array('i')
    count = 0
    for a in range(len(arr)):
        if arr[a] % dividedBy == 0:
            arrayDivided5.append(arr[a])
            count+=1
    window['-OUTPUTARRAY-'].update(str(arr).strip('[]'))
    krStr = "Элементы % " + str(dividedBy) + " ("+str(count)+" всего)" +":"
    window['KR'].update(krStr)
    if len(arrayDivided5) != 0:
        window['-DIVIDEDARRAY-'].update(', '.join(map(str, arrayDivided5)))
    else:
        window['-DIVIDEDARRAY-'].update("Ничего не найдено")

window = sg.Window('Транспортный налог', layout, size=(800, 300))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == "-generate-":
        generateArray()

window.close()
