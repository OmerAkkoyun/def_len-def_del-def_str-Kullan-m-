class Yazýlýmcý(): #Yazýlýmcý Clasý Baþlýðý Oluþturuldu./Aþaðýda Özellikler verilecek.
    def __init__(self,isim,soyisim,maaþ,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.maaþ=maaþ
        self.diller=diller
#Buraya kadar sadece içinde olacak özellikleri girdik.

    def __str__(self):
        return " Ýsim : {}\n Soyisim : {} \n Maaþ : {}\n Diller : {}".format(self.isim,self.soyisim,self.maaþ,self.diller)


    def __len__(self):
        return  self.maaþ



yazilimci=Yazýlýmcý("omer","akkoyun",5500,["java","python","Html","JS"])
print (yazilimci)
print (len(yazilimci))




çýktýsý:


	Ýsim : omer
	Soyisim : akkoyun 
	Maaþ : 5500
	Diller : ['java', 'python', 'Html', 'JS']
	5500