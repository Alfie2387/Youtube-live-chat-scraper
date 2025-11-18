import pytchat
from datetime import datetime

# Generate filename
date_str = datetime.now().strftime("%Y-%m-%d")
LOGFILE = f"{date_str} chat data.txt"

# You have to set the stream URL yourself
# Steps on how to get the video ID
# Step 1: get your stream URL - For example "https://www.youtube.com/watch?v=weySwPr3PKY"
# Step 2: Extract the ID from the URL "https://www.youtube.com/watch?v=  weySwPr3PKY  <-- Here is the ID (it follows the ?=)
# Step 3: Input your ID below
stream = pytchat.create(video_id="VIDEO ID GOES HERE")

# list of users (only relevant for example 1)
#known_users = set()

with open(LOGFILE, "a", encoding="utf-8") as f:
    while True:
        data = stream.get()
        items = data.items
        for c in items:
            msg = f"{c.datetime}\t{c.author.name}\t{c.message}"
            # You can decide what data is printed and logged
            # The Variables are self-explanatory remove or alter them however you wish
            print(msg)
            f.write(msg + "\n")
            f.flush()
## This section will scrape and log the chat data - The rest of the file is optional interactivity for streamers


# These are examples of ways you can use the data for interactivity

            # Example 1: Welcome new chatters using Text-to-Speech (TTS)
            # if c.author.name not in known_users:
            #     import pyttsx3
            #     tts = pyttsx3.init()
            #     tts.say(f"Welcome to the stream, {c.author.name}!")
            #     tts.runAndWait()
            #     known_users.add(c.author.name)

            # Example 2: Keyword detection (e.g. someone says “hello”)
            # if "hello" in c.message.lower():
            #     print("Keyword detected: viewer said hello")
            #     # Example action: Play a sound or trigger some event
            #     # import winsound
            #     # winsound.Beep(800, 300)

            # Example 3: Trigger a mouse input from chat command
            # if c.message.lower().strip() == "left click":
            #     print("Viewer requested left click")
            #     # Example action: perform a mouse left click
            #     # import pyautogui
            #     # pyautogui.click()

            #     # You can add more commands:
            #     # if c.message.lower().strip() == "right click":
            #     #     pyautogui.rightClick()

            #     # if c.message.lower().strip() == "space":
            #     #     pyautogui.press("space")