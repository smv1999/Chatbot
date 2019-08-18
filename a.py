from multiprocessing import Process
from threading import Thread

def func1():
  print 'func1: starting'
  for i in xrange(10000000): pass
  print 'func1: finishing'

def func2():
  print 'func2: starting'
  for i in xrange(10000000): pass
  print 'func2: finishing'

def func3():
  print 'func3: starting'
  for i in xrange(10000000): pass
  print 'func3: finishing'

if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p3 = Process(target=func3)
  p3.start()
  p1.join()
  # p2.join()
  # p3.join()