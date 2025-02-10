from django.db import models

class Car(models.Model):
    TYPE_CHOICES = [
        ('supercar', 'Суперкари'),
        ('classic', 'Класичні'),
        ('electric', 'Електро'),
        ('race', 'Гоночні'),
    ]

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    image = models.URLField()
    car_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='supercar')  # ✅ Тип авто

    def __str__(self):
        return f"{self.brand} {self.model}"
