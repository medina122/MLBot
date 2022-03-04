from pybot_modificado import locate_image
from time import sleep

def windscribe():
    locate_image('windscribe')
    sleep(0.5)
    if locate_image('windscribe_status_off', move=False, click=False) != (None):
        print("Turning ON")
        sleep(1)
        locate_image('windscribe_turn_on')
        locate_image('windscribe_status_on', move=False, click=False, check=True, wait=1, end=1)
        print('Finished option 1')
    elif locate_image('windscribe_status_on', move=False, click=False) != (None):
        print("Changing IP Address")
        locate_image('windscribe_turn_off')
        locate_image('windscribe_status_off', move=False, click=False, check=True)
        sleep(3)
        locate_image('windscribe_turn_on')
        locate_image('windscribe_status_on', move=False, click=False, check=True, wait=1, end=1)
        print('Finished option 2')                                                      
    else: print('Something went wrong at Windscribe Code')
    print('Done')

windscribe()
print('Windscribe Script has finished')