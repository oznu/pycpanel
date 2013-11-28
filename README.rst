<h2>Python cPanel</h2>

<a href='https://pypi.python.org/pypi/pycpanel'><img src='https://pypip.in/v/pycpanel/badge.png'></a>

A Python wrapper for the cPanel API.

<h2><a href="#installation">Installation<a></h2>

Using pip:

    pip install pycpanel
    
<h2><a href='#authentication-handlers'>Authentication</a></h2>

You may use either remote access hash or basic user/password authentication. Remote access hash authentication is the prefered method.

<h3><a href='#basic-userpassword-authentication'>Basic user/password authentication</a></h3>

Warning: Do not perform authentication this way over an unsecured connection (ssl=False). The use of this method over an unsecured connection can compromise your server.

    import pycpanel
    
    server = pycpanel.conn(hostname='myserver.com.au', password='mypassword')
    
<h3><a href='#access-hash-authentication'>Access hash authentication</a></h3>

http://docs.cpanel.net/twiki/bin/view/AllDocumentation/WHMDocs/RemoteAccess

    import pycpanel
    
    hash = remote_access_hash
    server = pycpanel.conn(hostname='myserver.com.au', hash=hash)
    
<h3><a href='#connection-options'>Connection Options</a></h3>

The default options connect to the server as root using SSL on port 2087 without verifying the SSL certificate.

    import pycpanel
    
    server = pycpanel.conn(hostname, username='root', hash=None, password=None, ssl=True, verify=False, check_conn=False)
    
<ul>
<li><strong>hostname</strong> (required) - the hostname or ip address of the cPanel server.</li>
<li><strong>username</strong> (optional, default='root') - the authenticating user's username.</li>
<li><strong>hash</strong> (optional) - The remote access hash for the cPanel server. If not provided a password must be provided instead.</li>
<li><strong>password</strong> (optional) - The password for the authenticating user. If not provided the remote access hash must be provided instead.</li>
<li><strong>ssl</strong> (optional, boolean, default=True) - If set to False pycpanel will connect on HTTP port 2086 rather than HTTPS port 2087.</li>
<li><strong>verify</strong> (optional, boolean, default=False) - If set to True the SSL certificate of the server will be verifying to ensure it is valid.</li>
<li><strong>check_conn</strong> (optional, boolean, default=True) - If set to True pycpanel will test and authenticate against the server after setting up the connection.</li>
</ul>

<h2><a href="#cpanel-external-api">cPanel External API<a></h2>

Detailed documentation for the cPanel External API can be found here:
http://docs.cpanel.net/twiki/bin/view/SoftwareDevelopmentKit/XmlApi

    pycpanel.api(function, params=None)

<h4><a href='#example-1'>Example 1</a></h4>

This example will print a dict with all the cPanel accounts on the server. No additional params are passed in this example.

    import pycpanel

    server = pycpanel.conn(hostname='myserver.com.au', password='mypassword')
    print server.api('listaccts')
    
    
<h4><a href='#example-2'>Example 2</a></h4>
    
This exmaple will <a target='_blank' href='http://docs.cpanel.net/twiki/bin/view/SoftwareDevelopmentKit/ModifyAccount'>adjust the cPanel account</a> with username 'user1' to have a limit of 10 addon domains.

    import pycpanel
    
    server = pycpanel.conn(hostname='myserver.com.au', password='mypassword')
    
    params = {
        'user'      : 'user1',
        'MAXADDON ' : 10,
    }
    
    server.api('modifyacct', params=params)
    
    
<h2><a href="#cpanel-external-api">cPanel API 2 Functions<a></h2>

Detailed documentation for the cPanel API 2 Functions can be found here:
http://docs.cpanel.net/twiki/bin/view/ApiDocs/Api2/WebHome

    pycpanel.cpanel_api(module, function, user, params=None)


<h4><a href='#example-3'>Example 3</a></h4>

This example retrieves a list of email accounts associated with a cPanel account with username 'user1'.

    import pycpanel
    
    server = pycpanel.conn(hostname='myserver.com.au', password='mypassword')
    
    print server.cpanel_api('Email', 'listpops', 'user1')
    
    
<h4><a href='#example-4'>Example 4</a></h4>

This example creates a new email account (steve@mydomain.com.au) for the user account 'user1'.

    import pycpanel
    
    server = pycpanel.conn(hostname='myserver.com.au', password='mypassword')
    
    params = {
        'domain'    : 'mydomain.com.au',
        'email'     : 'steve',
        'password'  : '@#fwefq122442',
        'quota'     : 0
    }
    
    server.cpanel_api('Email', 'addpop', 'user1', params=params)
    

