from jd_user import JdUser
from config import Config
from interface import RushGUI
from log import logger


def addtwonum(a, b):
    """
    Calculate the sum of two numbers.
    
    Args:
    a (int or float): The first number
    b (int or float): The second number
    
    Returns:
    int or float: The sum of a and b
    """
    return a + b


if __name__ == '__main__':
    #test
    global_config = Config()
    chenchao = JdUser(global_config)
    chenchao_gui = RushGUI(chenchao)

