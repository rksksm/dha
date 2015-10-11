from django.db import models
from time import time
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models

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





def generate_filename(instance, filename):
    return "src/static/img/about/" + "uncle.jpg"
	
class About(models.Model):
	pic = models.FileField(upload_to = generate_filename)




def generate_filename31(instance, filename):
    return "src/static/img/services/" + "1.jpg"
def generate_filename32(instance, filename):
    return "src/static/img/services/" + "2.jpg"
def generate_filename33(instance, filename):
    return "src/static/img/services/" + "3.jpg"
def generate_filename34(instance, filename):
    return "src/static/img/services/" + "4.jpg"
def generate_filename35(instance, filename):
    return "src/static/img/services/" + "5.jpg"   
def generate_filename36(instance, filename):
    return "src/static/img/services/" + "6.jpg"
class Services(models.Model):
	pic1 = models.FileField(upload_to=generate_filename31)
	pic2 = models.FileField(upload_to=generate_filename32)
	pic3 = models.FileField(upload_to=generate_filename33)
	pic4 = models.FileField(upload_to=generate_filename34)
	pic5 = models.FileField(upload_to=generate_filename35)
	pic6 = models.FileField(upload_to=generate_filename36)




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
def generate_filename410(instance, filename):
    return "src/static/img/interior/" + "10.jpg"
def generate_filename411(instance, filename):
    return "src/static/img/interior/" + "11.jpg"
def generate_filename412(instance, filename):
    return "src/static/img/interior/" + "12.jpg"
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
	pic10 = models.FileField(upload_to=generate_filename410)
	pic11 = models.FileField(upload_to=generate_filename411)
	pic12 = models.FileField(upload_to=generate_filename412)



def generate_filename51(instance, filename):
    return "src/static/img/building/" + "1.jpg"
def generate_filename52(instance, filename):
    return "src/static/img/building/" + "2.jpg"
def generate_filename53(instance, filename):
    return "src/static/img/building/" + "3.jpg"
def generate_filename54(instance, filename):
    return "src/static/img/building/" + "4.jpg"
def generate_filename55(instance, filename):
    return "src/static/img/building/" + "5.jpg"
def generate_filename56(instance, filename):
    return "src/static/img/building/" + "6.jpg"
def generate_filename57(instance, filename):
    return "src/static/img/building/" + "7.jpg"
def generate_filename58(instance, filename):
    return "src/static/img/building/" + "8.jpg"
def generate_filename59(instance, filename):
    return "src/static/img/building/" + "9.jpg"
def generate_filename510(instance, filename):
    return "src/static/img/building/" + "10.jpg"
def generate_filename511(instance, filename):
    return "src/static/img/building/" + "11.jpg"
def generate_filename512(instance, filename):
    return "src/static/img/building/" + "12.jpg"

class Building(models.Model):
	pic1 = models.FileField(upload_to=generate_filename51)
	pic2 = models.FileField(upload_to=generate_filename52)
	pic3 = models.FileField(upload_to=generate_filename53)
	pic4 = models.FileField(upload_to=generate_filename54)
	pic5 = models.FileField(upload_to=generate_filename55)
	pic6 = models.FileField(upload_to=generate_filename56)
	pic7 = models.FileField(upload_to=generate_filename57)
	pic8 = models.FileField(upload_to=generate_filename58)
	pic9 = models.FileField(upload_to=generate_filename59)
	pic10 = models.FileField(upload_to=generate_filename510)
	pic11 = models.FileField(upload_to=generate_filename511)
	pic12 = models.FileField(upload_to=generate_filename512)





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

class Recent(models.Model):
	recent_works =  models.CharField(max_length = 140)
	def __str__(self):
		return self.recent_works


# def generate_filename(instance, filename):
#     ext = filename.split('.')[-1]
#     return 'blog/static/' + filename


class Post(models.Model):
	title = models.CharField(max_length = 140)
	body = models.TextField()
	date = models.DateTimeField()
	image = models.FileField(upload_to="src/static/")
	pic = models.CharField(max_length = 75, default = "copy name of image")
	def __unicode__(self):
		return self.title




class Client(models.Model):
	c1 =  models.CharField(max_length = 140)
	c2 =  models.CharField(max_length = 140)
	c3 =  models.CharField(max_length = 140)
	c4 =  models.CharField(max_length = 140)
	c5 =  models.CharField(max_length = 140)
	c6 =  models.CharField(max_length = 140)
	c7 =  models.CharField(max_length = 140)
	c8 =  models.CharField(max_length = 140)
	c9 =  models.CharField(max_length = 140)
	c10 =  models.CharField(max_length = 140)
	c11 =  models.CharField(max_length = 140)
	c12 =  models.CharField(max_length = 140)
	c13 =  models.CharField(max_length = 140)
	c14 =  models.CharField(max_length = 140)
	c15 =  models.CharField(max_length = 140)
	c16 =  models.CharField(max_length = 140)
	c17 =  models.CharField(max_length = 140)
	c18 =  models.CharField(max_length = 140)
	c19 =  models.CharField(max_length = 140)
	c20 =  models.CharField(max_length = 140)
	c21 =  models.CharField(max_length = 140)
	c22 =  models.CharField(max_length = 140)
	c23 =  models.CharField(max_length = 140)
	c24 =  models.CharField(max_length = 140)
	def __str__(self):
		return self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.c10,self.c11,self.c12,self.c13,self.c14,self.c15,self.c16,self.c17,self.c18,self.c19,self.c20,self.c21,self.c22,self.c23,self.c24