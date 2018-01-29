import itchat
import sys

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)

    for item in itchat.get_friends():
        if item['NickName'] == 'Taylor Liang':
            itchat.send('Hello, taylor', toUserName=item['UserName'])
            break

    sys.exit(0)
