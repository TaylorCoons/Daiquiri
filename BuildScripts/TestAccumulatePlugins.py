#!/usr/bin/python3

import unittest
import sys
import os

from AccumulatePlugins import accumulate_plugins
from GlobalDefines import ENVIRON

class TestAccumulatePlugins(unittest.TestCase):
    def setUp(self):
        self.testDir = os.path.join(ENVIRON['ROOT_DIR'],
                               ENVIRON['TEST_DIR'],
                               'AccumulatePluginsTest')


    def test_valid_plugins(self):
        activePluginsPath = os.path.join(self.testDir, 'Plugins3.h')
        
        plugins = accumulate_plugins(activePluginsPath)
    
        self.assertEqual(len(plugins), 3)    
        self.assertEqual(plugins, ['plugin1', 'plugin2', 'plugin3'])

        activePluginsPath = os.path.join(self.testDir, 'Plugins4.h')

        plugins = accumulate_plugins(activePluginsPath)
        
        self.assertEqual(len(plugins), 4)
        self.assertEqual(plugins, ['plugin1', 'plugin2', 'plugin3', 'plugin4'])    
    
    
    def test_empty_plugins(self):
        activePluginsPath = os.path.join(self.testDir, 'Empty.h')
        
        plugins = accumulate_plugins(activePluginsPath)
        
        self.assertEqual(len(plugins), 0)
        self.assertEqual(plugins, [])

    def test_invalid_plugin(self):
        activePluginsPath = os.path.join(self.testDir, 'NonExistant.h')
        
        plugins = accumulate_plugins(activePluginsPath)

        self.assertEqual(len(plugins), 0)
        self.assertEqual(plugins, [])

    
if __name__=="__main__":
    unittest.main()
