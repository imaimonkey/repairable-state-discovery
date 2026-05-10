#!/bin/bash
#SBATCH --job-name=repair_phase1
#SBATCH --output=/home/kimhj/repairable-state-discovery/logs/protocol_phase1_%j.out
#SBATCH --error=/home/kimhj/repairable-state-discovery/logs/protocol_phase1_%j.err
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=96G
#SBATCH --time=9999:00:00
#SBATCH --nodelist=devbox

exec "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/run_protocol_phase1.sh" "$@"
