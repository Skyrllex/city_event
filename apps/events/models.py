from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from location.models import Location
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.files.base import ContentFile
#from users.models import Users

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
   

   author=models.ForeignKey( 
       User,
       on_delete=models.PROTECT,
       verbose_name = "Автор",
    )

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
   
   def save(self, *args, **kwargs):
       
       super().save(*args, **kwargs)
       if self.b_preview:
        EventImage.objects.filter(
            event=self.event,
            b_preview = True
            ).exclude(pk=self.pk).update(b_preview=False)
        self.image_preview
   
   def image_preview(self):
        img = Image.open(self.image.path)
        weight, height= img.size
        if weight<height:
            preview_height = 200
            preview_weight = int ((weight/height)*200)
        else:
            preview_height = int ((height/weight)*200)
            preview_weight = 200
        img= img.resize((preview_weight,preview_height))

        img_bytes = BytesIO()
        img.save(fp=img_bytes, format="WEBP", quality=100)

        image_content_file = ContentFile(content=img_bytes.getvalue())
        name = self.image.name.split('.')[0] + '.WEBP'

        new_image = File(image_content_file, name=name)
        return new_image
       
        