from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=150)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    color_options = [
        ('R', 'Red'),
        ('O', 'Orange'),
        ('Y', 'Yellow'),
        ('G', 'Green'),
        ('B', 'Blue'),
        ('I', 'Indigo'),
        ('V', 'Violet'),
        ('W', 'White'),
        ('B', 'Black'),

    ]
    color_name = models.CharField(
        max_length=15,
        choices=color_options,
        blank=False
    )

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
    color = models.ForeignKey(
        ShoeColor,
        on_delete=models.CASCADE,
    )
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(
        ShoeType,
        on_delete=models.CASCADE
    )
    fasten_type = models.CharField(max_length=50)
