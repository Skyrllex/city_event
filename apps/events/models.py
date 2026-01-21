from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#from apps.location.models import Location
#from apps.users.models import Users

class Event(models.Model):
   name = models.CharField(
        verbose_name = "Название мероприятия", 
        max_length=70, 
        #need russian regex
        #validators= [r'^[а-яА-ЯёЁ0-9\s\-\.\,]+$'], 
    )
   
   description = models.CharField(
        verbose_name = "Описание мероприятия", 
        max_length=500, 
    )
   
   #loadimage

   start_date= models.DateTimeField(
        verbose_name = "Дата начала",
        auto_now=True
    )
   
   end_date= models.DateTimeField(
        verbose_name = "Дата завершения",
    )
   
   pub_date= models.DateTimeField(
        verbose_name = "Дата публикации",
    )
   
   author = models.CharField(
        verbose_name = "Автор", 
        max_length=50, 
    )
   #author=models.ForeignKey(Users, on_delete=models.CASCADE)
   #id_location=models.ForeignKey(Location, on_delete=models.CASCADE),
   #mb use SET_NULL

   top  = models.IntegerField(
        verbose_name = "Рейтинг",
        #max_digits=2,
        #decimal_places=0,
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(25)
            ],
        default=1,
        help_text="Рейтинг от 0 до 25",
    )
   
   status_choices=[
      ('draft','черновик'),
      ('later publication','отложенная публикация'),
      ('publication','опубликовано'),
      ('publication','архив'),
   ]
   status = models.CharField(
      max_length=40,

      choices=status_choices,
      default='draft',
   )
   
   def __str__(self):
        return super().__str__()

