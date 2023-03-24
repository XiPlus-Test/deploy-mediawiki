import os

os.chdir(os.environ.get('GITHUB_WORKSPACE'))
os.environ['PYWIKIBOT_DIR'] = os.environ.get('GITHUB_WORKSPACE')
import pywikibot

src = os.environ.get('SRC')
dst = os.environ.get('DST')
summary = os.environ.get('SUMMARY', '')

print('src', src)
print('dst', dst)
print('summary', summary)

with open(src, 'r') as f:
    new_text = f.read()

site = pywikibot.Site()
site.login()
page = pywikibot.Page(site, dst)

if new_text.rstrip() == page.text.rstrip():
    print('No changes')
else:
    page.text = new_text
    page.save(summary)
