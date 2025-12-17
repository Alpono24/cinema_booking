from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator


# Кинотеатр
class Cinema(models.Model):
    name = models.CharField(max_length=100)  # Название кинотеатра
    address = models.TextField()  # Адрес кинотеатра
    image = models.ImageField(upload_to='cinemas/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])

    def __str__(self):
        return self.name


# Сеанс фильма
class Session(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # Название фильма
    description = models.TextField(blank=True, null=True)  # Описание фильма (необязательно)
    poster = models.ImageField(upload_to='movies/', blank=True, null=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])  # Постер фильма
    date_time = models.DateTimeField()  # Дата и время показа
    total_seats = models.PositiveIntegerField()  # Общее число мест в зале

    def available_seats(self):
        """Возвращает доступное количество мест"""
        booked_tickets_count = self.bookedticket_set.count()
        return max(0, self.total_seats - booked_tickets_count)

    def __str__(self):
        return f"{self.title} ({self.date_time.strftime('%Y-%m-%d %H:%M')})"

    class Meta:
        ordering = ["date_time"]  # сортировка по дате


# Бронирование билета
class BookedTicket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()

    def __str__(self):
        return f"Билет на '{self.session.title}', кресло №{self.seat_number}"

    class Meta:
        unique_together = ("session", "seat_number")