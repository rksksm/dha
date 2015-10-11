from django.db import models
from time import time
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models


def generate_filename91(instance, filename):
    return "src/static/img/construction/" + "1.jpg"
def generate_filename92(instance, filename):
    return "src/static/img/construction/" + "2.jpg"
def generate_filename93(instance, filename):
    return "src/static/img/construction/" + "3.jpg"
def generate_filename94(instance, filename):
    return "src/static/img/construction/" + "4.jpg"
def generate_filename95(instance, filename):
    return "src/static/img/construction/" + "5.jpg"
def generate_filename96(instance, filename):
    return "src/static/img/construction/" + "6.jpg"
def generate_filename97(instance, filename):
    return "src/static/img/construction/" + "7.jpg"
def generate_filename98(instance, filename):
    return "src/static/img/construction/" + "8.jpg"
def generate_filename99(instance, filename):
    return "src/static/img/construction/" + "9.jpg"
class Construction(models.Model):
	pic1 = models.FileField(upload_to=generate_filename91)
	pic2 = models.FileField(upload_to=generate_filename92)
	pic3 = models.FileField(upload_to=generate_filename93)
	pic4 = models.FileField(upload_to=generate_filename94)
	pic5 = models.FileField(upload_to=generate_filename95)
	pic6 = models.FileField(upload_to=generate_filename96)
	pic7 = models.FileField(upload_to=generate_filename97)
	pic8 = models.FileField(upload_to=generate_filename98)
	pic9 = models.FileField(upload_to=generate_filename99)





def generate_filename81(instance, filename):
    return "src/static/img/fabrication/" + "1.jpg"
def generate_filename82(instance, filename):
    return "src/static/img/fabrication/" + "2.jpg"
def generate_filename83(instance, filename):
    return "src/static/img/fabrication/" + "3.jpg"
def generate_filename84(instance, filename):
    return "src/static/img/fabrication/" + "4.jpg"
def generate_filename85(instance, filename):
    return "src/static/img/fabrication/" + "5.jpg"
def generate_filename86(instance, filename):
    return "src/static/img/fabrication/" + "6.jpg"
def generate_filename87(instance, filename):
    return "src/static/img/fabrication/" + "7.jpg"
def generate_filename88(instance, filename):
    return "src/static/img/fabrication/" + "8.jpg"
def generate_filename89(instance, filename):
    return "src/static/img/fabrication/" + "9.jpg"
class Fabrication(models.Model):
	pic1 = models.FileField(upload_to=generate_filename81)
	pic2 = models.FileField(upload_to=generate_filename82)
	pic3 = models.FileField(upload_to=generate_filename83)
	pic4 = models.FileField(upload_to=generate_filename84)
	pic5 = models.FileField(upload_to=generate_filename85)
	pic6 = models.FileField(upload_to=generate_filename86)
	pic7 = models.FileField(upload_to=generate_filename87)
	pic8 = models.FileField(upload_to=generate_filename88)
	pic9 = models.FileField(upload_to=generate_filename89)



def generate_filename11(instance, filename):
    return "src/static/img/slide/" + "1.jpg"
def generate_filename12(instance, filename):
    return "src/static/img/slide/" + "2.jpg"
def generate_filename13(instance, filename):
    return "src/static/img/slide/" + "3.jpg"
def generate_filename14(instance, filename):
    return "src/static/img/slide/" + "4.jpg"
def generate_filename15(instance, filename):
    return "src/static/img/slide/" + "5.jpg"
def generate_filename16(instance, filename):
    return "src/static/img/slide/" + "6.jpg"
def generate_filename17(instance, filename):
    return "src/static/img/slide/" + "7.jpg"
def generate_filename18(instance, filename):
    return "src/static/img/slide/" + "8.jpg"
class Home(models.Model):
	pic1 = models.FileField(upload_to=generate_filename11)
	pic2 = models.FileField(upload_to=generate_filename12)
	pic3 = models.FileField(upload_to=generate_filename13)
	pic4 = models.FileField(upload_to=generate_filename14)
	pic5 = models.FileField(upload_to=generate_filename15)
	pic6 = models.FileField(upload_to=generate_filename16)
	pic7 = models.FileField(upload_to=generate_filename17)
	pic8 = models.FileField(upload_to=generate_filename18)





