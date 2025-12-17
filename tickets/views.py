from django.template.defaultfilters import title
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Session, Cinema, BookedTicket
from .booking_manager import BookingManager
from django.contrib.auth.decorators import login_required

# class SessionListView(ListView):
#     model = Session
#     template_name = 'sessions.html'
#
#     context_object_name = 'sessions'


def SessionListView(request):
    title: str = "Доступные сеансы"
    sessions = Session.objects.all()
    cinema = Cinema.objects.all()
    return render(request, 'sessions.html', {
        'title': title,
        'sessions': sessions,
        'cinema': cinema
    })



# class SuccessfulBookingView(TemplateView):
#     template_name = 'successful_booking.html'


def SuccessfulBookingView(request):
    title: str = "Информация о брони"
    sessions = Session.objects.all()
    cinema = Cinema.objects.all()
    booked_tickets = BookedTicket.objects.filter(user=request.user)
    return render(request, 'successful_booking.html', {
        'title': title,
        'sessions': sessions,
        'cinema': cinema,
        'tickets': booked_tickets
    })

@method_decorator(login_required(login_url='/registration/login/'), name='dispatch')
class BookSeatsView(FormView):
    form_class = BookingForm
    template_name = 'book_seats.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_id = self.kwargs.get('pk')
        session = get_object_or_404(Session, pk=session_id)
        context['session'] = session

        # Генерация списка свободных мест
        taken_seats = set(session.bookedticket_set.values_list('seat_number', flat=True))
        all_seats = range(1, session.total_seats + 1)
        free_seats = sorted(set(all_seats) - taken_seats)
        context['free_seats'] = free_seats

        return context

    def post(self, request, *args, **kwargs):
        session_id = kwargs.get('pk')
        form = self.form_class(data=request.POST, free_seats=self.get_context_data()['free_seats'])

        if form.is_valid():
            seat_numbers = form.cleaned_data['selected_seats']
            user = request.user

            print(f"Selected Seats: {seat_numbers}, User: {user.username}, Session ID: {session_id}")

            manager = BookingManager()
            if manager.reserve_seats(session_id, seat_numbers, user):
                return redirect('booking:successful_booking')
            else:
                error_message = f"Недостаточно свободных мест."
                return render(request, self.template_name, {'form': form, 'error_message': error_message})
        else:
            print(form.errors.as_json())
            return super().post(request, *args, **kwargs)