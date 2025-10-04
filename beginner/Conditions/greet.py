import time

hour = time.localtime().tm_hour

if hour < 12:
    greeting = "Good morning lovely"
elif hour < 17:
    greeting = "Good Afternoon Dear"
elif hour < 20:
    greeting = "Good evening sweetheart"
else:
    greeting = "Good Night Darling"

#idhu summa extra 

name = input("Enter your name: "). strip()
if name:
    print(f"{greeting}, {name}!")
else:
    print(greeting + "!")