from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Applicant(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Dealer(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    applicant = models.ForeignKey(Applicant, on_delete=models.DO_NOTHING)