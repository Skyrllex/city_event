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
    )
   
   end_date= models.DateTimeField(
        verbose_name = "Дата завершения",
    )
   

   author = models.CharField(
        verbose_name = "Автор", 
        max_length=50, 
    )
   #author=models.ForeignKey(Users, on_delete=models.SET_NULL)
   #id_location=models.ForeignKey(Location, on_delete=models.SET_NULL,
   

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
   
   pub_date= models.DateTimeField(
        verbose_name = "Дата публикации",
    )
   
   status_choices=[
      ('draft','черновик'),
      ('later publication','отложенная публикация'),
      ('publication','опубликовано'),
      ('archive','архив'),
   ]
   status = models.CharField(
      max_length=40,

      choices=status_choices,
      default='draft',
   )
   class Meta:
        verbose_name = "мероприятие"
        verbose_name_plural = "Мероприятия"

   def __str__(self):
        return super().__str__()

#easy image test
class EventImage(models.Model):
   event  =models.ForeignKey(Event, on_delete=models.CASCADE, 
       related_name='images',
       verbose_name = "Мероприятие"
       )
   
   image = models.ImageField(
       upload_to='events/images/',
       verbose_name = "изображения"
       )
   
   class Meta:
        verbose_name = "Медиа"
        verbose_name_plural = "Изображения"

   def __str__(self):
       return f"Изображения для {self.event.name}"