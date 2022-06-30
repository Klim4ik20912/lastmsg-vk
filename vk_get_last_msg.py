import vk_api
import time
from datetime import datetime

session = vk_api.VkApi(token='vk1.a.4Z7mTLe4fM8mywUao0UjrpR3nAbz7oUSDxaEBc06pRZwXweB3xvkcGJnjNrcybrAD6lL5UwwTJ9Ig7dt8vg4Z-R584Oe5fN-mE2kIWgjbuMWvyj4j_ST0SsQk9qLt3y4mVv8qdsDSOnq9J4mQaQxDqoGUnDAi61sICTTphtnH5InRaco1KZNYfTMH7FLgDNW')
vk = session.get_api()
 
def get_last_msg():
    messages = session.method("messages.getHistory", {"user_id": '454121835', "offset": 0, "count": 1})
    text = messages['items'][0]['text']
    date = messages['items'][0]['date']

    read = convert_time(date)
    print(f'msg_text: {text}. msg date: {read}')
    
def convert_time(date):
    read_time = datetime.fromtimestamp(date)
    return read_time

get_last_msg()
