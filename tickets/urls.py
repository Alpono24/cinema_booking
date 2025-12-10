from django.urls import path
from .views import SessionListView, BookSeatsView, SuccessfulBookingView


app_name = 'booking'

urlpatterns = [
    path('', SessionListView.as_view(), name='session_list'),      # Список всех сеансов
    path('book/<int:pk>/', BookSeatsView.as_view(), name='book_seats'),  # Бронирование мест
    path('successful_booking/', SuccessfulBookingView.as_view(), name='successful_booking'),
]
