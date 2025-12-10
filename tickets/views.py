from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView, TemplateView
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Session
from .booking_manager import BookingManager
from django.contrib.auth.decorators import login_required



class SessionListView(ListView):
    model = Session
    template_name = 'sessions.html'
    context_object_name = 'sessions'
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()  # исходный QuerySet
    #     print("Sessions:", list(queryset))  # преобразование в список и вывод в консоль
    #     return queryset  # возвращение обратно


@method_decorator(login_required(login_url='/registration/login/'), name='dispatch')
class BookSeatsView(FormView):
    form_class = BookingForm
    template_name = 'book_seats.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        session_id = kwargs.get('pk')
        form = self.form_class(request.POST)

        if form.is_valid():
            manager = BookingManager()
            num_seats = int(form.cleaned_data['num_seats'])

            if manager.reserve_seats(session_id, num_seats):
                return redirect('/successful_booking')
            else:
                error_message = f"Нет достаточного количества свободных мест!"
                return render(request, self.template_name, {'form': form, 'error_message': error_message})

        return super().post(request, *args, **kwargs)



class SuccessfulBookingView(TemplateView):
    template_name = 'successful_booking.html'
