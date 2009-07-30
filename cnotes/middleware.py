# Barrowed from David Cramer http://www.davidcramer.net/code/62/set-cookies-without-a-response-in-django.html
from Cookie import SimpleCookie, Morsel
import copy, cPickle as Pickle
 
class CnotesHandlerMiddleware(object):
    """
    This middleware modifies request.COOKIES and adds a set and delete method.
 
    `set` matches django.http.HttpResponse.set_cookie
    `delete` matches django.http.HttpResponse.delete_cookie
 
    This should be the first middleware you load.
    """
    def process_request(self, request):
        import cnotes
        raw = request.COOKIES.get('cnotes', None)
        if raw:
            cnotes.cnotes = Pickle.loads(raw)
        else:
            cnotes.cnotes = []
            
    def process_response(self, request, response):
        import cnotes
        data = cnotes.cnotes + cnotes.new_cnotes
        cnotes.new_cnotes = []
        response.set_cookie('cnotes', Pickle.dumps(data))
        
        return response
    