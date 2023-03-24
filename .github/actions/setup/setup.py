import os

os.chdir(os.environ.get('GITHUB_WORKSPACE'))

print('username', os.environ.get('USERNAME'))
print('password', os.environ.get('PASSWORD'))
print('family', os.environ.get('FAMILY'))
print('mylang', os.environ.get('MYLANG'))
print('url', os.environ.get('URL'))
