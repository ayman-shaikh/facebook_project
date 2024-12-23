from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Invoice(models.Model):
    invoice_no = models.CharField(max_length=10, null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=25, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    product_description = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.CharField(max_length=10, null=True, blank=True)
    rate = models.CharField(max_length=10, null=True, blank=True)
    amount = models.CharField(max_length=10, null=True, blank=True)
    #total = models.CharField(max_length=10, null=True, blank=True)
    
    user = models.ForeignKey(User, related_name='create_invoice', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.invoice_no