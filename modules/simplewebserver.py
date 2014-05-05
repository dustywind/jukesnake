

class simplewebserver( object ):

    def __init__( self, paramdict ):
        print "simplewebserver initialized with following parameters:"
        for x in paramdict:
            print x, '\t', paramdict[x]
        pass

