from django.db import transaction
from django.db.models import F
from .models import Session


class BookingManager:
    def __init__(self):
        pass  # Оставляем конструктор пустым, так как он нам не нужен

    def reserve_seats(self, session_id, num_seats):
        """
        Резервирует указанное число мест для заданного сеанса.
        :param session_id: Идентификатор сеанса
        :param num_seats: Количество мест для резервирования
        :return: True, если резервирование прошло успешно, False иначе
        """
        with transaction.atomic():  # Начало атомарной транзакции
            session = Session.objects.select_for_update().get(pk=session_id)

            # Рассчитываем оставшееся количество мест
            remaining_seats = session.total_seats - session.booked_seats

            # Проверяем, достаточно ли мест
            if remaining_seats >= num_seats:
                # Атомарно увеличиваем количество забронированных мест
                Session.objects.filter(id=session_id).update(booked_seats=F('booked_seats') + num_seats)

                # Обновляем состояние объекта после обновления
                session.refresh_from_db(fields=["booked_seats"])
                return True
            else:
                return False