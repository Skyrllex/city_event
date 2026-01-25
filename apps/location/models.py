from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Location(models.Model):
    name = models.CharField(
        verbose_name = "Название места", 
        max_length=150, 
    )
    
    coordinateX = models.DecimalField(
        verbose_name = "Широта",
        max_digits=10,
        decimal_places=8,
        validators=[
            MinValueValidator(-90), 
            MaxValueValidator(90)
            ],
        default=0.0,
        help_text= "Широта должна быть от -90.00000000 до 90.00000000"
    )


    coordinateY = models.DecimalField(
        verbose_name = "Долгота",
        max_digits=11,
        decimal_places=8,
        validators=[
            MinValueValidator(-180), 
            MaxValueValidator(180)
            ],
        default=0.0,
        help_text="Долгота должна быть от -180.00000000 до 180.00000000"   
    )
   
    created_at= models.DateTimeField(
        verbose_name = "Дата создания",
        auto_now_add=True
        )
    updates_at= models.DateTimeField(
        verbose_name = "Дата изменения",
        auto_now=True
        )

    class Meta:
        verbose_name = "локацию"
        verbose_name_plural = "Локации"

    @property
    def get_weather_loc(self):
        from weather.services import WeatherService
        return WeatherService.up_weather(self.name)
    
    @property
    def weather(self):
        return self.get_weather_loc()
    
    def __str__(self):
        return self.name
    

