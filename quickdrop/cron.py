from django.utils import timezone
from .models import TempNote

def cleanup_expired_notes():
    now = timezone.now()
    expired = TempNote.objects.filter(expires_at__lte=now)
    count = expired.count()
    expired.delete()
    print(f"[{now}] Cron deleted {count} expired note(s).")