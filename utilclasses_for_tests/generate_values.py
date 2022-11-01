import string
import random


class GenerateRandomValue:

    @staticmethod
    def generate_text(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    @staticmethod
    def generate_int_number(start, end):
        num = random.randint(start, end)
        return num

