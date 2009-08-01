from django.test import TestCase
from django.http import HttpRequest, HttpResponse

from cnotes.middleware import CnotesHandlerMiddleware

class CnotesTests(TestCase):
    
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
        cnotes.add('Test Message')
        mware = CnotesHandlerMiddleware()
        request = self._get_no_cookie_request()
        orig_response = self._get_response()
        response = mware.process_response(request, orig_response)
        expected_key = "cnotes"
        expected_value =  "715ea66a12e8953126e44e0de53d8c5f840a63ae:KGxwMQpTJ1Rlc3QgTWVzc2FnZScKcDIKYS4="
        # FIXME: Add a cookie morsel as the compairson
        self.assertEquals(response.cookies['cnotes'].key, expected_key)
        self.assertEquals(response.cookies['cnotes'].value, expected_value)
        