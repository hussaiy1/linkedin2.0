import json
import time as t
import sys
from datetime import datetime
from colorama import init, Fore, Back, Style

class messaging(object):
    ##CAN CHANGE BELOW TO FUNCTIONS IF NEEDED, Will need to build out in main.py
    with open('message.json', 'r') as jsonf:
        text = json.load(jsonf)

    connectMsg = text['jobTitle'] + '\n' + text['greeting'] + ' ' + ',\n' + text['msg']
    dateTimeObj = datetime.now()
    print(Fore.YELLOW + '[{}] Message : \n {}'.format(str(dateTimeObj), connectMsg))

    message = input(Fore.BLUE + 'Has Your Message Been Updated? (y/n) ')
    if message == 'y':
        print(Fore.GREEN + 'Starting Process....')
    elif message == 'n':
        print(Fore.RED + 'Exiting... Please Update Message')
        sys.exit()
    


# Test Message
