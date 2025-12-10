from django.db import models

# Создадаю две основные модели:
# Cinema (кинотеатр) и Session (сеанс фильма).
# Каждая модель будет хранить соответствующую информацию.

# Модель "Кинотеатр"
class Cinema(models.Model):
    name = models.CharField(max_length=100) # Имя кинотеатра
    address = models.TextField() # Адрес кинотеатра

    def __str__(self):
        return self.name

# Модель "Сеанс_Фильма"
class Session(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    title = models.CharField(max_length=100) # Название фильма
    date_time = models.DateTimeField()  # Дата и время начала фильма
    total_seats = models.PositiveIntegerField() # Количество мест в зале
    booked_seats = models.PositiveIntegerField(default=0) # Количество забронированных мест

    def __str__(self):
        return f'{self.title} at {self.cinema}, {self.date_time}'

    class Meta:
        ordering = ['date_time'] # Сортируем по полю даты

