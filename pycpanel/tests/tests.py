import pycpanel
import unittest

""" Your server details """

hostname = 'my.cpanelserver.com'
hash = "hash without line breaks"
password = 'password'
cpanel_user = 'user'  #not root


""" Tests begin """


class PyCpanelTest(unittest.TestCase):
    def setUp(self):
  
        """Test Password Authentication"""

        self.server = pycpanel.conn(hostname=hostname, password=password)
        
    def testOne(self):

        """Test External API Call"""

        raised = False
        try:
            result = self.server.api('listaccts')
            if result['status'] == 0: raised = True
        except: raised = True
        self.assertFalse(raised, 'Exception raised')

    def testTwo(self):

        """Test API 2 Function"""

        raised = False
        try:
            result = self.server.cpanel_api('Email', 'listpops', cpanel_user)
            found = False
            for email in result:
                if email['email'] == cpanel_user: found = True
        except: raised = True
        self.assertFalse(raised, 'Exception raised')

    def testThree(self):

        """Test Hash Authentication"""

        raised = False
        try:
            pycpanel.conn(hostname=hostname, hash=hash)
        except: raised = True
        self.assertFalse(raised, 'Exception raised')

    def testFour(self):

        """Test CSF Allow"""

        try:
            result = self.server.csf.allow('192.168.1.1')
        except: result = False
        self.assertTrue(result, 'Exception raised')

    def testFive(self):

        """Test CSF Deny"""

        try:
            result = self.server.csf.deny('192.168.1.1')
        except: result = False
        self.assertTrue(result, 'Exception raised')

    def testSix(self):

        """Test CSF Unblock"""

        try:
            result = self.server.csf.unblock('192.168.1.1')
        except: result = False
        self.assertTrue(result, 'Exception raised')
   

    def testSeven(self):

        """Test CSF Ignore"""

        try:
            result = self.server.csf.ignore('192.168.1.1')
        except: result = False
        self.assertTrue(result, 'Exception raised')


def main():
    unittest.main()

if __name__ == '__main__':
    main()


