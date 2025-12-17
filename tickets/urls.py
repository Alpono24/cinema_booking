from django.urls import path
from .views import SessionListView, BookSeatsView, SuccessfulBookingView


app_name = 'booking'

urlpatterns = [
    path('', SessionListView, name='session_list'),      # Список всех сеансов
    path('book/<int:pk>/', BookSeatsView.as_view(), name='book_seats'),  # Бронирование мест
    path('successful_booking/', SuccessfulBookingView, name='successful_booking'),
]
