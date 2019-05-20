#!/usr/bin/python3

import os
import re

from GlobalDefines import ENVIRON

def accumulate_plugins(activePluginsPath):
    
    try:
        activePluginsFile = open(activePluginsPath, 'r')
    except FileNotFoundError as e:
        print(e)
        return []

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
        
    activePluginsFile.close()

    return plugins
