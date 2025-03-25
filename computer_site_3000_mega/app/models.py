from django.db import models

class catalog(models.Model):
  photo = models.ImageField('Фото товара', upload_to='photo/%Y/%m/%d')
  name = models.CharField('Название товара', max_length=100)
  price = models.IntegerField('Цена')
  date = models.DateField('Дата', auto_now_add=True)
  
  def __str__(self):
    return self.name
  
