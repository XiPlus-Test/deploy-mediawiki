import os

import pywikibot

os.chdir(os.environ.get('GITHUB_WORKSPACE'))

src = os.environ.get('SRC')
dst = os.environ.get('DST')
summary = os.environ.get('SUMMARY', '')

print('src', src)
print('dst', dst)
print('summary', summary)

with open(src, 'r') as f:
    new_text = f.read()

site = pywikibot.Site()
page = pywikibot.Page(site, dst)

if new_text.rstrip() == page.text.rstrip():
    print('No changes')
else:
    page.text = new_text
    page.save(summary)
