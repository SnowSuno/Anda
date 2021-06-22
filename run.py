import os
import sys

from data.settings import USER_ID, USER_PW, DEVICE_NAME, DEVICE_UUID
from src.main import AndaClient
from src.system.console import Console
from src.system.exception_handler import exception_handler


def run(run_mode):
    bot = AndaClient(DEVICE_NAME, DEVICE_UUID)

    if run_mode == 'deploy':
        bot.loop.set_exception_handler(exception_handler)
    elif run_mode == 'debug':
        pass
    else:
        raise Exception('Not a valid mode')

    bot.run(USER_ID, USER_PW)


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) == 2 else 'debug'
    print('')
    Console.log('Server start')
    run(mode)
    os.execv(sys.executable, ['python'] + sys.argv)
