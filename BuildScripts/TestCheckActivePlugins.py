#!/usr/bin/python3

import unittest
import sys
import os

from CheckActivePlugins import parse_active_plugins_file
from GlobalDefines import ENVIRON

class TestCheckActivePlugins(unittest.TestCase):
    def setUp(self):
        self.testDir = os.path.join(ENVIRON['ROOT_DIR'],
                                    ENVIRON['TEST_DIR'],
                                    'CheckActivePluginsTest')

    
    def test_valid_active_plugins(self):
        activePluginsPath = os.path.join(self.testDir, 'Valid.h')
        
        returnVal = parse_active_plugins_file(activePluginsPath)
    
        self.assertEqual(returnVal, True)


    def test_invalid_active_plugins(self):
        activePluginsPath = os.path.join(self.testDir, 'InvalidSymbol.h')
        
        returnVal = parse_active_plugins_file(activePluginsPath)
        
        self.assertEqual(returnVal, False)


    def test_nonexistant_active_plugins(self):
        activePluginsPath = os.path.join(self.testDir, 'NonExistant.h')
        
        returnVal = parse_active_plugins_file(activePluginsPath)

        self.assertEqual(returnVal, False)

    
if __name__=="__main__":
    unittest.main()
