from django.db import models

# Create your models here.




class patient_data(models.Model):
    patient_id = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    age = models.CharField(max_length=122)
    date_adm = models.CharField(max_length=122)
    diagnosis = models.CharField(max_length=122)
    prescription = models.CharField(max_length=122)
    nok_add = models.CharField(max_length=122)
    hosp_name = models.CharField(max_length=122)
    ward = models.CharField(max_length=122)
    def __str__(self):
        return self.patient_id


class User(models.Model):
    user_name = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    user_type = models.CharField(max_length=122)



class Hospitals(models.Model):
    name = models.CharField(max_length=122)
      

