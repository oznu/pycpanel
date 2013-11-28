Python cPanel
=============

.. image:: https://pypip.in/v/pycpanel/badge.png
        :target: https://pypi.python.org/pypi/pycpanel
        
A Python wrapper for the cPanel API.

.. contents::
    :local:
    
.. _installation:

============
Installation
============

Using pip::

    $ pip install pycpanel
    
==============
Authentication
==============


You may use either remote access hash or basic user/password authentication. Remote access hash authentication is the prefered method.

Basic user/password authentication
----------------------------------

Warning: Do not perform authentication this way over an unsecured connection (ssl=False). The use of this method over an unsecured connection can compromise your server.

.. code:: python

    import pycpanel
    
    server = pycpanel.conn(hostname='myserver.com.au', password='mypassword')
    
Access hash authentication
--------------------------

http://docs.cpanel.net/twiki/bin/view/AllDocumentation/WHMDocs/RemoteAccess

.. code:: python

    import pycpanel
    
    hash = remote_access_hash
    server = pycpanel.conn(hostname='myserver.com.au', hash=hash)
    
Connection Options
------------------

The default options connect to the server as root using SSL on port 2087 without verifying the SSL certificate.

.. code:: python

    import pycpanel
    
    server = pycpanel.conn(hostname, username='root', hash=None, password=None, ssl=True, verify=False, check_conn=False)
    

- hostname (required) - the hostname or ip address of the cPanel server.
- username (optional, default='root') - the authenticating user's username.
- hash (optional) - The remote access hash for the cPanel server. If not provided a password must be provided instead.
- password (optional) - The password for the authenticating user. If not provided the remote access hash must be provided instead.
- ssl (optional, boolean, default=True) - If set to False pycpanel will connect on HTTP port 2086 rather than HTTPS port 2087.
- verify (optional, boolean, default=False) - If set to True the SSL certificate of the server will be verifying to ensure it is valid.
- check_conn (optional, boolean, default=True) - If set to True pycpanel will test and authenticate against the server after setting up the connection.

===================
cPanel External API
===================

Detailed documentation for the cPanel External API can be found here:
http://docs.cpanel.net/twiki/bin/view/SoftwareDevelopmentKit/XmlApi

.. code:: python

    pycpanel.api(function, params=None)

External API without params
---------------------------

This example will print a dict with all the cPanel accounts on the server. No additional params are passed in this example.

.. code:: python

    import pycpanel

    server = pycpanel.conn(hostname='myserver.com.au', password='mypassword')
    print server.api('listaccts')
    
    
External API with params
------------------------
    
This exmaple will adjust the cPanel account with username 'user1' to have a limit of 10 addon domains.

.. code:: python

    import pycpanel
    
    server = pycpanel.conn(hostname='myserver.com.au', password='mypassword')
    
    params = {
        'user'      : 'user1',
        'MAXADDON ' : 10,
    }
    
    server.api('modifyacct', params=params)
    
======================
cPanel API 2 Functions
======================

Detailed documentation for the cPanel API 2 Functions can be found here:
http://docs.cpanel.net/twiki/bin/view/ApiDocs/Api2/WebHome

.. code:: python

    pycpanel.cpanel_api(module, function, user, params=None)


API 2 Function without params
-----------------------------

This example retrieves a list of email accounts associated with a cPanel account with username 'user1'.

.. code:: python

    import pycpanel
    
    server = pycpanel.conn(hostname='myserver.com.au', password='mypassword')
    
    print server.cpanel_api('Email', 'listpops', 'user1')
    
    
API 2 Function with params
--------------------------

This example creates a new email account (steve@mydomain.com.au) for the user account 'user1'.

.. code:: python

    import pycpanel
    
    server = pycpanel.conn(hostname='myserver.com.au', password='mypassword')
    
    params = {
        'domain'    : 'mydomain.com.au',
        'email'     : 'steve',
        'password'  : '@#fwefq122442',
        'quota'     : 0
    }
    
    server.cpanel_api('Email', 'addpop', 'user1', params=params)
    

