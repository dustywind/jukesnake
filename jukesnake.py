from confmanager import confmanager
import socket
import threading
import Queue
from HTTPHelper import HTTPHelper
import pdb


class RequestHandler( threading.Thread ):
    
    def __init__( self, connqueue, routemanager, stopevent ):
        threading.Thread.__init__( self )
        self.connqueue = connqueue
        self.rm = routemanager
        self.stop = stopevent
        pass

    def run( self ):
        print self.name, ' is running'
        while True:
            try:
                # check for event
                if self.stop.is_set():
                    break

                # take a socket from the queue
                c = connqueue.get( True, 2 )

                # read from the socket
                httpheader = HTTPHelper.readheaderfromconnection( c )
                
                # chose the matching route-module
                # use the given function
                
                print 'about to exec given method'
                method, param = self.rm.getmethod( httpheader.path )
                method( [c] + param )
                #self.rm.execroute( httpheader.path )

                c.close()
            except Exception, msg:
                pass
        print self.name, ' is shutting down'
        return


if __name__ == '__main__':
    conf = confmanager('./example.conf')

    # create server-stuff
    # initialize sockets + pthreads
    bindaddr = (bindhost, bindport) = conf.host, conf.port
    
    print bindaddr

    lsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM, 0 )
    lsock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    lsock.bind( bindaddr )
   
    lsock.listen( 2 )   # max backlog == 5

    # routemanager
    rm = conf.getroutemanager()

    print 'loaded routemanager'

    # create the thread-thingy
    connqueue = Queue.Queue( 3 ) # infinite size per default

    print 'created queue'

    thread_stopper = threading.Event()
    threads = []
    for x in xrange( conf.maxthreads ):
        t =  RequestHandler( connqueue, rm, thread_stopper )
        t.start()
        threads + [ t ]

    print 'createt threads'

    while True:
        try:
            while True:
                csock, _ = lsock.accept()
                print 'accepted'
                connqueue.put( csock, False )
        except KeyboardInterrupt, msg:
            break
        except Exception, msg:
            pass

    # wow, do some waiting...
    # dunno
    # we'll see how to implement this feature

    print 'cought excepion'

    thread_stopper.set()

    for t in threads:
        t.join( 4 )
        if t.isAlive():
            print t.name, ' could not join'
            pass
    lsock.close()

    print 'bye :D'

    pass



