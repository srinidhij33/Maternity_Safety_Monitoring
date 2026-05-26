from django.db import models

# Create your models here.
class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True,max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status  = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid
    class Meta:
        db_table='Users'



class HeartDataModel(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()
    target = models.IntegerField()
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'HeartDatabase'



class DataModel(models.Model):
    email = models.CharField(max_length=100)
    data1 = models.IntegerField()
    data2 = models.IntegerField()
    data3 = models.IntegerField()
    data4 = models.IntegerField()
    data5 = models.IntegerField()
    data6 = models.IntegerField()
    pred = models.IntegerField()
    
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'dataDatabase'