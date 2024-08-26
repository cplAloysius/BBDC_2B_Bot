# BBDC Class 2B Bot
This is a bot that checks for available slots for class 2B motorcycle lessons at BBDC. 

- It refreshes the page at a specified interval and compares the number of lesson slots available to that of the previous refresh
- If there is a change, a telegram message will be sent to you with a screenshot of the current availabilty of lessons

![Telegram bot screenshot example](https://github.com/cplAloysius/BBDC-2B-Bot/blob/main/table.png?raw=true)

### Using the bot
1. Install [chromedriver](https://chromedriver.chromium.org)
2. Enter your BBDC username and password into the code in [main.py](https://github.com/cplAloysius/BBDC-2B-Bot/blob/main/main.py)
3. Get your telegram chat id using [this bot](https://t.me/get_id_bot) and edit the code in main.py appropriately. 
4. Create a telegram bot using Bot Father and enter the bot token in main.py.
5. Run main.py

#

### Notes
You may need to add/remove certain lines depending on your BBDC account. For example, I took class 3 at BBDC prior to taking class 2B. Whenever I login to BBDC, it asks if I want to access my class 3 or class 2B account. The lines of code which handle this selection are from lines 49 to 51. You may modify it to work with your BBDC account.

Since my schedule was not fixed, I did not implement a booking function so that the bot doesn't book lessons that I would be unable to attend. Creating a booking function should be fairly trivial.

I ran this program on my desktop in the background while on Youtube/Netflix/gaming. I would occasionally let it to run while I wasn't home by running the "caffeinate" command on a new terminal window (MacOS). You may wish to do the same or to deploy this onto a free hosting service such as heroku.
