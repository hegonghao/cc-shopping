import random
from jd_user import JdUser
from config import Config
from interface import RushGUI
from log import logger


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


if __name__ == '__main__':
    #test
    global_config = Config()
    chenchao = JdUser(global_config)
    chenchao_gui = RushGUI(chenchao)
