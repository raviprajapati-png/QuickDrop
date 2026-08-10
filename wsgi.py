import os
import sys

# Add your project configuration folder to Python's path
sys.path.append(os.path.dirname(__file__))

from quickdrop_project.wsgi import application

app = application