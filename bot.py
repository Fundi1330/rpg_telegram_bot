from telegram.ext import *

key = ''

with open('config.ini', 'r') as file:
    read = file.read()

key = read
print(key)
def start(update, context):
    update.message