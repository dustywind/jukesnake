
import vlc
import pdb
import sqlite3


class PlayerFactory( object ):

    @staticmethod
    def getinstance( ):
        if self._instance == None:
            self._instance = VLCWrapper()
        return self._instance



class VLCWrapper( object ):
    """
    The VLCWrapper contains a list of playable media
    and takes care of the user-input to control the vlc-player
    
    Datastructures:
        - media_list: [ ( id, path, artist, album, songtitel, songnr ), ( ... ) ]
    """

    database = './musiclibrary.db'

    def __init__( self ):
        # create the vlc stuff
        self.vlc_instance = vlc.Instance()
        self.vlc_mediaplayer = self.vlc_instance.media_player_new()

        # connect to the database and check, if all tables are initialised
        self.dbconn = sqlite3.connect( VLCWrapper.database )        
        self.dbc = self.dbconn.cursor()
        self.initdatabase()


        # create list structures such as a list of playable media
        self.media_list = []
        pass

    def initdatabase( self ):
        self.dbc.execute(
            """
            CREATE TABLE IF NOT EXISTS tArtists (
                artist_id           INTEGER PRIMARY KEY,
                artist_name         TEXT
            )
            """
        )
        self.dbc.execute(
            """
            CREATE TABLE IF NOT EXISTS tAlbum (
                album_id            INTEGER PRIMARY KEY,
                album_name          TEXT
            )
            """
        )
        self.dbc.execute(
            """
            CREATE TABLE IF NOT EXISTS tSongs (
                song_id             INTEGER PRIMARY KEY,
                song_name           TEXT,
                song_path           TEXT,

                FOREIGN KEY( artist_id ) REFERENCES tArtists( artist_id ),
                FOREIGN KEY( album_id ) REFERENCES tAlbum( album_id )
            )
            """
        )
        self.dbc.execute(
            """
            CREATE TABLE IF NOT EXISTS tPlaylists (
                playlist_id         INTEGER PRIMARY KEY,
                playlist_content    TEXT
            )
            """
        )
        pass

    def newmedialist( self, nmedialist ):
        # TODO, Check, whether nmedialist contains useable stuff or not
        pass






















