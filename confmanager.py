import os, imp, json, sys
import types
from moduleloader import moduleloader, routemanager

class confmanager( object ):

    __defaultport = 1984
    __defaulthost = '127.0.0.1'
    __defaultmaxthreads = 5
    __defaultqueuesize = 0  # infinite space

    def __init__(self, path):
        """
        Creates an Instance of confmanager.
        @param
            path: filepath to an configfile which can be used by confmanager
        """
        self.path = path
        self.modules = {}
        try:
            self.config = self._readconfig( path )
            self.routes = self.config["routes"]
            # get the port
            self.port = self._port()
            self.host = self._host()
            self.maxthreads = self._maxthreads()
            self.queuesize = self._queuesize()
        except Exception, e:
            # TODO log exc + msg
            print e
        self.loadedroutes = {}

    def _readconfig(self, path ):
        """
        Tries to read from a given config file.
        On error, exceptions will be thrown
        """
        conf = ''
        with open( path ) as f:
            for line in f:
                if line.strip(' \t').startswith('#') == False:
                    conf = conf + line[ :-1 ]
        jconf = json.loads( conf )
        # TODO del debug-print
        print conf
        return jconf
   
    def _port( self ):
        if self.config.has_key( "port" ):
            port = self.config['port']
            # is this a valid port?
            if type( port ) == types.IntType:
                return port
        # otherwise set it to default
        return self.__class__.__defaultport

    def _host( self ):
        if self.config.has_key( 'host' ):
            return self.config['host']
        else:
            return self.__class__.__defaulthost
            
    def _maxthreads( self ):
        if self.config.has_key( 'maxthreads' ):
            mt = self.config['maxthreads']
            if type( mt ) == types.IntType:
                return mt
        else:
            return self.__class__.__defaultmaxthreads

    def _queuesize( self ):
        if self.config.has_key( 'queuesize' ):
            qs = self.config['queuesize']
            if type( qs ) == types.IntType:
                return qs
        return self.__class__.__defaultqueuesize


    def getroutemanager( self ):
        if not hasattr( self, '_routemanagerinstance' ):
        #if not self.hasattr( _routemanagerinstance ):
            self._routemanagerinstance = routemanager()._update( self.routes )
            pass
        return self._routemanagerinstance

    def updateroutemanager( self ):
        return self._routemanagerinstance.update( self.routes )



