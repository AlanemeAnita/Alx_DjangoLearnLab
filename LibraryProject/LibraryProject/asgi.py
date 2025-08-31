<<<<<<< HEAD
ECHO is on.
=======
"""
ASGI config for LibraryProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

application = get_asgi_application()
>>>>>>> 583b81e80b5cdd4f9a8ccb418026dcfbce6e52de
