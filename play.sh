#!/bin/bash

# Run setupo.sh using source
if [ -f setup.sh ]; then
    echo "Running setupo.sh..."
    source setup.sh
else
    echo "Error: setup.sh not found."
    exit 1
fi

# Run open.sh using bash
if [ -f open.sh ]; then
    echo "Running open.sh..."
    bash open.sh
else
    echo "Error: open.sh not found."
    exit 1
fi
sleep 2
# Run start.sh after setupo.sh completes
if [ -f start2.sh ]; then
    echo "Running start.sh..."
    bash start2.sh
else
    echo "Error: start.sh not found."
    exit 1
fi
