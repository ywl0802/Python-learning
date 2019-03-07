import re
def is_valid_email(addr):
    return re.match(r'^[a-zA-Z0-9\.\_]+@[a-zA-Z]+.com',addr)


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
        