def generate_filename21(instance, filename):
    return "src/static/img/about/" + "uncle1.jpg"
def generate_filename22(instance, filename):
    return "src/static/img/about/" + "uncle2.jpg"
def generate_filename23(instance, filename):
    return "src/static/img/about/" + "uncle3.jpg"	
class About(models.Model):
	pic1 = models.FileField(upload_to = generate_filename21)
	pic2 = models.FileField(upload_to = generate_filename22)
	pic3 = models.FileField(upload_to = generate_filename23)


def generate_filename41(instance, filename):
    return "src/static/img/interior/" + "1.jpg"
def generate_filename42(instance, filename):
    return "src/static/img/interior/" + "2.jpg"
def generate_filename43(instance, filename):
    return "src/static/img/interior/" + "3.jpg"
def generate_filename44(instance, filename):
    return "src/static/img/interior/" + "4.jpg"
def generate_filename45(instance, filename):
    return "src/static/img/interior/" + "5.jpg"
def generate_filename46(instance, filename):
    return "src/static/img/interior/" + "6.jpg"
def generate_filename47(instance, filename):
    return "src/static/img/interior/" + "7.jpg"
def generate_filename48(instance, filename):
    return "src/static/img/interior/" + "8.jpg"
def generate_filename49(instance, filename):
    return "src/static/img/interior/" + "9.jpg"
class Interior(models.Model):
	pic1 = models.FileField(upload_to=generate_filename41)
	pic2 = models.FileField(upload_to=generate_filename42)
	pic3 = models.FileField(upload_to=generate_filename43)
	pic4 = models.FileField(upload_to=generate_filename44)
	pic5 = models.FileField(upload_to=generate_filename45)
	pic6 = models.FileField(upload_to=generate_filename46)
	pic7 = models.FileField(upload_to=generate_filename47)
	pic8 = models.FileField(upload_to=generate_filename48)
	pic9 = models.FileField(upload_to=generate_filename49)



def generate_filename31(instance, filename):
    return "src/static/img/building/" + "1.jpg"
def generate_filename32(instance, filename):
    return "src/static/img/building/" + "2.jpg"
def generate_filename33(instance, filename):
    return "src/static/img/building/" + "3.jpg"
def generate_filename34(instance, filename):
    return "src/static/img/building/" + "4.jpg"
def generate_filename35(instance, filename):
    return "src/static/img/building/" + "5.jpg"
def generate_filename36(instance, filename):
    return "src/static/img/building/" + "6.jpg"
def generate_filename37(instance, filename):
    return "src/static/img/building/" + "7.jpg"
def generate_filename38(instance, filename):
    return "src/static/img/building/" + "8.jpg"
def generate_filename39(instance, filename):
    return "src/static/img/building/" + "9.jpg"
class Building(models.Model):
	pic1 = models.FileField(upload_to=generate_filename31)
	pic2 = models.FileField(upload_to=generate_filename32)
	pic3 = models.FileField(upload_to=generate_filename33)
	pic4 = models.FileField(upload_to=generate_filename34)
	pic5 = models.FileField(upload_to=generate_filename35)
	pic6 = models.FileField(upload_to=generate_filename36)
	pic7 = models.FileField(upload_to=generate_filename37)
	pic8 = models.FileField(upload_to=generate_filename38)
	pic9 = models.FileField(upload_to=generate_filename39)


def generate_filename51(instance, filename):
    return "src/static/img/modular/" + "1.jpg"
def generate_filename52(instance, filename):
    return "src/static/img/modular/" + "2.jpg"
def generate_filename53(instance, filename):
    return "src/static/img/modular/" + "3.jpg"
def generate_filename54(instance, filename):
    return "src/static/img/modular/" + "4.jpg"
def generate_filename55(instance, filename):
    return "src/static/img/modular/" + "5.jpg"
def generate_filename56(instance, filename):
    return "src/static/img/modular/" + "6.jpg"
def generate_filename57(instance, filename):
    return "src/static/img/modular/" + "7.jpg"
def generate_filename58(instance, filename):
    return "src/static/img/modular/" + "8.jpg"
def generate_filename59(instance, filename):
    return "src/static/img/modular/" + "9.jpg"
