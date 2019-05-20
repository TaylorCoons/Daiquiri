#!/usr/bin/python3

import os
import re
import argparse

import GlobalDefines as GD
from AccumulatePlugins import accumulate_plugins

def validate_plugins(plugins):
    
    for plugin in plugins:
        pluginConfig = os.path.join(GD.ROOT_DIR, 
                                    GD.PLUGIN_DIR, 
                                    plugin, 
                                    plugin + 'Config.h')
        pluginHeader = os.path.join(GD.ROOT_DIR, 
                                    GD.PLUGIN_DIR, 
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
    plugins = accumulate_plugins()
    if not validate_plugins(plugins):
        print('Failed to validate plugins')
        return 1

    print('Plugins Validated') 
 
    return 0
 
if __name__ == "__main__":
    exit(main())
