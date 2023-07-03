#!/bin/bash

# Gets the path of the script
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

# cd's into the script directory
cd "$SCRIPT_DIR"

# runs the script in the directory
python3 "$SCRIPT_DIR/resetcounter.py"

# old commands, only works with konsole iirc
#cd "$SCRIPT_DIR"

#konsole --hold --new-tab -e python3 resetcounter.py
