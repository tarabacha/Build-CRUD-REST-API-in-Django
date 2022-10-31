from django.db import models

# Create your models here.
# must do it in order.

batch Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    
    def __str__():
        return "employee_table"
