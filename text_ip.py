

class input:
    def __init__(self):
        self.txt1=None
        self.txt2=None
    
    #getter
    def get_txt1(self):
        return self.txt1
    def get_txt2(self):
        return self.txt2
    
    #setting manual text input
    def set_txt1(self,txt1):
        self.txt1=txt1
    def set_txt2(self,txt2):
        self.txt2=txt2
   
    #setting text file input
    def set_txtf1(self,txtf1):
        f=open(txtf1,'r')
        self.txt1=f.read()
        f.close()
    def set_txtf2(self,txtf2):
        f=open(txtf2,'r')
        self.txt2=f.read()
        f.close()
