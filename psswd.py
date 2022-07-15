import random 
import time
# Heves İçin Yapıldı Gökhan SU ya teşekkürlerimi iletirim.
input('Şifreniz Oluşturuldu Lütfen Entera Basınız.')

liste = ['A-£','@b23','!c','Z#r+','bGz','Xj','Root','HzX']
liste1 = ['A-','b23','Qc','Xr-','ZoRt','zXj','Root','BbC']
liste2 = ['A-','b24','Qm','Xr+','ZiRt','bXj','Rx','zJ']
liste3 = ['A-','b25','Qn','Xa','ALAJ','Xbj','AJ','AzQ']
liste4 = ['A-','b26','Qt','Xr+','BaQ','sXj','AqO','B31']
liste5 = ['A-','b27','Qr','Xb','DxJ','Xdj','BoR','tOx']
liste6 = ['A-','b29','Qd','Xc+','gIz','Xoj','ZXrT','RzC']
liste7 = ['A-','b30','Qa','Xd+','bOaJ','Xhj','AlAh','hZx']
liste8 = ['A-','b31','Qb','Xf+','bja','zNj','xd','SxL']
bir = random.choice(liste)
bir2 = random.choice(liste2)
bir3 = random.choice(liste3)
bir4 = random.choice(liste4)
bir5 = random.choice(liste5)
bir6 = random.choice(liste6)
bir7 = random.choice(liste7)
bir8 = random.choice(liste8)
print('Bizi Tercih Ettiğiniz İçin Çok Teşekkür Ederim')
print('Şifreniz : ' ,bir+bir2+bir3+bir4+bir5+bir6+bir7+bir8)
print("""  _____                     _ 
 |  __ \                   | |
 | |__) |__ _____      ____| |
 |  ___/ __/ __\ \ /\ / / _` |
 | |   \__ \__ \\ V  V / (_| |
 |_|   |___/___/ \_/\_/ \__,_|
                              
                              """)
print("1 - Kaydet\n2 - Kaydetme")
root = input("Şifreniz Kaydedilsin Mi??? 1/2 : ")
if root=='1':
    allah = open("sonsifreniz.txt","w")
    allah.write(bir+bir2+bir3+bir4+bir5+bir6+bir7+bir8)

time.sleep(10)
########################################
#                                      #
# MADED BY ROOTMAN X                   #    
# Don't Use Project On Other Stuffs <3 #
#                                      #
########################################
