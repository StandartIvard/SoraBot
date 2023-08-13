import vk_api
from TOKENS import VKtoken
import requests
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import json
from io import BytesIO
import random
from vk_api.upload import VkUpload




def main():
    # Авторизация
    vk_session = vk_api.VkApi(token=VKtoken)
    vk_session.api_version = '5.131'
    api = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, '222003478')
    vk = vk_session.get_api()
    upload = VkUpload(vk)

    print('Бот запущен. Ожидаю сообщений...')

    for event in longpoll.listen():
        print(event.type)
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.message['text'])
            if event.message['text'][0:4].lower() == "сора" and "лис" in event.message['text'].lower():
                print("process")

                imgURL = requests.get('https://randomfox.ca/floof/')
                data = json.loads(imgURL.content)

                getimg = requests.get(data['image'])
                getimg = getimg.content

                f = BytesIO(getimg)

                photo = upload.photo_messages(f)[0]

                owner_id = photo['owner_id']
                photo_id = photo['id']
                access_key = photo['access_key']
                attachment = f'photo{owner_id}_{photo_id}_{access_key}'

                api.messages.send(
                    random_id=random.randint(0, 2 ** 64),
                    peer_id=event.message['peer_id'],
                    attachment=attachment
                )

            if event.message['text'][0:4].lower() == "сора" and "аним" in event.message['text'].lower():
                imgURL = requests.get('https://api.waifu.pics/sfw/waifu')
                data = json.loads(imgURL.content)

                getimg = requests.get(data['url'])
                getimg = getimg.content

                f = BytesIO(getimg)

                photo = upload.photo_messages(f)[0]

                owner_id = photo['owner_id']
                photo_id = photo['id']
                access_key = photo['access_key']
                attachment = f'photo{owner_id}_{photo_id}_{access_key}'

                api.messages.send(
                    random_id=random.randint(0, 2 ** 64),
                    peer_id=event.message['peer_id'],
                    attachment=attachment
                )

if __name__ == '__main__':
    main()
