# mcstatus-ui
Originally based on https://github.com/Dinnerbone/mcstatus, this adds a more refined finish to the use of the program. @ present, it just saves a log of IP addresses you yourself enter (no features added as of yet to remove them directly in "app"), and pings them. You can do this once, or repeatedly. The choice is yours!

This version is aimed at constantly pinging the server while the app is running, and if players are online, to report that information to you! (Enable Quere when pinging server) 

# Background
This was originally a replit project from a few years ago, and I have since then made a UI for this app several times. I finally decided that enough was enough and that I needed to make a GitHub for it, so I don't have to keep reinventing the wheel every time I want to use this program. This Github is me, redoing this project probably for the 3rd or 5th time now. Each time prior, I manually used a lot of research and development time, but thanks to new tools of the modern age (ChatGPT and API documentation), I was able to create this in an afternoon.  (~4-6 hrs)

Addons took about an additional ~3-4 hrs (logging server data).

# Features
* Menu to select which server to start pinging

<p align="center">
  <img src="https://github.com/NoicTheBrave/mcstatus-ui/blob/main/images/mcstatus-ui_image1.png" alt="Image">
</p>

* Ability to add new servers to the roster
  * Simply press the "Add Server IP" button on the main menu and you will be prompted to enter the IP address (w/ port if required)
<p align="center">
  <img src="https://github.com/NoicTheBrave/mcstatus-ui/blob/main/images/mcstatus-ui_image3.png" alt="Image">
</p>

* The background of the server pop-up you are pinging changes colors depending on the number of people online! The feature helps you determine if someone is online, and how many, at a glance.
  * White = 0 (Default color)
  * Red = 1
  * Orange = 2
  * Yellow = 3
  * Green = 4
  * Blue = 5
  * Purple = 6
  * Cyan = 7
  * Lime Green = 8
  * White = +9
<p align="center">
  <img src="https://github.com/NoicTheBrave/mcstatus-ui/blob/main/images/mcstatus-ui_image4.png" alt="Image">
</p>

* Query Players on Server
  * If the server that you are pinging has query enabled (in server config files, even for basic *java* vanilla servers [idk about bedrock]), then you can query and get the player names of the players actively on the server. Otherwise, you will be met with a message similar to the one shown below, because of this, query is OFF by default. To enable, click the little checkbox under the listed IP address of the server you are pinging, as shown below. 
<p align="center">
  <img src="https://github.com/NoicTheBrave/mcstatus-ui/blob/main/images/mcstatus-ui_image5.png" alt="Image">
</p>

* Remove servers from listings
  * To remove a server from the list, simply open the "iplist.txt" file included in the same directory as the main program
<p align="center">
  <img src="https://github.com/NoicTheBrave/mcstatus-ui/blob/main/images/mcstatus-ui_image2.png" alt="Image">
</p>

# New Update: Logging Server Data
* Ability to log server data (stored in the "logData" folder). Items such as server IP, number of players online, player names, if you enabled query via the UI and more.
  * NOTE: Checking to see if you enabled attempting to Query is important to determine if a query attempt was made and the server returned nothing, or if there was no query attempt made. Checking this variable will tell us what course of action the user took and what settings were enabled/disabled.
* Smart Logging: Data is logged once per second if there is more than one player on the server you are pinging. If there is nobody on the server that you are pinging, in an attempt to save storage on the computer running this program, it will only store data once per minute but still ping the server once per second in the event someone does join. 
* (Basic) Logging (Disabled): Data will be logged once every server ping (Disabled by default - can be enabled in mcstatus-ui.py (search for "if logData_var.get()") 
<p align="center">
  <img src="https://github.com/NoicTheBrave/mcstatus-ui/blob/main/images/mcstatus-ui_image6.png" alt="Image">
</p>
* Note: Window height is known to be big enough for when Server logging is enabled only. At present, if both Enable Query and Enable Player Data Logging are enabled at the same time, you may need to expand the window height. This was done intentionally, since more often than not, servers will have querying off by default. 

# Resources & References (and core-library used)
* [The original Replit I created - NOT included for *reasons*]
   * Also known as the "web version" of the application, this is where I first made the foundational functions of this application. Unfortunately, I cannot develop UI on this (fair enough), and thus this project was born
* https://github.com/Dinnerbone/mcstatus
  * This was the original source and inspiration of the crux of the project :) 
