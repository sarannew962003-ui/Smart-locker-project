1. Database Models (PostgreSQL + Django ORM)
Define models in models.py
2. Dynamic Pricing & Redis Caching
Use django-redis for caching.

Create a utility function to calculate demand multiplier based on time/day.

Cache locker prices in Redis with TTL (e.g., 1 hour).
3. Reservation API (DRF)
GET /api/lockers/ → List available lockers with dynamic pricing.

POST /api/reserve/ → Reserve a locker (lock in Redis for 10 min).
4. Notifications via Firebase
Use pyfcm to send push notifications.

Background task (via Celery or management command) checks for price drops.
5. Logging & Kibana Integration
Use structlog or Python’s logging module with JSON format.



