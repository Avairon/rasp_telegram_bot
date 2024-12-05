import sys
sys.path.insert(1, 'D:\Code\CodePython\chat_bot_python\Chats_bot_paython')

import src.tranzactions as tr

text = tr.read_messages()
str = "16"

print(text[8] % (str))
