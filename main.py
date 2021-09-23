import Reminder
import datetime
from win10toast import ToastNotifier

toaster = ToastNotifier()
now = datetime.datetime.now

r = Reminder.Reminder(alert_time="16:52", name="A TEST REMINDER!", color="green")


while True:
    current_time = datetime.datetime.now().strftime("%H:%M")
    for reminder in Reminder.__all__:
        time_to_alert = (
            current_time == reminder.alert_time and 
            reminder.active is True and
            now().strftime("%A") in reminder.routine
            )

        if time_to_alert:
            toaster.show_toast("Sample Notification","Python is awesome!!!")
            reminder.alert()
