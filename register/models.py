from django.db import models

# Create your models here.
class Register_model(models.Model):
    # Applicant Detail
    
    Name = models.CharField(max_length=50 , default='0000000')
    Code = models.CharField(max_length=50, default='0000000')
    Designation = models.CharField(max_length=50, default='0000000')
    Gender = models.BooleanField(max_length=50, default='0000000')
    Category = models.CharField(max_length=50, default='0000000')


    # Posting Details
    Unit = models.CharField(max_length=50, default='0000000')
    Place = models.CharField(max_length=50, default='0000000')
    State_Unit = models.CharField(max_length=50, default='0000000')
    Region = models.CharField(max_length=50, default='0000000')

        #e-contact details:

    Mobile = models.CharField(max_length=50, default='0000000')
    Office = models.CharField(max_length=50, default='0000000')
    Residence = models.CharField(max_length=50, default='0000000')
    Email = models.CharField(max_length=50, default='0000000')


# office address
    House = models.CharField(max_length=50, default='0000000')
    Building = models.CharField(max_length=50, default='0000000')
    Flat = models.CharField(max_length=50, default='0000000')
    Street = models.CharField(max_length=50, default='0000000')
    Locality = models.CharField(max_length=50, default='0000000')
    LandMark = models.CharField(max_length=50, default='0000000')
    City = models.CharField(max_length=50, default='0000000')
    State = models.CharField(max_length=50, default='0000000')
    Pin = models.CharField(max_length=50, default='0000000')

# Residence Address: (copy all tabs of office address)


    def __str__(self):
        return self.Email

