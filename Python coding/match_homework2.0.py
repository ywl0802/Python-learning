import re 
def name_of_email(addr):
    name = re.match(r'([<]*)([A-Za-z0-9_.\s]*)([>]*)\s*([A-Za-z]*)@([0-9a-z]+).(\w{2,3})',addr)
    if name!=None:
        if name.group(1)!=None:
            print(str(name.group(2)))
        else:
            print(str(name.group(4)))
        return True
    else:
        return False

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
