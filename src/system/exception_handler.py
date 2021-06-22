from src.system.console import Console
from pprint import pformat


def exception_handler(loop, context):
    exception = context.get('exception')
    if isinstance(exception, ConnectionResetError):
        Console.log('Connection reset')
        loop.stop()

    elif isinstance(exception, Exception):
        error_log = f'Undefined error\n{pformat(context)}'
        Console.log(error_log)
        loop.stop()
