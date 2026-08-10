import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from quickdrop_project.wsgi import application

app = application