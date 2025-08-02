from django.db import models
from Traditionalapp.models import Customerlist
from Digitalapp.models import Productlist

class orderlist(models.Model):
    customer = models.ForeignKey(Customerlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Productlist, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
   
    

    def __str__(self):
        return f"{self.customer.name} ordered {self.product.name}"