class Modular(models.Model):
	pic1 = models.FileField(upload_to=generate_filename51)
	pic2 = models.FileField(upload_to=generate_filename52)
	pic3 = models.FileField(upload_to=generate_filename53)
	pic4 = models.FileField(upload_to=generate_filename54)
	pic5 = models.FileField(upload_to=generate_filename55)
	pic6 = models.FileField(upload_to=generate_filename56)
	pic7 = models.FileField(upload_to=generate_filename57)
	pic8 = models.FileField(upload_to=generate_filename58)
	pic9 = models.FileField(upload_to=generate_filename59)

def generate_filename71(instance, filename):
    return "src/static/img/corporate/" + "1.jpg"
def generate_filename72(instance, filename):
    return "src/static/img/corporate/" + "2.jpg"
def generate_filename73(instance, filename):
    return "src/static/img/corporate/" + "3.jpg"
def generate_filename74(instance, filename):
    return "src/static/img/corporate/" + "4.jpg"
def generate_filename75(instance, filename):
    return "src/static/img/corporate/" + "5.jpg"
def generate_filename76(instance, filename):
    return "src/static/img/corporate/" + "6.jpg"
def generate_filename77(instance, filename):
    return "src/static/img/corporate/" + "7.jpg"
def generate_filename78(instance, filename):
    return "src/static/img/corporate/" + "8.jpg"
def generate_filename79(instance, filename):
    return "src/static/img/corporate/" + "9.jpg"
class Corporate(models.Model):
	pic1 = models.FileField(upload_to=generate_filename71)
	pic2 = models.FileField(upload_to=generate_filename72)
	pic3 = models.FileField(upload_to=generate_filename73)
	pic4 = models.FileField(upload_to=generate_filename74)
	pic5 = models.FileField(upload_to=generate_filename75)
	pic6 = models.FileField(upload_to=generate_filename76)
	pic7 = models.FileField(upload_to=generate_filename77)
	pic8 = models.FileField(upload_to=generate_filename78)
	pic9 = models.FileField(upload_to=generate_filename79)


def generate_filename61(instance, filename):
    return "src/static/img/icon/" + "1.jpg"
def generate_filename62(instance, filename):
    return "src/static/img/icon/" + "2.jpg"
def generate_filename63(instance, filename):
    return "src/static/img/icon/" + "3.jpg"
def generate_filename64(instance, filename):
    return "src/static/img/icon/" + "4.jpg"
def generate_filename65(instance, filename):
    return "src/static/img/icon/" + "5.jpg"
def generate_filename66(instance, filename):
    return "src/static/img/icon/" + "6.jpg"
def generate_filename67(instance, filename):
    return "src/static/img/icon/" + "7.jpg"
def generate_filename68(instance, filename):
    return "src/static/img/icon/" + "8.jpg"
def generate_filename69(instance, filename):
    return "src/static/img/icon/" + "9.jpg"
def generate_filename610(instance, filename):
    return "src/static/img/icon/" + "10.jpg"
def generate_filename611(instance, filename):
    return "src/static/img/icon/" + "11.jpg"
def generate_filename612(instance, filename):
    return "src/static/img/icon/" + "12.jpg"
def generate_filename613(instance, filename):
    return "src/static/img/icon/" + "13.jpg"
def generate_filename614(instance, filename):
    return "src/static/img/icon/" + "14.jpg"
def generate_filename615(instance, filename):
    return "src/static/img/icon/" + "15.jpg"

class Icon(models.Model):
	pic1 = models.FileField(upload_to=generate_filename61)
	pic2 = models.FileField(upload_to=generate_filename62)
	pic3 = models.FileField(upload_to=generate_filename63)
	pic4 = models.FileField(upload_to=generate_filename64)
	pic5 = models.FileField(upload_to=generate_filename65)
	pic6 = models.FileField(upload_to=generate_filename66)
	pic7 = models.FileField(upload_to=generate_filename67)
	pic8 = models.FileField(upload_to=generate_filename68)
	pic9 = models.FileField(upload_to=generate_filename69)
	pic10 = models.FileField(upload_to=generate_filename610)
	pic11 = models.FileField(upload_to=generate_filename611)
	pic12 = models.FileField(upload_to=generate_filename612)
	pic13 = models.FileField(upload_to=generate_filename613)
	pic14 = models.FileField(upload_to=generate_filename614)
	pic15 = models.FileField(upload_to=generate_filename615)
