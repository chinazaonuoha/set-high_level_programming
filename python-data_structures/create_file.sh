#!/usr/bin/bash
# This script creates a new file with the specified name and extension.
touch "$1.$2" && chmod 644 "$1.$2"