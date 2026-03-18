#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
COMPILER_DIR="$SCRIPT_DIR/compiler"
BUILD_DIR="$COMPILER_DIR/build/python"

if [[ $# -lt 2 ]]; then
    echo "Usage: $0 inputfile outputfile"
    exit 1
fi

INPUT_FILE="$(realpath "$1")"
OUTPUT_FILE="$(realpath -m "$2")"

cd "$COMPILER_DIR" || exit 1
export PYTHONPATH="$COMPILER_DIR:$COMPILER_DIR/python:$BUILD_DIR:$PYTHONPATH"
python3 python/main.py "$INPUT_FILE" > "$OUTPUT_FILE"
