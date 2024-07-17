import random
import requests
from jd_user import JdUser
from config import Config
from interface import RushGUI
from log import logger


def create_random_word():
    """
    Creates a random English word from a predefined list.
    """
    common_words = [
        'apple', 'banana', 'cherry', 'date', 'elder',
        'fig', 'grape', 'honey', 'iris', 'kiwi',
        'lemon', 'mango', 'nectarine', 'orange', 'peach',
        'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli',
        'vanilla', 'watermelon', 'xigua', 'yuzu', 'zucchini'
    ]
    return random.choice(common_words)


def multiply_two_numbers(a, b):
    """
    Returns the product of two numbers.
    """
    return a * b


def generate_random_chinese_word():
    """
    Generates a random Chinese word (character).
    """
    # A list of common Chinese characters
    chinese_chars = [
        '我', '你', '他', '她', '它', '们', '的', '是', '在', '有',
        '个', '好', '来', '去', '出', '入', '上', '下', '前', '后',
        '左', '右', '大', '小', '多', '少', '高', '低', '长', '短'
    ]
    return random.choice(chinese_chars)


def get_local_temperature():
    """
    Gets the current local temperature using OpenWeatherMap API.
    You need to replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key.
    """
    api_key = 'YOUR_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    
    city_name = 'Beijing'
    country_code = 'CN'
    
    complete_url = f"{base_url}q={city_name},{country_code}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(complete_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data["cod"] != "404":
            current_temperature = data["main"]["temp"]
            return f"The current temperature in {city_name} is {current_temperature}°C"
        else:
            return "City not found"
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    #test
    global_config = Config()
    chenchao = JdUser(global_config)
    chenchao_gui = RushGUI(chenchao)
