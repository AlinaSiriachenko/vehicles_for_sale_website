from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField('Марка', max_length=50)
    description = models.TextField('Описание', max_length=1000)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("main:manufacturer_detail", args=(self.id,))

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'



class Car(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    img = models.ImageField(null=True, blank=True, upload_to='cars/')
    views = models.IntegerField(default=0)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:car_detail", args=(self.id,))

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машин(ы)'
