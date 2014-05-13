import os, imp, json, sys
import pdb
import types

class moduleloader( object ):
    
    __routemanagerinstance = None

    @staticmethod
    def loadmodule( conf ):
        """
        loads all items defined in the config, received by _readconfig
        """
        try:
            #conf = routes[ route ]
            # try to load the module
            module_name = conf['module']['name']
            module_path = conf['module']['path']
            
            mod_name, file_ext = os.path.splitext( os.path.split( module_path )[ -1] )
            if file_ext.lower() == '.py':
                py_mod = imp.load_source( mod_name, module_path )
            elif file_ext.lower() == '.pyc':
                py_mod = imp.load_compiled( mod_name, module_path )
            else:
                raise Exception("Cannot handle module for route: " + route )
        except Exception, e:
            import traceback
            traceback.print_exc( file=sys.stdout )
            # TODO log error + msg
        return py_mod

    @staticmethod
    def getinstanceofmodule( module, classname, parameter):
        instance = None
        if hasattr( module, classname ):
            instance = getattr( module, classname )( parameter )
        return instance


    @staticmethod
    def getroutemanager( ):
        #if not hasattr( self, '__routemanagerinstance' ):
        #_routemanagerinstance = routemanager()._update( self.routes )
        if __routemanagerinstance == None:
            __routemanagerinstance = routemanager()._update( routes )
        return _routemanagerinstance

    @staticmethod
    def updateroutemanager( ):
        return getroutemanager()._update( self.routes )


class routemanager( object ):

    def __init__( self ):
        self.index = {}
        pass

    def _update( self, routes ):
        """
        """
        del self.index
        self.index = routes
        # add the instance of the class
        for route in self.index:
            module = moduleloader.loadmodule( route )
            route[ 'instance' ] = moduleloader.getinstanceofmodule( module, route['module']['name'], {} )
        return self 

    def execroute( self, route ):
        """
        """
        #pdb.set_trace()

        # ommit tainlint '/'
        if route[-1] == '/':
            route = route[:-1]
            pass

        for i in self.index:
            if route.startswith( i['route'] ):
                # found a matching route
                # are there any subroutes?
                route = route.replace( i['route'], '' )
                method = i['defaultmethod']

                for sub in i['subroutes']:
                    if route.startswith( sub['path'] ):
                        # get the method
                        method = sub['method']
                        # adapt route (to determine parameters)
                        route = route.replace( sub['path'], '' )
                        pass
                    pass

                # exec method
                if len(route) > 0:
                    if route[1] == '/':
                        param = route[1:].split('/')
                    else:
                        param = route.split('/')
                else:
                    param = []
                # get the instance and exec the given method
                pdb.set_trace()

                i['instance'].__getattribute__( method )( param )
                break



