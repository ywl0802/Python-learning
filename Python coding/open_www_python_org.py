import subprocess

print('$ nalookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:', r)
