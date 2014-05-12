

class simplewebserver( object ):

    def __init__( self, paramdict ):
        print "simplewebserver initialized with following parameters:"
        for x in paramdict:
            print x, '\t', paramdict[x]
        pass

    def default( self, paramlist):
        print 'at simplewebserver.default()\n'

    def printimpressum( self, paramlist ):
        print 'impressum'
        return

