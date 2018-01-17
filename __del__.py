class Yazýlýmcý(): #Yazýlýmcý Clasý Baþlýðý Oluþturuldu./Aþaðýda Özellikler verilecek.
    def __init__(self,isim,soyisim,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.diller=diller
#Buraya kadar sadece içinde olacak özellikleri girdik.

    def __str__(self):
        return " Ýsim : {}\n Soyisim : {} \n Maaþ : {}\n Diller : {}".format(self.isim,self.soyisim,self.maas,self.diller)
    def __len__(self):
        return  self.maas
    def __del__(self):
        print ("Baþarýyla silindi..")



yazilimci=Yazýlýmcý("omer","akkoyun",5500,["java","python","Html","JS"])

del yazilimci #yazilimci deðiþkenini silecek




çýktý:
Baþarýyla silindi..
