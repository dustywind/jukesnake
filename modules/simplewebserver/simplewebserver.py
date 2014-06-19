import pdb
import os

class simplewebserver( object ):

    def __init__( self, paramdict ):
        print "simplewebserver initialized with following parameters:"
        for x in paramdict:
            print x, '\t', paramdict[x]
        self.rootdir = paramdict['rootdir']
        pass

    def default( self, connection, paramlist):
        print 'at simplewebserver.default()\n'

        # reassamble the route to the file
        path = self.rootdir
        for p in paramlist:
            path = os.path.join( path, p )
        
        print 'requested file: ', path

        #pdb.set_trace()

        if os.path.isfile( path ):
            content = ''
            with open( path ) as f:
                for line in f:
                    content += line
                pass
            return content
        elif os.path.isdir( path ):
            return "some directory content"

    def echo( self, connection, paramlist ):
        message = """<!DOCTYPE html>
            <html>
            <head><title>ECHO</title></head>
            <body>
            <ul>
            """
        for param in paramlist:
            message += "<li>"
            message += param
            message += "</li>"
            
        message += "</ul></body></html>"
        return message

    def printimpressum( self, connection, paramlist ):
        print 'impressum'
        return

