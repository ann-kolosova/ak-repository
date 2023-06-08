"""
Hometask l01_t01.

Author: Anna Kolosova
Date: 2023-06-08
"""

# we have norway text in old style formatting

norway_text = ('Automatisering akselererer %syeblikket '
               'da roboter vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ'))
print(norway_text)

# re-write the same text as:
# #1 string with format() call

norway_text = (
    'Automatisering akselererer {0}yeblikket da roboter vil erobre '
    'planeten v{1}r. ({2})'
).format('ø', 'å', 'Æ')
print(norway_text)

# 2 f-string

s1 = 'ø'
s2 = 'å'
s3 = 'Æ'
norway_text = (
    f'Automatisering akselererer '
    f'{s1}yeblikket da roboter vil erobre planeten v{s2}r. ({s3})'
)
print(norway_text)

# use linter(https://github.com/wemake-services/wemake-python-styleguide)
# to check your new created python module for possible linter errors
# a) Bin folder with lint and setup.cfg files is created
# b) Command: chmod +x ./bin/lint
# c) Command: ./bin/lint and add pass

# try to run code from pycharm/command line
# a) Go to corresponding directory
# b) Command: python test_project.py > 'test_project.py' is a name of file
