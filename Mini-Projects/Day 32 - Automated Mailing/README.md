# Automated Mailing

This mini-project has the basics for automated mailing.

## Happy Birthday Letters.

This script will check in an CSV if there's someone having a birthday today. If anyone is found, it will randomly choose letters and mail to those people.

Letter templates provided by course teacher.

## Motivational Quotes.

This script will randomly choose quotes in a csv and mail them to e-mails in "mail_list.txt". It is possible to make it verify if it is a specific day of the week first before mailing.

Quotes from: https://www.positivityblog.com/

## To keep in mind.

Both folders require a file called "hidden.json", which is a file in the format:
```
{
    "e-mail": "your@email.com",
    "password": "yourpassword",
    "smtp": "smtp.yourEmailsSMTPLink.com"
}
```

Create it with your information for it to work. Some e-mail providers don't allow directly inputting your e-mail and password for programs like these. In those situations, you'll probably have to search up how to do it.

I'd recommend creating a new "dummy" account for this. Make sure to always read and understand scripts before running them, even more when they require this kind of information!

## Suggested way to automate running those scripts.

www.pythonanywhere.com free acounts can run 1 task daily (you can run yours scripts every day in a specific time).

There are limitations though (in 20/07/2022):
1. 100 seconds per day (resets every 24 hours);
2. Only one task;
    - You can probably make calls to many scripts though;
    - This limits all scripts to be called at an specific time.
3. Other limitations that are irrelevant for this project.

## Other ways to automate:

### GitHub actions.

This was the first thing I thought. The problem here is that you'd probably need GitHub Pro to have information such as passwords up and hidden from other users (by making private repositories). This should be used carefully.

### Linux (?).

I think I've seen a linux cmd command that automates running tasks at specific times. I'm not sure how it works though. Also not sure what happens if you computer isn't turned on when the task should be running (maybe it does the task after turning on? maybe it skips that task?). This needs more research.

