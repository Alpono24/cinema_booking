from django.db import transaction
from .models import Session, BookedTicket


class BookingManager:
    def reserve_seats(self, session_id, seat_numbers, user):
        with transaction.atomic():
            session = Session.objects.select_for_update().get(pk=session_id)
            available_seats = session.available_seats()
            required_seats = len(seat_numbers)

            print(f"Available Seats: {available_seats}, Requested Seats: {required_seats}")

            if available_seats >= required_seats:
                new_tickets = [
                    BookedTicket(session=session, user=user, seat_number=int(seat_number))
                    for seat_number in seat_numbers
                ]

                print(f"New Tickets: {new_tickets}")

                try:
                    BookedTicket.objects.bulk_create(new_tickets)
                    print("Tickets created!")
                    return True
                except Exception as e:
                    print(f"Error creating tickets: {e}")
                    raise e
            else:
                return False