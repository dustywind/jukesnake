import pdb
import re
import socket

class HTTPHelper( object ):

    class HTTPStatusLine( object ):
        OK = 200


    def __init__( self ):
        pass

    
    @staticmethod
    def readheaderfromconnection( conn ):
        print 'entered HTTPHelper.readheaderfromconnection'
        offset = 0
        # 284
        bufsize = 4096
        msg = ''

        # read from the socket
        while True:
            tmsg = conn.recv(bufsize)
            #o = conn.recv_into( buffer( msg, offset, bufsize ) )
            
            msg = msg + tmsg

            # check for '\r\n\r\n' - the HTTP-end thingy
            if msg.find( '\r\n\r\n' ) >= 0:
                break

        #create the header
        header = HTTPHeader()

        for i, entry in enumerate( msg.split( '\r\n' ) ):
            if i == 0:
                header.method, header.path, header.protocol = re.search('([\w]*) ([/\w.]*) ([/\w.]*)', msg ).groups()
                continue
            elif len( entry ) == 0:
                break
            # get the other fields
            key, value = re.search('([-\w]*): ([\w\s/;.:\(\)]*)', entry).groups()
            header.fields[ key ] = value
            pass


        # check, if there is a payload
        # and read it - if neccessary
        if header.method == 'POST':
            if header.fields.has_key( 'Content-Length' ):
                payload_length = header.fields[ 'Content-Length' ]
                pass
        else:
            payload_length = 0

        header.payload = msg.split( '\r\n\r\n' )[1]
        if len( header.payload ) <  payload_length:
            # keep on reading the payload
            header.payload += conn.recv( payload_length - len( header.payload ) )

            print header.payload
            pass

        print 'done'

        return header
        


class HTTPHeader( object ):

    def __init__( self ):
        self.method = None
        self.path = None
        self.fields = {}
        self.payload = None
        self.protocol = 'HTTP/1.1'
        pass



class HTTPResponse( object ):

    def __init__( self, statusline):
        self.statusline = statusline
        self.message = ''

    def getfullresponse( self ):
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Server: myawesomeserver\r\n'
        response += 'Connection: close\r\n'
        response += 'Content-Type: image/jpeg\r\n'
        # add another \r\n to signalise the data-part thingy
        response += '\r\n'
        response += self.message
        return response

    def writeresponse( self, connection ):
        i = connection.send( self.getfullresponse() )
        if i != ( self.getfullresponse() ):
            print 'sent ', i, ' bytes instead of ', len( self.getrullresponse() )
        pass

    def append( self, message ):
        self.message += message
        pass


