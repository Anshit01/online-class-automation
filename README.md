# Online Class Automation

<p>
This application provides desktop notifications about classes and opens their meet links in browser automatically at the start of the class.
</p>

It works both in windows and linux. But runs better in linux when used with cron.

## Code Overview
- **class-data.json:**
    Stores the timetable in simple json format. Specify the name and meet link of classes with their timings according to your timetable. The time of a class is specified by day and hour. Day ranges from 0 for Monday to 6 for Sunday. And hour ranges from 0 to 23.

- **main.py:**
    It loads the timetable and checks if there is a class now. In case there is a class it shows a desktop notification with sound and then opens its meet link in the browser.

    Creating a cron job to run this file at the start of every hour is enough to achieve the goal of this program.

- **scheduler.py:**
    This is a custom scheduler which may be used in case cron is not available (in case of windows).

## Installation

-   Install the dependencies

        pipenv install --system

-   In case of windows, also install win10toast

        pip install win10toast

-   The class-data.json file by default has 2nd year CSE B.Tech timetable. Edit this as per your timetable.
-   The last step is setting up the scheduler. **Follow one of the following methods.**

### Using Cron

This methods works in linux and macOS.

-   Run this command to setup cron job

        crontab -e

-   If this is the first time you are setting a cron job, you'll be prompted to select an editor. Choose nano to keep it simple.

-   At the end of file that opens, append this line

        1 * * * * export DISPLAY=:0; XDG_RUNTIME_DIR=/run/user/$(id -u) cd ~/<path-to-this-project>/online-class-automation && python3 main.py

    This command is run at <code>:01</code> every hour.

    Make sure to change the _&lt;path-to-this-project&gt;_

    You may add _<code>>>debug.log 2>&1</code>_ at the end of this line to create a log file to keep log of this programs activity.

### Set as startup app for windows

-   Create a shortcut of <code>start-class-scheduler.bat</code>

-   Open the startup apps folder. Press <code>Windows logo key + R</code>, then enter <code>shell:startup</code> to open it.

-   Move the shortcut of <code>start-class-scheduler.bat</code> to the startup apps folder.

This method will keep a command prompt window always open, which may be annoying :/

You may explore others methods such as Windows Task Scheduler or creating a background process. All you need to do is run the this command at startup.

    python scheduler.py

## Contributing to this project
This is a simple project. It can be easily customized to perform other scheduling tasks with minor changes in code.

If you have any query regarding this project, or want to add any feature to it, feel free to open an issue.
