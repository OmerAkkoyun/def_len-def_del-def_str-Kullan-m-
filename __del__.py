class Yaz�l�mc�(): #Yaz�l�mc� Clas� Ba�l��� Olu�turuldu./A�a��da �zellikler verilecek.
    def __init__(self,isim,soyisim,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.diller=diller
#Buraya kadar sadece i�inde olacak �zellikleri girdik.

    def __str__(self):
        return " �sim : {}\n Soyisim : {} \n Maa� : {}\n Diller : {}".format(self.isim,self.soyisim,self.maas,self.diller)
    def __len__(self):
        return  self.maas
    def __del__(self):
        print ("Ba�ar�yla silindi..")



yazilimci=Yaz�l�mc�("omer","akkoyun",5500,["java","python","Html","JS"])

del yazilimci #yazilimci de�i�kenini silecek




��kt�:
Ba�ar�yla silindi..
