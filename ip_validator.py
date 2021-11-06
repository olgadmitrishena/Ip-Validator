#! python3

import argparse
import pytest

def main():
    parser = argparse.ArgumentParser(add_help=False, description="This script validate ip address")
    required_args = parser.add_argument_group('required args')
    required_args.add_argument('-a', '--address', dest='ip_addr', metavar='ip_addr', required=True,
                               help='Please provide IP address')
    args = parser.parse_args()
    valid = validate_ip(args.ip_addr)
    if valid:
        print("This IP address is valid")
    else:
        print("This IP address is invalid")


def validate_ip(input):
    '''
    This function validates the ip address
    :param input: str
    :return: boolean
    '''
    ip = input.split('.')
    if len(ip) != 4:
        return False
    for n in ip:
        try:
            number = int(n)
            if number < 1 or number > 255:
                return False
        except Exception:
            return False
    return True


if __name__ == '__main__':
    main()