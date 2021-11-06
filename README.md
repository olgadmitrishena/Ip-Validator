# Ip-Validator
Check whether an input string is a valid IP address. If it's not a valid address, throw error. If it's a valid address, check and print whether it's a class A, class B, or class C IP address.

ip_validator.py contains main and validate_ip functions
it takes 1 argument (ip address), with flag -a or --address and validates if it's valid IPv4 address.

```python3 ip_validator.py -a 192.168.1.1```

test.py contains 2 unit tests with set of negative and positive test cases.

```pytest test.py```