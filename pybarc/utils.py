import random
from pybarc.constants import EAN_WEIGHTS


def ean_18_checksum(value):
    return sum(x*y for x, y in zip(EAN_WEIGHTS, value[:-1]))

def ean_13_checksum(value):
    return sum(x*(ord(y)-ord('0')) for x, y in zip(EAN_WEIGHTS[-12:], value[:-1]))

def ean_8_checksum(value):
    return sum(x*(ord(y)-ord('0')) for x, y in zip(EAN_WEIGHTS[-7:], value[:-1]))

def _check_digit(checksum):
    check = (int(checksum/10)+1)*10 if (checksum % 10 != 0) else checksum
    digit = check - checksum
    return str(digit)

def ean_13_check_digit(value):
    checksum = ean_13_checksum(value)
    return _check_digit(checksum)

def ean_8_check_digit(value):
    checksum = ean_8_checksum(value)
    return _check_digit(checksum)

def generate_random_ean_13_codes(count=10):
    return [v[0:12]+ean_13_check_digit(v) for v in (str(random.randint(10**11, 10**12 - 1))+'x' for _ in range(count))]

def generate_random_ean_8_codes(count=10):
    return [v[0:7]+ean_8_check_digit(v) for v in (str(random.randint(10**6, 10**7 - 1))+'x' for _ in range(count))]
