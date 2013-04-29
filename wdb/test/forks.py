from multiprocessing import Process
from multiprocessing.util import log_to_stderr
from time import sleep
log_to_stderr(5)


class Process1(Process):

    def run(self):
        print 'Process 1 start'
        sleep(1)
        1/0
        print 'Process 1 end'
        sleep(1)


class Process2(Process):

    def run(self):
        print 'Process 2 start'
        # sleep(2)
        import wdb; wdb.set_trace()
        sleep(1)

        print 'Process 2 end'
        # sleep(2)

t1 = Process1()
t2 = Process2()
print 'Starting threads'
t1.start()
t2.start()

print 'Joining'
t1.join()
t2.join()

import wdb; wdb.set_trace()
print 'The End'