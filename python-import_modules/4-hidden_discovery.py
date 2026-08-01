#!/usr/bin/env python3
import importlib.util

def print_hidden_names():
    file_path = "hidden_4.pyc"
    
    # Load the compiled .pyc module dynamically for Python 3.8
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Extract names, filter out any starting with '__', and sort alphabetically
    names = sorted(name for name in dir(module) if not name.startswith("__"))
    
    # Print each name on a new line
    for name in names:
        print(name)

if __name__ == "__main__":
    print_hidden_names()