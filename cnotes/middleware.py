
from Cookie import SimpleCookie, Morsel
import copy, cPickle as Pickle
 
class CnotesHandlerMiddleware(object):
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
    