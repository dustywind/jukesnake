import pdb
import os

class jukebox( object ):

    class PlayerStates( object ):
        PLAY = 'play'
        PAUSE = 'pause'

        NEXT = 'next'
        PREV = 'prev'

        PLAY_AT = 'playat'

        MEDIALIST = 'medialist'

        SET_VOLUME = 'setvolume'


    def __init__( self, paramdict ):
        """
        Do some initial stuff
        create a instance of the VLC-Player Wrapper
        """
        self.rootdir = paramdict['rootdir']

        # TODO VLC Wrapper instance
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

        if len( paramlist ) == 0:
            return ""

        if paramlist[0] == jukebox.PlayerStates.PLAY:
            self.play()
        elif paramlist[0] == jukebox.PlayerStates.PAUSE:
            pass
        elif paramlist[0] == jukebox.PlayerStates.NEXT:
            pass
        elif paramlist[0] == jukebox.PlayerStates.PREV:
            pass
        elif paramlist[0] == jukebox.PlayerStates.PLAY_AT:
            pass
        elif paramlist[0] == jukebox.PlayerStates.MEDIALIST:
            pass
        elif paramlist[0] == jukebox.PlayerStates.SET_VOLUME:
            pass
        pass

    
    def play( self ):
        pass



