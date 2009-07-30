from django.utils import simplejson as json
from copy import deepcopy

cnotes = []
new_cnotes = []

def add(message):
    new_cnotes = globals()['new_cnotes']
    new_cnotes.append(message)
    
def get():
    cnotes = globals()['cnotes']
    return cnotes
    
def get_and_clear():
    cnotes = globals()['cnotes']
    new_cnotes = globals()['new_cnotes']
    print cnotes
    print new_cnotes
    retval = deepcopy(cnotes)
    globals()['cnotes'] = []
    
    return retval
