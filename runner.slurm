#!/bin/bash
#SBATCH --job-name=bbo_experiment_array
#SBATCH --output=logs/experiment_%A_%a.out
#SBATCH --error=logs/experiment_%A_%a.err
#SBATCH --array=0-422
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32G
#SBATCH --time=30:00:00
#SBATCH --partition=plgrid

# CONFIGURATION
REPORTS_PATH="$SCRATCH/OUTPUT"
ENV_PATH="$SCRATCH/BBO_Experiment/venv/bin/activate"

# Ensure reports directory exists
mkdir -p "$REPORTS_PATH"

# shellcheck disable=SC1090
source "$ENV_PATH"

# Run Experiment
echo "Running experiment $SLURM_ARRAY_TASK_ID"
python3 "main.py" "$SLURM_ARRAY_TASK_ID" "$REPORTS_PATH"

# shellcheck disable=SC2181
if [ $? -ne 0 ]; then
    echo "Experiment run failed for index $SLURM_ARRAY_TASK_ID"
else
    echo "Experiment run completed: $SLURM_ARRAY_TASK_ID"
fi
