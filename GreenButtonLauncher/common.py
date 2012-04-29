'''
Created on Apr 28, 2012

@author: Bryan
'''
import sys
import os

SITE_ROOT = "/Users/Bryan/Documents/Aptana Studio 3 Workspace/GreenButtonLauncher"
PROJECT_ROOT = os.path.join(SITE_ROOT,"GreenButtonLauncher")

sys.path.append(SITE_ROOT)
sys.path.append(PROJECT_ROOT + '/apps')