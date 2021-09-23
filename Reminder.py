import os
import keyboard
from mutagen.mp3 import MP3
import time
import datetime
import colorama
import pygame
import re


pygame.init()
speaker = pygame.mixer.music
now = datetime.datetime.now

__all__ = []

class Reminder:
    def __init__(self,
                 alert_time: str, routine: list = [now().strftime("%A")],
                 name: str = "", color:str = "BLACK",
                 ringtone: str = "ringtone 1", volume: float = 0.030,
                 snooze: bool = True, snooze_delay: str = None,
                 dismiss_key: str = "esc", active: bool = True):

        try:
            time.strptime(alert_time, '%H:%M')
            self.alert_time = alert_time
        except ValueError:
            raise self.Exceptions.AlertTimeNotInPattern("The alert time provided is not a time pattern")

        self.name = name
        self.routine = routine

        # Default Variables
        self.ringtone = ringtone
        if f"{self.ringtone}.mp3" not in os.listdir("ringtones/"):
            raise self.Exceptions.RingtoneNotFound(f"No ringtone named '{self.ringtone}.mp3'")

        self.volume = volume
        self.snooze = snooze
        self.snooze_delay = snooze_delay
        self.dismiss_key = dismiss_key
        if color.upper() not in colorama.Fore.__dict__:
            raise self.Exceptions.ColorNotFound("Unknown color\\The color specified is not supported")
        else:
            self.color = color.upper()
        
        self.active = active
        self.id = len(__all__) + 1
        
        __all__.append(self)

    def __repr__(self):
        return f"""Reminder(alert-time: {self.alert_time}, ringtone: {self.ringtone}.mp3, snooze: {self.snooze}, snooze-delay: {self.snooze_delay})"""

    def __str__(self):
        return f"""Reminder(alert-time: {self.alert_time}, ringtone: {self.ringtone}.mp3, snooze: {self.snooze}, snooze-delay: {self.snooze_delay})"""

    def alert(self):
        # print(f"{self.alert_name} was alerted!")
        audio = MP3(f"ringtones/{self.ringtone}.mp3")
        try:
            speaker.load(f"ringtones/{self.ringtone}.mp3")
            speaker.set_volume(self.volume)
            while not keyboard.is_pressed(self.dismiss_key):
                print("\033[1m" + colorama.Fore.__dict__[self.color] + f"{self.name}: {now().strftime('%H:%M:%S')}" + colorama.Fore.RESET)
                speaker.play(loops=0)
                time.sleep(audio.info.length + 2)
            speaker.stop()
        except pygame.error:
            raise self.Exceptions.PygameError("PAn error was occurred in the pygame library")

    def dismiss(self):
        pass  #TODO create the dismiss function wich dismisses an active alert
    
    def snooze(self):
        pass  #TODO create the snooze function wich activates a snooze timeout based on the reminder snooze properties

    class Exceptions:
        class RingtoneNotFound(Exception): pass
        class PygameError(Exception): pass
        class ColorNotFound(Exception): pass
        class AlertTimeNotInPattern(Exception): pass


#COMMENT --TESTING--

def test():
    # code to test on __main__ run

    reminder = Reminder(
        alert_time="none for now",
        alert_name="Wake Up!",
        ringtone="ringtone 2",
        dismiss_key="esc",
        color="cyan"
    )

    reminder.alert()
    print("hello")
    pass


if __name__ == "__main__":
    test()
