from src.main import AndaClient
from data.private import KAKAO_ID, KAKAO_PW, DEVICE_NAME, DEVICE_UUID
from src.system.exception_handler import exception_handler


if __name__ == '__main__':
    bot = AndaClient(DEVICE_NAME, DEVICE_UUID)
    bot.loop.set_exception_handler(exception_handler)
    bot.run(KAKAO_ID, KAKAO_PW)
