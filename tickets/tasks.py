import threading
from booking_manager import BookingManager

SEMAPHORE = threading.Semaphore(5)  # Ограничиваем количество одновременных бронирований
BOOKING_MANAGER = BookingManager()

def book_tickets(session_id, seats):
    SEMAPHORE.acquire()
    success = BOOKING_MANAGER.reserve_seats(session_id, seats)
    SEMAPHORE.release()
    return success
