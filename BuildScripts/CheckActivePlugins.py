#!/usr/bin/python3

import argparse
import os
import re

import GlobalDefines as GD 

def parse_arguments():
    parser = argparse.ArgumentParser()
    defaultPath = os.path.join(GD.ROOT_DIR, GD.ACTIVE_PLUGINS_FILE)
    parser.add_argument('--path', 
                        nargs=1, 
                        default=defaultPath, 
                        help='Non-conventional path to active plugins file')
    
    args = parser.parse_args()
    return args    

def parse_active_plugins_file(activePluginsPath):
    activePlugins = open(activePluginsPath, 'r')
    if not activePlugins:
        print('Failed to open active plugins file')
        print('Could not open: ' + activePluginsPath)
        return False
  
    reEngineBlank = re.compile('^[\s\t]*$', re.MULTILINE)
    reEngineInclude = re.compile('#include .*', re.MULTILINE)
  
    lines = activePlugins.readlines()
    
    lineNumber = 1    

    for line in lines:
        if (reEngineBlank.match(line) is None and
                reEngineInclude.match(line) is None):
            print('Unexpected symbol in ' + activePluginsPath)
            print('Line: ' + str(lineNumber) + ' Data: ' + line)
            return False

        lineNumber = lineNumber + 1

    activePlugins.close()

    return True


def main():
    print('Validating Active Plugins file')
    args = parse_arguments() 
    if not os.path.isfile(args.path):
        print('Failed to find active plugins file')
        print('File does not exist at: ' + args.path)    
        return 1

    if not parse_active_plugins_file(args.path):
        print('Failed to parse active plugins file')
        return 1

    print('Active Plugins Validated') 

    return 0    


if __name__ == "__main__":
    main()
