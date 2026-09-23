# Live monitor

`live_monitor.py` performs one read-only observation cycle. It collects
Slurm state from the controller and existing artifact metadata from server1,
server2, and server4 when the normal SSH credential permits access. It writes
only `status/live/`, commits the snapshot, and pushes the monitoring branch.

`run_monitor_loop.sh` holds a user-level `flock`, waits 30 minutes between
cycles, and continues after a failed cycle. It does not restart or alter any
scientific job.
