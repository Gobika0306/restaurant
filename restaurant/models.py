from django.db import models


# Create your models here.
# In restaurant/models.py

from django.db import models

# class MenuItem(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image=models.ImageField(default=0)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return self.name
    

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('STARTERS', 'Starters'),
        ('MAIN_DISHES', 'Main Dishes'),
        ('DESSERTS', 'Desserts'),
        ('DRINKS', 'Drinks'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name



class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.menu_item.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name}"
