from datetime import datetime

class Console:
    @classmethod
    def log(cls, log_msg):
        print(f'{cls.current_timestamp()} {log_msg}')

    @staticmethod
    def current_timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

