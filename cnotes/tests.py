import hmac
import base64

try:
    from hashlib import sha1
except ImportError:
    # Compatibility with older versions of Python
    from md5 import new as sha1
    
import cPickle as Pickle

from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.conf import settings


from cnotes.middleware import CnotesHandlerMiddleware


class CnotesTests(TestCase):
    
    
    def setUp(self):
        self.clear_text = 'Test Message'
        data = [self.clear_text]
        encoded = base64.urlsafe_b64encode(Pickle.dumps(data))
        self.key = 'cnotes'
        digest =  hmac.new(settings.SECRET_KEY, ':'.join([self.key, encoded]), sha1).hexdigest()
        self.signed = '%s:%s' % (digest, encoded)
        
    
    def _get_no_cookie_request(self):
        return HttpRequest()
        
    def _get_response(self):
        return HttpResponse()
        
    def testNoCookieRead(self):
        request = self._get_no_cookie_request()
        mware = CnotesHandlerMiddleware()
        mware.process_request(request)
        
        self.assertEquals(request.cnotes, [])
        
    def testAddCnote(self):
        import cnotes
        cnotes.add(self.clear_text)
        mware = CnotesHandlerMiddleware()
        request = self._get_no_cookie_request()
        orig_response = self._get_response()
        response = mware.process_response(request, orig_response)
        expected_key = self.key
        expected_value =  self.signed
        # FIXME: Add a cookie morsel as the compairson
        self.assertEquals(response.cookies['cnotes'].key, expected_key)
        self.assertEquals(response.cookies['cnotes'].value, expected_value)
        