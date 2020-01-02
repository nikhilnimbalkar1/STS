
import text_ip as ip
import PySimpleGUI as sg

def main_GUI():
    sg.theme('LightBlue')	
    layout = [  [sg.Text('Enter sentences')],
                [sg.Text("Text 1", size=(8, 1)),sg.InputText()],
                [sg.Text("Text 2", size=(8, 1)),sg.InputText()],
                [sg.Text('or')],
                [sg.Text('Choose files')],
                [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse()],
                [sg.Text('File 2', size=(8, 1)), sg.Input(), sg.FileBrowse()],
                [sg.Button('Submit')]
            ]
    window = sg.Window('Semantic Text Similarity', layout,location=(575,300))
    event, values = window.read()
    while True:
        if event in (None, 'Cancel'):
            window.close()
        else:   
            sg.Popup("The System Developmment is in progress!")
            break
    return values
def error_popup():
    sg.Popup("Please enter some text!!")
    main_GUI()

values=main_GUI()

if(values[0]!='' and values[1] != ''):
    obj=ip.input()
    obj.set_txt1(values[0])
    obj.set_txt2(values[1])
elif(values[2] !='' and values[3] !=''):
     obj=ip.input()
     obj.set_txtf1(values[2])
     obj.set_txtf2(values[3])
else:
    error_popup()

'''
a=obj.get_txt1()
b=obj.get_txt2()
print(a,b)
'''
