from wsgiref.simple_server import make_server


def index(url):
    with open('index.html', 'r', encoding='utf-8') as f:
        s = f.read()
        return bytes(s, encoding='utf-8')


def home(url):
    with open('home.html', 'r', encoding='utf-8') as f:
        s = f.read()
        return bytes(s, encoding='utf-8')


def timer(url):
    import time
    now = time.time()
    with open('time.html', 'r', encoding='utf-8') as f:
        s = f.read()
        s = s.replace('@@time@@', time.strftime('%Y-%m-%d %H:%M:%s'))
        return bytes(s, encoding='utf-8')



list1 = [
    ('/index', index),
    ('/home', home),
    ('/time', timer),
]


def run_server(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html; charset=utf-8'), ])
    url = environ['PATH_INFO']
    func = None
    for i in list1:
        if url == i[0]:
            func = i[1]
            break
    if func:
        response = func(url)
    else:
        response = b'404 not found'
    return [response, ]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8090, run_server)
    print('始于8090端口')
    httpd.serve_forever()

