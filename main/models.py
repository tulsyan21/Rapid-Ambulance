from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=256)
    available_beds = models.PositiveIntegerField()
    crowd = models.PositiveIntegerField(null = True , blank = True)
    departments = models.ManyToManyField('Department')
    is_private = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name