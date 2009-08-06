import hmac
import re
import base64
try:
    from hashlib import sha1
except ImportError:
    # Compatibility with older versions of Python
    from md5 import new as sha1
from Cookie import SimpleCookie, Morsel
import copy, cPickle as Pickle
from django.core.exceptions import SuspiciousOperation
from django.conf import settings

 
class CnotesHandlerMiddleware(object):
    regex = re.compile(r'(?:([0-9a-f]+):)?(.*)')
    def process_request(self, request):
        import cnotes
        raw = request.COOKIES.get('cnotes', None)
        if raw:
            try:
                raw = base64.urlsafe_b64decode(self.unsign('cnotes', raw))
                cnotes.cnotes = Pickle.loads(raw)
            except SuspiciousOperation:
                cnotes.cnotes = []
        else:
            cnotes.cnotes = []
            
        request.cnotes = cnotes.cnotes
            
    def process_response(self, request, response):
        import cnotes
        data = cnotes.new_cnotes
        signed_data = self.sign('cnotes', base64.urlsafe_b64encode(Pickle.dumps(data)))
        response.set_cookie('cnotes', signed_data)
        auto_clear = getattr(settings, 'CNOTES_AUTO_CLEAR', True)
        if auto_clear and not request.is_ajax():
            cnotes.new_cnotes = []
        
        return response

    # The following are borrowed from Gulopine's django-signedcookies project
    # http://django-signedcookies.googlecode.com/
    def get_digest(self, key, value):
        digest =  hmac.new(settings.SECRET_KEY, ':'.join([key, value]), sha1).hexdigest()
        return digest

    def sign(self, key, unsigned_value):
        return '%s:%s' % (self.get_digest(key, unsigned_value), unsigned_value)
        
    def unsign(self, key, signed_value):
        signature, unsigned_value = self.regex.match(signed_value).groups()
        if not signature or self.get_digest(key, unsigned_value) != signature:
            raise SuspiciousOperation, "'%s' was not properly signed." % key
        return unsigned_value