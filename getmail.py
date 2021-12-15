import pyperclip, pyautogui as bot
from funciones import locate_image, telegram_report
from time import sleep

def get_mail():

    if locate_image('profile'):

        profile_location = locate_image('account_mail', move=False, click=False, wait=1)[1]

        bot.moveTo(profile_location[0]+80, profile_location[1]+30)
        sleep(0.20)
        bot.tripleClick(interval=0.02)
        bot.hotkey('ctrl', 'c')
        data = f"Desde: {pyperclip.paste()}"
        sleep(1)
        bot.click()
        
        telegram_report(f"{data}", '2112636737')

        
        return data


get_mail()

