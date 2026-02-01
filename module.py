# import pyttsx3
# engine = pyttsx3.init()

# rate = engine.getProperty('rate')
# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

import os

# specify the directory (use '.' for current directory)
directory = "/D"

# list all files and folders
contents = os.listdir(directory)

print("Contents of directory:", directory)
for item in contents:
    print(item)
