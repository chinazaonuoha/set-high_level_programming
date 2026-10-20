#!/usr/bin/bash
# This script creates a new file with an optional extension.

# If no second argument is provided, just use the first argument
if [ -z "$2" ]; then
    filename="$1"
else
    filename="$1.$2"
fi

touch "$filename" && chmod 755 "$filename"