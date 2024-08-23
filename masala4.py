class Alphabet:
    def __init__(self,til=str()):
        self.til=til
        self.harflar=[]
        self.count=0
    
    def printf(self):
        for i in self.harflar:
            print(i)
            self.count+=1
        print(f"{self.til} alfavitida {self.count} ta harf bor")


class EngAlphabet(Alphabet):
    def __init__(self):
        self.til="Ingliz"
        self.harflar=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.count=0
    
    def compare(self,new_item):
        if new_item in self.harflar:
            print(f"{new_item} ingliz alfavitida bor")
        else:
            print(f"{new_item} ingliz alfavitida yo'q")
    
    def text(self):
        print(f"There are {self.count} items in English alphabet ")


english=EngAlphabet()
english.printf()
english.compare("F")
english.compare("Ш")
english.text()