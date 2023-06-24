# -*- coding: utf-8 -*-
"""print()_fonksiyonu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b2sW6f6u9etapcFBh8oSv1FsERcQAzYD
"""

#TEMEL FONKSİYONLAR
#print Fonksiyonu
#print( ) fonksiyonu, konsola çıktı göndermek amacıyla kullanılır.

print('değer')
print("değer")
print("""değer""")
#konsola gönderilecek değer bir metinsel ifade ise bu ifade çift tırnak, tek tırnak ya da üç çift tırnak içinde yazılabilir.
#eğer konsola gönderilecek değer bir değişken ya da sayısal bir ifade ise bu durumda tırnak içerisinde yazmaya gerek yoktur.

print(7)
#print( ) fonksiyonu kullanılırken parantez içerisinde kullanılan değerlere argüman denilmektedir. Python, print( ) fonksiyonu argümanını kontrol ederek, belirtilen kurallara uyup uymadığını kontrol eder.

print("python)
#tırnak kapatılmadığı için hata mesajı verir.

print(a)
#değişken tanımlanmadığı için hata mesajı verir.

print("Merhaba, Dünya!")
#karakter dizilerinde çift tırnak, tek tırnak ya da üç çift tırnak kullanılmalıdır.

print('Türkiye'nin başkenti Ankara'dır')
#bu kullanıma bakıldığında karakter dizisi tek tırnak işareti ile başlamış, ancak kesme işareti olarak kullanıldığı yerde sonlanmıştır.
#Burada çift tırnak ve tek tırnak beraber kullanılarak sorun çözülür.
print("Türkiye'nin başkenti Ankara'dır")

print(2+2)
#print( ) fonksiyonu, bu şekilde aritmetik işlemler yapmak amacıyla kullanılabilir.

#print() Fonksiyonu ile Kullanılabilen Parametreler
#print() fonksiyonu kullanılırken karakter dizilerinde tek tırnak ve çift tırnak işaretleri (‘ ,“ ,“““) kullanılır.
#bu işaretler karakter dizilerinin nerede başladığını ve bittiğini ifade eder.

#ters taksim(\)
print("Merhaba," Python "öğreniyorum")
#çift tırnak işareti arasındaki “Merhaba, ” kelimesi karakter dizisi olarak algılandı ama sonrasında Python kelimesi çift tırnak içinde ve argümanlar arasında “,” virgül olmadığı için hata verdi.
#bu problemi çözmek için kaçış parametreleri (escape character) kullanılmalıdır.

print('Samsun\'un pidesi meşhurdur.')
#\ karakteri kendinden sonra gelen kesme ‘ işaretinin dikkate alınmaması gerektiği anlamı vermektedir.
#aynı işlem çift tırnakla da yapılabilir.

#alt satır başı (\n)
print("1.satır\n2.satır\n3.satır")
#karakter dizilerinde bazen alt satıra inme ihtiyacı duyulabilir. Python’da en sık kullanılan kaçış parametresi \n parametresidir.

#sekme(\t)
print("ocak\tşubat\tmart")
#klavyeden tab tuşuna basıldığındaki gibi belirli karakter boşluk bırakılmasını sağlayan bir parametredir.

#end Parametresi
print("Merhaba!")
print("Dünya")
#kodların çıktısı alt alta verilmiştir. Ancak bazı durumlarda programın çıktısı birleştirilmek istenir.
#işte bu gibi durumlarda end parametresi çok işe yaramaktadır.
print("Merhaba!",end=" ")
print("Dünya")
#end parametresi içinde iki tırnak arasında boşluk karakteri kullanıldığı için program çıktısını birleştirerek araya boşluk eklendi.
print("Merhaba!",end=",")
print("Dünya")
#aynı işlem virgül kullanılarak yapılabilir.

#sep() Parametresi
print("pazartesi","salı","çarşamba","perşembe","cuma")
print("pazartesi","salı","çarşamba","perşembe","cuma",sep="-")
#her bir argümanın arasında farklı işlemler sep parametresi ile yapılabilir.
#sep parametresi yardımıyla birer kural belirlenebilir.

#format() Metodu ile Biçimlendirme İşlemleri
a=2
b=3
c=5
print("girilen",a,b, "ve",c,"değerlerinin toplamı: ",a+b+c,"dur")
#bu hata yapmaya müsait bir kullanımdır.Bu gibi durumlar için print( ) fonksiyonunda format metodunun kullanılması daha uygun olur.
print("çıktı işlemi denemesi {} {} {}".format(3,2,1))
#print( ) fonksiyonunda kullanılan her bir {} ifadesine karşılık olarak format(  ) metoduna bir adet argüman verilmelidir.
a=2
b=3
c=5
print("girilen {} , {} ve {} değerlerinin toplamı= {} dir".format(a,b,c,a+b+c))
#Süslü parantez içine sayılar girerek format metodu ile hangi sıradaki değerin geleceği belirlenir.

print("{1} {0} {2}".format(10,"Python",20))

print("Memleket isterim,\nGök mavi, dal yeşil, tarla sarı olsun,")

print("Memleket isterim,","Gök mavi, dal yeşil, tarla sarı olsun,")

print("Memleket isterim,")
print("Gök mavi, dal yeşil" ,"tarla sarı olsun,")

print("Memleket isterim,",end=" ")
print("Gök mavi, dal yeşil" ,"tarla sarı olsun,")

print("Memleket","isterim","Gök mavi","dal", "yeşil",sep="-")

print(" *")
print(" * *")
print(" * *")
print(" * *")
print("*** ***")
print(" * *")
print(" * *")
print(" *****")

not1 = 95
not2 = 100
print('1.Sınav Notu:{} \n2.Sınav Notu:{}'.format(not1,not2))