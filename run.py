import os
import sys

from data.settings import USER_ID, USER_PW, DEVICE_NAME, DEVICE_UUID
from src.main import AndaClient
from src.system.console import Console
from src.system.exception_handler import exception_handler

DEBUG = True

def run():
    bot = AndaClient(DEVICE_NAME, DEVICE_UUID)

    if not DEBUG:
        bot.loop.set_exception_handler(exception_handler)

    bot.run(USER_ID, USER_PW)


if __name__ == '__main__':
    print('')
    Console.log('Server start')
    run()
    os.execv(sys.executable, ['python'] + sys.argv)
