import os

os.chdir(os.environ.get('GITHUB_WORKSPACE'))

username = os.environ.get('USERNAME', '')
botname = os.environ.get('BOTNAME', '')
password = os.environ.get('PASSWORD', '')
family = os.environ.get('FAMILY')
mylang = os.environ.get('MYLANG')
url = os.environ.get('URL')

if url:
    family = 'mysite'
    MYLANG = 'mysite'

print('username', username)
print('family', family)
print('mylang', MYLANG)
print('url', url)

with open('user-config.py', 'w', encoding='utf8') as f:
    if family:
        f.write("family = '{}'\n".format(family))
    if mylang:
        f.write("mylang = '{}'\n".format(mylang))
    if family and mylang:
        f.write("usernames['{}']['{}'] = u'{}'\n".format(
            family,
            mylang,
            username,
        ))
    if url:
        f.write("family_files['mysite'] = '{}'\n".format(url))

with open('user-password.py', 'w', encoding='utf8') as f:
    f.write("(u'{}', BotPassword(u'{}', u'{}'))\n".format(
        username,
        botname,
        password,
    ))
