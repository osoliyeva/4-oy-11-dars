from abc import ABC, abstractmethod
from datetime import datetime

class HisopInterfacesi(ABC):
    @abstractmethod
    def depozit(self):
        ...
    
    @abstractmethod
    def yechish(self):
        pass

class BankHisobi(HisopInterfacesi):
    def __init__(self, raqam, ism, turi, balans=0.0) -> None:
        self.__hisop_raqami = raqam     
        self.__egasi_ism = ism
        self.__hisop_turi = turi
        self.__balans = balans

    def depozit(self, miqdor: float) -> None:
        self.__balans += miqdor
        with open("depozitlar.txt", "a+") as fl:
            fl.write(f"Hisob Raqami: {self.__hisop_raqami}, Ism: {self.__egasi_ism}, Turi: {self.__hisop_turi}, Depozit: {miqdor}, Vaqt: {datetime.now()}\n")

    def yechish(self, miqdor: float) -> None:
        if miqdor > self.__balans:
            print("Hisobingizda yetarli mablag' mavjud emas!")
        else:
            self.__balans -= miqdor
            with open("yechimlar.txt", "a+") as fl:
                fl.write(f"Hisob Raqami: {self.__hisop_raqami}, Ism: {self.__egasi_ism}, Turi: {self.__hisop_turi}, Yechim: {miqdor}, Vaqt: {datetime.now()}\n")
    
    def get_balans(self) -> float:
        return self.__balans
    

    def __str__(self) -> str:
        return f"Hisob Raqami: {self.__hisop_raqami}\nIsm: {self.__egasi_ism}\nHisob Turi: {self.__hisop_turi}\nBalans: {self.__balans}"


class BankMenedjer:
    def __init__(self) -> None:
        self.hisoblar = []

    def yaratish_hisob(self, hisob: BankHisobi) -> None:
        self.hisoblar.append(hisob)
    
    def olish_hisob(self, hisob_raqami: str) -> BankHisobi:
        for hisob in self.hisoblar:
            if hisob.__hisop_raqami == hisob_raqami:
                return hisob
        raise ValueError(f"{hisob_raqami} raqamli hisob topilmadi.")

    def o_tkazish_mablag(self, dan_hisob: BankHisobi, ga_hisob: BankHisobi, miqdor: float) -> None:
        if dan_hisob.yechish(miqdor):
            ga_hisob.depozit(miqdor)
            print(f"{miqdor} summani {dan_hisob.__egasi_ism}'dan {ga_hisob.__egasi_ism}'ga o'tkazdingiz")
        else:
            print("O'tkazish mablag' yetarli emas.")

if __name__ == "__main__":
    bank_menedjer = BankMenedjer()

    
    hisob1 = BankHisobi("123456789", "Odinaxon", "Jamg'arma")
    hisob2 = BankHisobi("987654321", "Soliyeva", "Joriy", 1000.0)

   
    bank_menedjer.yaratish_hisob(hisob1)
    bank_menedjer.yaratish_hisob(hisob2)

    
    hisob1.depozit(500.0)
    hisob2.yechish(200.0)

   
    bank_menedjer.o_tkazish_mablag(hisob2, hisob1, 300.0)

    
    print(hisob1)
    print(hisob2)



bank_menedjer = BankMenedjer()

hisob1 = BankHisobi("123456789", "Odinaxon'", "Jamg'arma")
hisob2 = BankHisobi("987654321", "Soliyeva", "Joriy", 1000.0)

bank_menedjer.yaratish_hisob(hisob1)
bank_menedjer.yaratish_hisob(hisob2)

hisob1.depozit(500.0)
hisob2.yechish(200.0)

bank_menedjer.o_tkazish_mablag(hisob2, hisob1, 300.0)

print(hisob1)
print(hisob2)


# public qimadimmikin hozi