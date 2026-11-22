#!/bin/bash
SCRIPT_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"
for PYTHON_CANDIDATE in "$SCRIPT_DIR/.venv/bin/python" /opt/homebrew/bin/python3 /usr/local/bin/python3 "$(command -v python3)" /usr/bin/python3; do
  if [ -x "$PYTHON_CANDIDATE" ] && "$PYTHON_CANDIDATE" -c 'import sys; sys.exit(sys.version_info < (3, 9))' 2>/dev/null; then
    "$PYTHON_CANDIDATE" "$SCRIPT_DIR/tools/reader/launch_library.py" "$@"
    RESULT=$?
    if [ "$RESULT" -ne 0 ]; then
      printf '\nLibrary startup stopped. See the message above. Press Return to close.\n'
      read -r
    fi
    exit "$RESULT"
  fi
done
printf 'Python 3.9 or newer is required. Install Python 3, then double-click this file again.\nPress Return to close.\n'
read -r
exit 1
