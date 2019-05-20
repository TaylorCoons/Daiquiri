#!/usr/bin/python3

import os
import re
import argparse

from AccumulatePlugins import accumulate_plugins
from GlobalDefines import ENVIRON

def validate_plugins(plugins, pluginDir):
    
    for plugin in plugins:
        pluginConfig = os.path.join(pluginDir,
                                    plugin, 
                                    plugin + 'Config.h')
        pluginHeader = os.path.join(pluginDir, 
                                    plugin, 
                                    plugin + '.h')
       
        if not os.path.isfile(pluginConfig):
            print('Could not find config file for ' + plugin)
            print(pluginConfig + ' does not exist')
            return False
        
        if not os.path.isfile(pluginHeader):
            print('Could not find header file for ' + plugin)
            print(pluginHeader + ' does not exist')
            return False
        
    return True


def main():
    print('Validating plugins')
    pluginDir = os.path.join(ENVIRON['ROOT_DIR'], ENVIRON['PLUGIN_DIR'])
    activePluginsPath = os.path.join(ENVIRON['ROOT_DIR'], ENVIRON['ACTIVE_PLUGINS_FILE'])
    plugins = accumulate_plugins(activePluginsPath)
    if not validate_plugins(plugins):
        print('Failed to validate plugins')
        return 1

    print('Plugins Validated') 
 
    return 0
 
if __name__ == "__main__":
    exit(main())
