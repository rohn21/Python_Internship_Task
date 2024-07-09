from django.db import models
from django.core.validators import EmailValidator

GENDER_CHOICES = {
    'M': 'Male',
    'F': 'Female',
    'NA': 'Not Specified',
}

class UserData(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(validators=[EmailValidator(message="Invalid email address")])
    Gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    Phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name