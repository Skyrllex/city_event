from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from location.models import Location
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
   id_location=models.ForeignKey( 
       Location,
       on_delete=models.PROTECT,
       verbose_name = "Локация"
       )
   

   top  = models.IntegerField(
        verbose_name = "Рейтинг",
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
      ('draft','Черновик'),
      ('later publication','Отложенная публикация'),
      ('publication','Опубликовано'),
      ('archive','Архив'),
   ]
   status = models.CharField(
       verbose_name = "Статус",
       max_length=40,
       choices=status_choices,
       default='draft',
       )
   class Meta:
        verbose_name = "мероприятие"
        verbose_name_plural = "Мероприятия"

   def __str__(self):
        return self.name


class EventImage(models.Model):
   event  = models.ForeignKey(Event, on_delete=models.CASCADE, 
       related_name='images',
       verbose_name = "Мероприятие"
       )
   
   image = models.ImageField(
       upload_to='events/images/',
       verbose_name = "изображения"
       )
   
   b_preview= models.BooleanField(
       default= False,
       verbose_name="Главное изображение",
    )
   

   class Meta:
        verbose_name = "медиафайл"
        verbose_name_plural = "Медиа"


   def __str__(self):
       return f"Изображения для события: {self.event.name}"

        