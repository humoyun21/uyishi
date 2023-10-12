class Car:
    def __init__(self, nom: str, narx: str, yil: int) -> None:
        self.benzin = 2 
        self.benzin_sigimi = 50 
        self.km = 0 
        self.engine = "O'chiq" 
        self.nom = nom 
        self.narx = narx 
        self.yil = yil 

    def start(self):
        print("Moshina o't oldi")
        self.engine = "Yoniq"


    def stop(self):
        self.engine = "O'chiq"
        print("Moshina o'chdi")


    def yur(self, km):
        if self.engine == "O'chiq":
            print("Avval moshinani o't oldiring!")
        else:
            if km <=self.benzin:
                print(f"Moshina {km} km yurdi")
                self.benzin = self.benzin - km
                self.km = self.km + km
            else:
                if self.benzin == 0:
                    print(f"Moshinada {km} km uchun yetarli benzin mavjud emas. Moshinada 0 l benzin mavjud. Siz moshina {km} km ga borishi uchun {km} l benzin quyishingiz kerak!")
                elif self.benzin > 0:
                    ha_yoq = input(f"Moshinada {km} km uchun yetarli benzin mavjud emas. Moshinada {self.benzin} l benzin mavjud va siz {self.benzin} km yura olasiz!\n{self.benzin} km yurishni xoxlaysizmi?\nHa/Yo'q\n")
                    if ha_yoq == "Ha":
                        print(f"Moshina {self.benzin} km yurdi")
                        self.km = self.km + self.benzin
                        self.benzin = 0

                    elif ha_yoq == "Yo'q":
                        print(f"Moshina yurmadi!\nSizda {self.benzin} l benzin mavjud")

    
    def quyish(self, litr):
        max_quyish = self.benzin_sigimi - self.benzin
        if max_quyish >= litr:
            self.benzin = self.benzin + litr
            if self.benzin == self.benzin_sigimi:
                print(f"Moshinaga {litr} l benzin quyildi. Moshinada {self.benzin} l benzin mavjud! Moshinada benzin to'la!")
            elif self.benzin < self.benzin_sigimi:
                print(f"Moshinaga {litr} l benzin quyildi. Moshinada {self.benzin} l benzin mavjud! Moshinada maksimum benzin sig'imi {self.benzin_sigimi} l. Moshinada benzin to'lmadi! Moshinaga to'la benzin quyish uchun yana {self.benzin_sigimi - self.benzin} l benzin quying!")
        elif max_quyish < litr:
            print(f"Moshinada benzin to'ldi va sizda {litr - max_quyish} l benzin oshib qoldi!")
            self.benzin = self.benzin_sigimi

    def moshina_haqida_malumot(self):
        print(f"Moshina holati: {self.engine}")
        print(f"Moshina nomi: {self.nom}")
        print(f"Moshina bosgan yo'li: {self.km} km")
        print(f"Moshina yili: {self.yil} yil")
        print(f"Moshina narxi: {self.narx}")
        print(f"Moshina benzin sig'imi: {self.benzin_sigimi} l")
        print(f"Moshinada {self.benzin} l mavjud")


car = Car("Cobalt", "$20000", 2021)
car.yur(5)
car.quyish(10)