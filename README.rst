=============
Django Cnotes
=============

Django cnotes provides a simple cookie based user notification system.  

Why not use Django's own `messaging system <http://docs.djangoproject.com/en/dev/topics/auth/#messages>`_ or `django-notification <http://github.com/jtauber/django-notification/tree/master>`_?  While both good solutions, they are a bit more heavy weight than cnotes.  Specifically they can only send messages to logged in users and they involve hitting the database to find any queued messages.  

Cntoes is different in that it keeps all messaging information in signed cookies and memory.  This way it can send, tamper-proof notifications to both authenticated and anonymous users, without ever touching the database.


Installation
============

1. Add the `cnotes` directory to your python path.
2. Add `cnotes.middleware.CnotesHandlerMiddleware` to the `MIDDLEWARE_CLASSES` variable in your `settings.py` file.


Usage
=====

Adding new messages::

	import cnotes
	cnotes.add('My message')
	
Getting, clearing and printing all existing messages::

	import cnotes
	notes = cnotes.get_and_clear()
	for note in notes:
		print note
		
Similar action without clearing::

	import cnotes
	notes = cnotes.get()
	for note in notes:
		print note
		
You can also access cnotes from the request object::

	def my_view(request):
		
		messages = request.cnotes
		
		return render_to_response( 'my_view.html'), {
			'messages': messages,
		})
		
Settings
========

	CNOTES_AUTO_CLEAR
		If set to ``True`` (default) the cnotes middlware will clear messages one they have been made available on a non-ajax request object.