from models import db, UserActivity
def log_user_activity(user_id, activity, ipadress):
    user_activity = UserActivity(user_id=user_id, activity=activity, ipaddress=ipadress)
    db.session.add(user_activity)
    db.session.commit()