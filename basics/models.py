from django.db import models

# Create your models here.


class PersonDetails(models.Model):
    PER_NAME=models.CharField(max_length=1000)
    PER_PHONENO=models.CharField(max_length=1000)
    PER_EMAIL=models.CharField(max_length=1000)
    PER_ADDRESS=models.CharField(max_length=1000)
    PER_DOB=models.CharField(max_length=1000)
    PER_BLOODGROUPNAME=models.CharField(max_length=1000)


class BloodGroup(models.Model):
    BLOOD_GROUPNAME=models.CharField(max_length=1000)
    BLOOD_GROUPDESC=models.CharField(max_length=1000)


class DonateBlood(models.Model):
    DONOR_NAME=models.CharField(max_length=1000)
    DONOR_BLOODGROUPNAME=models.CharField(max_length=1000)
    DONOR_DATE=models.CharField(max_length=1000)
    DONOR_QTY=models.CharField(max_length=1000)


