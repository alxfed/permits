# -*- coding: utf-8 -*-
"""logged requests to the API
"""
import requests


enable_logging = True
if enable_logging:
    request_log = open("book.log","w")


def log(func):
    if enable_logging:
        def callf(*args,**kwargs):
            request_log.write("Calling %s: %s, %s\n" %
                            (func.__name__, args, kwargs))
            r = func(*args,**kwargs)
            request_log.write("%s returned %s\n" % (func.__name, r))
            return r
        return callf
    else:
        return func


def main():
    # here's the logging decorator
    @log
    def clicksend_api(num, message):
        try:
            res = requests.Request('clicksend.com')
            pass
        except TimeoutError as e:
            print('timeout')
            pass
        return res

    num = 3129709819
    message = 'test message'
    res = clicksend_api(num, message)
    if res.status() == 200:
        print('ok')
    else:
        print('not ok')
    return


if __name__ == '__main__':
    main()
    request_log.close()
    print('main - done')