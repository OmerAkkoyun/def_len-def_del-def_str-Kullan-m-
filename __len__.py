class Yaz�l�mc�(): #Yaz�l�mc� Clas� Ba�l��� Olu�turuldu./A�a��da �zellikler verilecek.
    def __init__(self,isim,soyisim,maa�,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.maa�=maa�
        self.diller=diller
#Buraya kadar sadece i�inde olacak �zellikleri girdik.

    def __str__(self):
        return " �sim : {}\n Soyisim : {} \n Maa� : {}\n Diller : {}".format(self.isim,self.soyisim,self.maa�,self.diller)


    def __len__(self):
        return  self.maa�



yazilimci=Yaz�l�mc�("omer","akkoyun",5500,["java","python","Html","JS"])
print (yazilimci)
print (len(yazilimci))




��kt�s�:


	�sim : omer
	Soyisim : akkoyun 
	Maa� : 5500
	Diller : ['java', 'python', 'Html', 'JS']
	5500