import time
import webbrowser
from datetime import timedelta
import pyautogui as pag
'''The purpose of this program is to provide a fun and simple script to promote better study cycles. The program follows a study interval where 
the user will study for x amount of minutes followed by a study break of x amount of minutes.
They will be asked how long they want their study periods to be (in mins) and how long they want their 
study breaks to be (in mins). They will also be asked to provide a url. This url will automatically be opened up as soon as 
their study period fully elapses. '''


def studyingInterval():
    # Give user the option to go through debrief of how the program works 
    debrief_option = input('Would you like to go through the debrief section to understand how this program works (Y/N)?: ').lower()
    if debrief_option == 'y':
        print('This program is desgined to help you study more efficiently.')
        time.sleep(10)
        print('You will be prompted a duration of study time to input. The more common study time is 25 - 30 min')
        time.sleep(10)
        print('Then you will be prompted to enter the length of your break + a url to any site you would like to spend your break on')
        time.sleep(10)
    # user input for length of session, length of study break, and their desired url destination
    duration = float(input('Please enter (in minutes) the duration of study time: '))
    study_break = float(input('Pleae enter (in minutes) the duration of your break: '))
    url = input('Please enter the link to the youtube video you would like to watch during your breaks: ')

    # the url won't actually open unless user inputs 'https://wwww. with their link. 
    if not url.startswith('https://www.'):
        url = 'https://www.' + url

    end_study_time = time.time() + float((duration * 60))
    # Since we don't want this program to be resource intensive, let's convert minutes to seconds and make program sleep until we get to the desired time
    study_seconds = duration * 60
    while time.time() < end_study_time:
        time.sleep(study_seconds)
    pag.alert(text = f"{duration} min elasped. Time for a break.", title = 'Wohoo!')
    webbrowser.open_new_tab(url)


    # after the browser is open we want to make sure they only break for as long as their study break 
    break_seconds = study_break * 60
    end_break_time = time.time() + float((study_break * 60))
    while time.time() < end_break_time:
        time.sleep(break_seconds)
    pag.alert(text = f"{study_break} min elapsed. Time to get to studying.", title = 'Study time')


studyingInterval()


