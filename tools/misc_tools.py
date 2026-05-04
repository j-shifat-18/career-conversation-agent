from notification.notify import send_notification

def record_unknown_question(question):
    send_notification("New question " ,f"Recording unknown details: {question}")
    return {"recorded": "ok"}
