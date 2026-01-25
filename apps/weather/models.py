from django.db import models

class Weather(models.Model):
    weather_key =models.CharField(max_length=100)

    temperature= models.FloatField(
      verbose_name = "Температура ℃", 
      )
    humidity= models.IntegerField(
      verbose_name = "Влажность %", 
      )
    pressure= models.IntegerField(
      verbose_name = "Атмосферное давление, mmHg", 
      )
    wind_speed= models.FloatField(
      verbose_name = "Скорость ветра, , m/s", 
      )
    wind_direction = models.CharField(
        verbose_name = "Направления ветра", 
        max_length=10, 
        )
    up_date= models.DateTimeField(
        verbose_name = "Дата обновления",
        auto_now=True,
        )
    source_url= models.CharField(
        verbose_name = "Агент погоды", 
        max_length=200, 
        ) 
    class Meta:
        verbose_name = "погода"
        verbose_name_plural = "Погода"

    def __str__(self):

        return self.weather_key