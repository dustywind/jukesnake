import pdb
import os

class jukebox( object ):

    def __init__( self, paramdict ):
        self.rootdir = paramdict['rootdir']
        pass

    def default( self, connection, paramlist):
        
        #if there are no parameters at all, get /index.html
        if len( paramlist ) == 0:
            paramlist.insert( 0, 'index.html' )

        # reassamble the route to the file
        path = self.rootdir
        for p in paramlist:
            path = os.path.join( path, p )

        print "following path was requested: ", path
        
        if os.path.isfile( path ):
            content = ''
            with open( path ) as f:
                for line in f:
                    content += line
                pass
            return content
        elif os.path.isdir( path ):
            return "some directory content"

    def rest( self, connection, paramlist ):
        """
        TODO IMPLEMENT
        actually this should be a restful api with lot's of methods
        """
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
