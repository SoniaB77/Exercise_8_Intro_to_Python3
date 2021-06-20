import sys


argc = len(sys.argv)
if argc > 1:
    print('too many args')
    print(sys.argv[1])
else:
    where = 'world'
    print("Hello", where)
print('Goodbye from ' + sys.argv[0])


