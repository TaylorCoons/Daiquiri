#!/usr/bin/python3

import unittest
import sys
import os

from ValidatePlugins import validate_plugins
from GlobalDefines import ENVIRON

class TestValidatePlugins(unittest.TestCase):
    def setUp(self):
        self.testDir = os.path.join(ENVIRON['ROOT_DIR'],
                                    ENVIRON['TEST_DIR'],
                                    'ValidatePluginsTest')

    def test_valid_plugins(self):
        pluginsPath = os.path.join(self.testDir, 'ValidPlugins')
        
        returnVal = validate_plugins(['Plugin1', 'Plugin2', 'Plugin3'], pluginsPath)

        self.assertEqual(returnVal, True)

    
    def test_invalid_plugins(self):
        pluginsPath = os.path.join(self.testDir, 'NoHeader')
        
        returnVal = validate_plugins(['Plugin'], pluginsPath)

        self.assertEqual(returnVal, False)
    
        pluginsPath = os.path.join(self.testDir, 'NoConfig')
        
        returnVal = validate_plugins(['Plugin'], pluginsPath)

        self.assertEqual(returnVal, False)

        pluginsPath = os.path.join(self.testDir, 'MissingPlugin')
    
        returnVal = validate_plugins(['Plugin1', 'Plugin2', 'Plugin3'], pluginsPath)

        self.assertEqual(returnVal, False)

if __name__=="__main__":
    unittest.main()

