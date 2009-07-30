=============
Django Cnotes
=============

Django cnotes provides a simple cookie based user notification system.


Installation
============

1. Add the `cnotes` directory to your python path.
1. Add `cnotes.middleware.CnotesHandlerMiddleware` to the `MIDDLEWARE_CLASSES` variable in your `settings.py` file.


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