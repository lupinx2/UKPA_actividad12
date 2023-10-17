import PySimpleGUI as sg
import requests
import json

if __name__ == '__main__':
    sg.theme('Default1')
    layout = [[sg.Text('Encontrar Colonia por Código Postal')],      
                 [sg.InputText()],
                 [sg.Submit( bind_return_key=True, button_text='Buscar')],
                 [sg.Combo(values=('one', 'two', 'three four'), key='-COLONIAS-', enable_events=True, size=(40, 1))],
                 [sg.Text('', key='-ALERT-')]]


window = sg.Window('Actividad 12', layout)
url = 'http://127.0.0.1:6660/API_colonias.php'
# El archivo API_colonias.php debe estar hosteado en un servidor local en el puerto 6660

while True:
    event, values = window.read()
    if event == 'Buscar':
        window['-ALERT-'].update('')
        codigoPostal = values[0]
        if codigoPostal.isnumeric() and len(codigoPostal) == 5:
            response = requests.get(url + '?cp=' + codigoPostal)
            if response.status_code == 200:
                if response.text == "Zero":
                    window['-ALERT-'].update('No se encontraron colonias')
                    continue
                # la respuesta es una lista de diccionarios, pero PySimpleGUI quiere un tuple de strings:
                colonias_dicts = json.loads(response.text)
                colonias_tuple = tuple(d['colonia'] for d in colonias_dicts)
                window['-COLONIAS-'].update(values=colonias_tuple)
            else:
                window['-ALERT-'].update('Error al buscar colonias: ' + str(response.reason) + ' (' + str(response.status_code) + ')')
        else:
            window['-ALERT-'].update('Código postal inválido')
    if event == sg.WIN_CLOSED:
        window.close()
        break