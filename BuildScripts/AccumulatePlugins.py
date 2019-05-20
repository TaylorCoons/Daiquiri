#!/usr/bin/python3

import os
import re

import GlobalDefines as GD

def accumulate_plugins():
    activePluginsPath = os.path.join(GD.ROOT_DIR, GD.ACTIVE_PLUGINS_FILE)
    activePluginsFile = open(activePluginsPath, 'r')
    
    reEngine = re.compile('#include "(?P<plugin>.*)\.h"')

    plugins = []

    if not activePluginsFile:
        print('Failed to open active plugins file')
        print('Could not open: ' + activePluginsPath)
        return []
   
    lines = activePluginsFile.readlines() 
    for line in lines:
        match = reEngine.match(line)
        if match is not None:
            plugins.append(match.group('plugin'))
        
    return plugins
