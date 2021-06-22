from KakaoBot.kakaopy.client import Client

class AndaClient(Client):
    async def on_message(self, chat):
        if chat.message.startswith('안다'):
            await chat.send_text('안다가 곧 부활합니당!!')
