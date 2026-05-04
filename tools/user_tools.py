from notification.notify import send_notification
def record_user_details(email , name="Name not provided" , notes = "No note provided"):
    send_notification("New User",f"Recording {name} with email {email} and notes {notes}")
    return {"recorded": "ok"}