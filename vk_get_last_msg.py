import vk_api
import time
from datetime import datetime
from time import sleep

session = vk_api.VkApi(
token='YOUR_TOKEN')
vk = session.get_api()


def get_last_msg():
    while True:
        sleep(5)
        messages = session.method("messages.getHistory", {"user_id": '432682913', "offset": 0, "count": 1})
        text = messages['items'][0]['text']
        date = messages['items'][0]['date']

        read = convert_time(date)

        final_time = count_stat(read)

        print(f'текст сообщения: {text}. {final_time}')
def convert_time(date):
    read_time = datetime.fromtimestamp(date)
    return read_time

def count_stat(vk_data):
    date_now = datetime.now()
    delta = date_now - vk_data
    if delta.seconds >= 3600:
        return f'{delta.seconds // 3600} часов назад'
    elif delta.seconds >= 60:
        return f'{delta.seconds % 3600 // 60} минут назад'
    else:
        return f'{delta.seconds} секунд назад'

get_last_msg()
