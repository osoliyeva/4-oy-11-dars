class Karta:
    def __init__(self,card_name):
        self.card_name=card_name
    
    def set_card_name(self,new_card_name):
        self.card_name=new_card_name
    
    def get_card(self):
        return self.card_name
    
    def compare(self,player2):
        if player2.card_name==self.card_name:
            print("durang!")
        elif player2.card_name=="A":
            print("2-o'yinchi g'olib")
        elif player2.card_name<self.card_name:
            print("1-o'yinchi g'olib")
        elif player2.card_name>self.card_name:
            print("2-o'yinchi g'olib")
        elif player2.card_name=="J" and self.card_name!="Q" and self.card_name!="K" and self.card_name!="A":
            print("2-o'yinchi g'olib")
        elif player2.card_name=="Q" and self.card_name!="K" and self.card_name!="A":
            print("2-o'yinchi g'olib")
        elif player2.card_name=="K" and self.card_name!="A":
            print("2-o'yinchi g'olib")
        else:
            print("1-o'yinchi g'olib")


player1=Karta("A")
player2=Karta("K")

player1.compare(player2)
        
