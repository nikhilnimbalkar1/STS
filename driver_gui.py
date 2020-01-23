
import text_ip as ip
import PySimpleGUI as sg
import vector_gen as vg


class driverGUI:
    def __init__(self):
        self.obj_ip=ip.input()
        self.obj_vg=vg.embedText()
        sg.theme('LightBlue')	
        self.ip_page = [  [sg.Text('Enter sentences')],
                    [sg.Text("Text 1", size=(8, 1)),sg.InputText()],
                    [sg.Text("Text 2", size=(8, 1)),sg.InputText()],
                    [sg.Text('or')],
                    [sg.Text('Choose files')],
                    [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse()],
                    [sg.Text('File 2', size=(8, 1)), sg.Input(), sg.FileBrowse()],
                    [sg.Button('Submit')]
                ]
        self.window = sg.Window('Semantic Text Similarity',self.ip_page,location=(575,300))
        self.event, self.values = self.window.read()
        while True:
            if self.event in (None, 'Cancel'):
                self.window.close()
            elif self.event in (None,'Submit') and len(self.values)==0:
                sg.popup("Please provide some input!")
                break
            elif self.event in (None, 'Submit') :
                sg.popup("Input is submitted!Please wait!")
                break 
            else:   
                sg.Popup("The System Developmment is in progress!")
                break
    
    
    def set_values(self):
        if(self.values[0]!='' and self.values[1] != ''):
            self.obj_ip.set_txt1(self.values[0])
            self.obj_ip.set_txt2(self.values[1])
        elif(self.values[2] !='' and self.values[3] !=''):
            self.obj_ip.set_txtf1(self.values[2])
            self.obj_ip.set_txtf2(self.values[3])
    
    
    def get_txt1(self):
        return self.obj_ip.get_txt1()
    
    def get_txt2(self):
        return self.obj_ip.get_txt2()

    def gen_vec1(self,snt1,snt2):
        self.obj_vg.embed_text(snt1,snt2)
    
    def get_vec1(self):
        return self.obj_vg.get_vec1()
    
    def get_vec2(self):
        return self.obj_vg.get_vec2()


def main():
    driver_instance=driverGUI()
    driver_instance.set_values()
    snt1=[driver_instance.get_txt1()]
    snt2=[driver_instance.get_txt2()]
    driver_instance.gen_vec1(snt1,snt2)
    print(driver_instance.get_vec1())
    
    
  

if __name__ == "__main__":
    main()