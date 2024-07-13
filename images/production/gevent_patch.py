import gevent.monkey

gevent.monkey.patch_all(ssl=False)
#gevent.monkey.patch_all()
