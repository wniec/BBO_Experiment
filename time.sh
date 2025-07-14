#!/bin/bash

# Measuring execution time
echo "Starting main.py..."
start_time=$(date +%s)

python3 main.py 0

end_time=$(date +%s)
execution_time=$((end_time - start_time))

echo "Execution time: ${execution_time} seconds"