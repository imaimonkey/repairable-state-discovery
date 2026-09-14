# Latest experiment handoff

- Repository: `repairable-state-discovery`
- Source commit: `be41174d1a93e7fff6cddb4727444b1c51663fc0`
- Branch: `idea/unbiased-repair-eval`
- Status: **blocked before execution**
- Slurm job: `47076`
- Dependency: `afterok:47075(failed)`
- Run path: `not created`
- Analysis source: `not created`

The job requested one GPU, 8 CPUs, and 64G memory, but Slurm reported
`DependencyNeverSatisfied`. No evaluator code ran and no new repairability
metric was produced by this session. Existing historical result artifacts were
preserved and are not relabeled as this run's result.

The next permitted action is a fresh submission after the KeyFinder
evaluation-integrity failure is repaired and verified.
