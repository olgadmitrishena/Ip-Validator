import pytest

import ip_validator

valid_cases = ["145.100.110.255", "154.200.166.222", "255.111.222.231"]
invalid_cases = ["14.100.110.259", "154.200", "255.111.222.257", "0.35.1.1"]

def test_valid_ip():
    '''
    test: valid ip
    '''
    for case in valid_cases:
        assert ip_validator.validate_ip(case) == True

def test_invalid_ip():
    '''
    test: invalid ip
    '''
    for case in invalid_cases:
        assert ip_validator.validate_ip(case) == False

