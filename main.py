from jd_user import JdUser
from config import Config
from interface import RushGUI
from log import logger


def sum_two_numbers(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b


if __name__ == '__main__':
    #test
    global_config = Config()
    chenchao = JdUser(global_config)
    chenchao_gui = RushGUI(chenchao)
