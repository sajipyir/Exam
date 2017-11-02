from django.db import models
class  QUESTION(models.Model):
    soal1=models.CharField(max_length=50)
    nomreh1=models.CharField(max_length=10)
    soal2=models.CharField(max_length=50)
    nomreh2=models.CharField(max_length=10)
    soal3=models.CharField(max_length=50)
    nomreh3=models.CharField(max_length=10)
    soal4=models.CharField(max_length=50)
    nomreh4=models.CharField(max_length=10)
    soal5=models.CharField(max_length=50)
    nomreh5=models.CharField(max_length=10)
    soal6=models.CharField(max_length=50)
    nomreh6=models.CharField(max_length=10)
    soal7=models.CharField(max_length=50)
    nomreh7=models.CharField(max_length=10)
    soal8=models.CharField(max_length=50)
    nomreh8=models.CharField(max_length=10)
    soal9=models.CharField(max_length=50)
    nomreh9=models.CharField(max_length=10)
    soal10=models.CharField(max_length=50)
    nomreh10=models.CharField(max_length=10)
    def __unicode__(self):
        return self.soal1+"<br>"+self.nomreh1+"<br>"+self.soal2+"<br>"+self.soal3+"<br>"+self.nomreh3+"<br>"+self.soal4+"<br>"+self.nomreh4+"<br>"+self.soal5+"<br>"+self.nomreh5+"<br>"+self.soal6+"<br>"+self.nomreh6+"<br>"+self.soal7+"<br>"+self.nomreh7+"<br>"+self.soal8+"<br>"+self.nomreh8+"<br>"+self.soal9+"<br>"+self.nomreh9+"<br>"+self.soal10+"<br>"+self.nomreh10+"<br><br>"
class answer(models.Model):
    javab1=models.CharField(max_length=100)
    javab2=models.CharField(max_length=100)
    javab3=models.CharField(max_length=100)
    javab4=models.CharField(max_length=100)
    javab5=models.CharField(max_length=100)
    javab6=models.CharField(max_length=100)
    javab7=models.CharField(max_length=10)
    javab8=models.CharField(max_length=100)
    javab9=models.CharField(max_length=100)
    javab10=models.CharField(max_length=100)
    def __unicode__(self):
        return self.javab1+"<br>"+self.javab2+"<br>"+self.javab3+"<br>"+self.javab4+"<br>"+self.javab4+"<br>"+self.javab5+"<br>"+self.javab6+"<br>"+self.javab7+"<br>"+self.javab8+"<br>"+self.javab9+"<br>"+self.javab10+"<br><br>"
# Create your models here.
