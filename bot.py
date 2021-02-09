from random import random
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_session = VkApi(token="8b92dfdc7dd1ae78707ba61d4554125ebb47c5590b7a5e3a05f1d8cfe11380509e511cbc29c1e0641daf1")
longpoll = VkBotLongPoll(vk_session, "194815411")
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:# and event.from_chat:
        if event.message['text'] == '1':
            random_id = round(random() * 10 ** 9)
            chat_id = int(event.chat_id)
            message = "[Ваш ответ]"

            vk.messages.send(
                random_id=random_id,
                chat_id=chat_id,
                message=message,
            )
