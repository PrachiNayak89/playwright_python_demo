# This file will hold all the common data for tests
import random
import string
from playwright.sync_api import Page as page


def get_random_word(length=3):
    uppercase = string.ascii_uppercase
    return ''.join([random.choice(uppercase[:length]) for _ in range(length)])


def get_random_number(length=3):
    numbers = string.digits
    return ''.join([random.choice(numbers[:length]) for _ in range(length)])


def generate_random_name():
    name = f'AUTO_TEST_{get_random_word()}'
    return name


def generate_random_email(name):
    domain = "autotest.com"
    email = f'{name}@{domain}'
    return email


def generate_random_password():
    name = f'TEST_{get_random_word()}@{get_random_number()}'
    return name


def generate_random_title():
    title = f'AUTO_TEST_ticket_{get_random_word(length=5)}'
    return title


def generate_random_description():
    description = f'AUTO_TEST_ticket_{get_random_word(length=10)}'
    return description
