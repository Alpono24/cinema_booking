# import threading
# from booking_manager import BookingManager
#
# SEMAPHORE = threading.Semaphore(5)  # Ограничиваем количество одновременных бронирований
# BOOKING_MANAGER = BookingManager()
#
# def book_tickets(session_id, seats):
#     SEMAPHORE.acquire()
#     success = BOOKING_MANAGER.reserve_seats(session_id, seats)
#     SEMAPHORE.release()
#     return success






import asyncio
import aiohttp

class AsyncBookingManager:
    async def reserve_seats(self, session_id, seats):
        """Асинхронная функция для резервирования мест"""
        # Эмуляция длительной операции (сетевого запроса, обработки данных)
        await asyncio.sleep(1)
        print(f"Бронируем места {seats} для сессии {session_id}")
        return True

async def book_tickets(session_id, seats):
    """Асинхронная функция для бронирования билетов"""
    manager = AsyncBookingManager()
    success = await manager.reserve_seats(session_id, seats)
    return success

async def main():
    tasks = [
        book_tickets("session1", ["A1"]),
        book_tickets("session2", ["B2"]),
        book_tickets("session3", ["C3"])
    ]
    results = await asyncio.gather(*tasks)
    for i, res in enumerate(results):
        print(f"Сессия {i+1}: {'успешно забронировано' if res else 'неудача'}")

if __name__ == "__main__":
    asyncio.run(main())