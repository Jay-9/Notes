import socket
import time

sk = socket.socket()
sk.bind(('127.0.0.1', 8000))
sk.listen()


def yi(the_url):
    return '欢迎访问 {}'.format(the_url)


def er(the_url):
    return '欢迎访问 {}'.format(the_url)


def san(the_url):
    return '欢迎访问 {}'.format(the_url)


def home(the_url):
    with open('home.html', 'r', encoding='utf-8') as f:
        the_ret = f.read()
        return the_ret


def the_time(the_url):
    now = time.time()
    with open('time.html', 'r', encoding='utf-8') as f:
        the_ret = f.read()
        return the_ret.replace('@@time@@', str(now))


list1 = [
    ('/yi', yi),
    ('/er', er),
    ('/san', san),
    ('/home', home),
    ('/time', the_time),
]

while True:
    coon, addr = sk.accept()
    data = coon.recv(2048).decode('utf-8')
    url = data.split()[1]

    coon.send(b'HTTP/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n')

    func = None
    for i in list1:
        if url == i[0]:
            func = i[1]
            break
    if func:
        ret = func(url)
    else:
        ret = '404 not found'

    coon.send(ret.encode('utf-8'))

    coon.close()
