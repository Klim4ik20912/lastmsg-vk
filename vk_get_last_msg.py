import vk_api
import time
from datetime import datetime

session = vk_api.VkApi(token='YOUR_TOKEN')
vk = session.get_api()
 
def get_last_msg():
    messages = session.method("messages.getHistory", {"user_id": '454121835', "offset": 1, "count": 1})
    text = messages['items'][0]['text']
    date = messages['items'][0]['date']

    read = convert_time(date)
    print(f'msg_text: {text}. msg date: {read}')
    
def convert_time(date):
    read_time = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
    return read_time

get_last_msg()