import os

os.chdir(os.environ.get('GITHUB_WORKSPACE'))

print('src', os.environ.get('SRC'))
print('dst', os.environ.get('DST'))
print('summary', os.environ.get('SUMMARY'))
