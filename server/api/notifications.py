import os
import shutil
import time

from filelock import FileLock
from tinydb import TinyDB


def latest_notifications(user_id, n):
    """Load latest n notification"""
    notifications_path = os.path.join(os.environ["CACHE_PATH"], "NOTIFICATIONS", user_id, f"notifications.json")
    if not os.path.exists(notifications_path):
        return []

    with FileLock(f"{notifications_path}.lock"):
        with TinyDB(notifications_path) as db:
            od = sorted(db.all(), key=lambda k: k['time'])[n*(-1):]
            return od


def notify(user_id, type_, msg, extra=None):
    """Store a notification for a certain user"""
    notifications_path = os.path.join(os.environ["CACHE_PATH"], "NOTIFICATIONS", user_id)
    if not os.path.exists(notifications_path):
        os.makedirs(notifications_path, exist_ok=True)

    clean_notifications_store(user_id)
    notifications_path = os.path.join(notifications_path, f"notifications.json")
    with FileLock(f"{notifications_path}.lock"):
        with TinyDB(notifications_path) as db:
            db.insert({
                "time": int(time.time()),
                "type": type_,
                "message": msg,
                "extra": extra
            })


def notify_all(users, type_, msg, extra=None):
    """Store a notification for a list of user"""
    for user in users:
        notify(user, type_, msg, extra=extra)


def clean_notifications_store(user_id):
    """
        Make sure that the notification store does not hold more than 30 notifications at most
        A new store will be created with 3 notifications padding from the last one
    """
    notifications_path = os.path.join(os.environ["CACHE_PATH"], "NOTIFICATIONS", user_id, f"notifications.json")
    with FileLock(f"{notifications_path}.lock"):
        with TinyDB(notifications_path) as db:
            size = len(db)
            if size < 30:
                return None
            else:
                shutil.copyfile(
                    notifications_path,
                    os.path.join(os.environ["CACHE_PATH"], "NOTIFICATIONS", user_id,
                                 f"notifications_{int(time.time())}.json")
                )
                od = sorted(db.all(), key=lambda k: k['time'])[-3:]
                db.truncate()
                db.insert_multiple(od)


if __name__ == "__main__":
    os.environ["CACHE_PATH"] = r"C:\Users\medzi\Desktop\bnp\s3-browser\cache"
    import uuid
    for i in range(31):
        notify("e63551", "normal", f"Your requested file is ready",extra=str(uuid.uuid4().hex))
