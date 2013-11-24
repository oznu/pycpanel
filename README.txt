pycpanel: Python module for the cPanel API
==========================================

pycpanel provides a wrapper for the WHM and cPanel API.

Supported API Calls:
    - WHM XML/JSON API Functions
    - API 2 Functions
    - Limited support for API 1 Functions

Typical usage:

    #!/usr/bin/env python

    import pycpanel

    # connect to cPanel server with password:
    server = pycpanel.conn(hostname='server1.myhost.com.au', password='mypassword')

    # Display a list of accounts on the server:
    print server.api('listaccts')

    # Modify contact email address for account 'userone':
    params = {
        'user'         : 'userone',
        'contactemail' : 'newemail@domain.com.au',
    }

    print server.api('modifyacct', params=params)


Advanced Connections:

    pycpanel.conn(hostname, username='root', hash=None, password=None, ssl=True, verify=False, check_conn=True)

    hostname: the hostname of the cPanel server.
    username (optional, default = root): the authenticating user's username.
    hash (optional): The remote access hash for the cPanel server. If not provided a password must be provided instead.
    password (optional): The password for the authenticating user. If not provided the remote access hash must be provided instead.
    ssl (optional, default = True): If set to false pycpanel will connect on HTTP port 2086 rather than HTTPS port 2087.
    verify (optional, default = False): If set to True the SSL certificate of the server will be checked to ensure it is valid.
    check_conn (optional, default = True): If set to True pycpanel will test and authenticate against the server after setting up the connection.


    Example:

        server = pycpanel.conn(hostname='server1.myhost.com.au', hash=hash, ssl=False, user='reseller_username')


Calling API 2 Functions:

    pycpanel.cpanel_api(module, function, user, version=2, params=None)

    module: Name of the module to access.
    function: Name of the function to access.
    user: The user as whom you wish to call the function.     
    version (optional, default = 2): Version of the API to access. API 1 calls are not supported, but may work.
    params: A dict of the API arguments / paramaters.

    Example:

        server = pycpanel.conn(hostname='server1.myhost.com.au', password='mypassword')

        params = {
            'domain' : 'domain.com.au',
        }
        print server.cpanel_api('Email', 'listpopswithdisk', 'username', params=params)

        Returns:

            {
               u'diskusedpercent20':0,
               u'diskused':0.01,
               u'domain':u'domain.com.au',
               u'_diskquota':u'262144000',
               u'diskquota':250,
               u'email':u'this@domain.com.au',
               u'_diskused':u'7221',
               u'user':u'this',
               u'humandiskquota':u'250\xa0MB',
               u'mtime':1385279920,
               u'humandiskused':u'7.05\xa0KB',
               u'diskusedpercent':0,
               u'login':u'this@domain.com.au',
               u'txtdiskquota':250
            }     



A list of all the WHM API Calls can be found here:
    http://docs.cpanel.net/twiki/bin/view/SoftwareDevelopmentKit/XmlApi

A list of the cPanel API 2 Calls can be found here:
    http://docs.cpanel.net/twiki/bin/view/ApiDocs/Api2/WebHome


    

