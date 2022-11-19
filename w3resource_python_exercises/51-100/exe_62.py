import os
import pyttsx3

engine = pyttsx3.init()

seconds_of_days = int(input("Input days: ")) * 3600 * 24
seconds_of_hours = int(input("Input hours: ")) * 3600
seconds_of_minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

full_seconds = seconds_of_days + seconds_of_hours + seconds_of_minutes + seconds

print(f'The amounts of seconds: {full_seconds:,}')
int = 1_000
#engine.say(int)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(full_seconds)
engine.runAndWait()
engine.stop()
