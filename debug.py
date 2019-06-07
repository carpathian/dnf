import os

print("Hello!!")
config = os.environ['COPR_INI']
print('config: ', config)
for c in config:
    print(c)

