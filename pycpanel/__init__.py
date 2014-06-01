__title__ = 'pycpanel'
__version__ = '0.1.3'
__date__ = '2013-12-08'
__licence__ = 'Apache License Version 2.0'
__author__ = 'oznu'

import requests, json

def unauthorised():
    raise Exception('Access denied:  please check the username and hash/password.')

class conn(object):
    def __init__(self, hostname, username='root', hash=None, password=None, ssl=True,  verify=False, check_conn=True):
        self.__session__ = requests.Session()
        if hash != None: hash = hash.replace('\r', '').replace('\n', '')
        if hash != None: self.__session__.headers.update({'Authorization' : 'WHM %s:%s' % (username,hash)})
        if password != None: self.__session__.auth = (username, password)
        if ssl == True: self.hostname = 'https://' + str(hostname) + ':2087/'
        elif ssl == False: self.hostname = 'http://' + str(hostname) + ':2086/'
        self.verify = verify
        try:
            if check_conn == True: self.apilist = self.api('applist')['app']
            else: self.apilist = None
        except: unauthorised() 

    def api(self, command, params=None, api='json-api'):
        r = self.__session__.get(self.hostname + api  + '/' +  command, params=params, verify=self.verify)
        if r.status_code == 403: unauthorised()
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
        r = self.__session__.get(self.hostname + api, params=params, verify=self.verify)
        if r.status_code == 403: unauthorised()
        if api == 'json-api/cpanel':
            if version == 1:
                return json.loads(r.text)['data']
            else:
                return json.loads(r.text)['cpanelresult']['data']
        return r.text

    def json_list(self):
        if self.apilist == None:
            self.apilist = self.api('applist')['app']
        return self.apilist
 
    @property
    def csf(self):
        return self.CSF(self)

    class CSF(object):
        def __init__(self, conn):
            self.conn = conn

        def unblock(self,ip):
            r = self.conn.__session__.post(self.conn.hostname + 'cgi/configserver/csf.cgi', data={ 'ip' : ip, 'action' : 'kill' }, verify=self.conn.verify)
            if r.status_code == 200: return True
            else: return unauthorised()

        def deny(self,ip,comment=None):
            r = self.conn.__session__.post(self.conn.hostname + 'cgi/configserver/csf.cgi', data={ 'ip' : ip, 'action' : 'qdeny', 'comment' : comment }, verify=self.conn.verify)
            if r.status_code == 200: return True
            else: return unauthorised()

        def allow(self,ip,comment=None):
            r = self.conn.__session__.post(self.conn.hostname + 'cgi/configserver/csf.cgi', data={ 'ip' : ip, 'action' : 'qallow', 'comment' : comment }, verify=self.conn.verify)
            if r.status_code == 200: return True
            else: return unauthorised()

        def ignore(self,ip):
            r = self.conn.__session__.post(self.conn.hostname + 'cgi/configserver/csf.cgi', data={ 'ip' : ip, 'action' : 'qignore' }, verify=self.conn.verify)
            if r.status_code == 200: return True
            else: return unauthorised()

