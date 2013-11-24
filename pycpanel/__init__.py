__title__ = 'pycpanel'
__version__ = '0.1.1'
__date__ = '2013-11-24'
__licence__ = 'Apache License Version 2.0'
__author__ = 'OZNU'

import requests, json

class conn(object):
    def __init__(self, hostname, username='root', hash=None, password=None, ssl=True,  verify=False, check_conn=True):
        self.__session__ = requests.Session()
        if hash != None: hash = hash.replace('\r\n', '')
        if hash != None: self.__session__.headers.update({'Authorization' : 'WHM %s:%s' % (username,hash)})
        if password != None: self.__session__.auth = (username, password)
        if ssl == True: self.__hostname__ = 'https://' + str(hostname) + ':2087/'
        elif ssl == False: self.__hostname__ = 'http://' + str(hostname) + ':2086/'
        self.__verify__ = verify
        try:
            if check_conn == True: self.__apilist__ = self.api('applist')['app']
            else: self.__apilist__ = None
        except:
            raise Exception('Error establishing a connection to %s.' % self.__hostname__)

    def api(self, command, params=None, api='json-api'):
        r = self.__session__.get(self.__hostname__ + api  + '/' +  command, params=params, verify=self.__verify__)
        if r.status_code == 403: raise Exception('Access denied:  please check the username and hash/password.' % hostname)
        if api == 'json-api': return json.loads(r.text)
        return r.text

    def cpanel_api(self, module, function, user, version=2, params=None, api='json-api/cpanel'):
        generic = {
            'cpanel_jsonapi_user' : user,
            'cpanel_jsonapi_module' : module,
            'cpanel_jsonapi_func' : function,
            'cpanel_jsonapi_apiversion' : version,
        }
        if params != None: params = dict(generic.items() + params.items())
        elif params == None: params = generic
        r = self.__session__.get(self.__hostname__ + api, params=params, verify=self.__verify__)
        if r.status_code == 403: raise Exception('Access denied:  please check the username and hash/password.' % hostname)
        if api == 'json-api/cpanel': return json.loads(r.text)['cpanelresult']['data']
        return r.text

    def json_list(self):
        if self.__apilist__ == None:
            self.__apilist__ = self.api('applist')['app']
        return self.__apilist__
