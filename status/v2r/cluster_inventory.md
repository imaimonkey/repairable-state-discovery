# V2R cluster inventory

2026-09-25T20:07:25.479292+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318720311296 available bytes; 82.22% used; 112476348 free inodes.

server1 `/home`: 318720311296 available bytes; 82.22% used; 112476348 free inodes.

server1 `/tmp`: 318720311296 available bytes; 82.22% used; 112476348 free inodes.

server1 `/var/tmp`: 318720311296 available bytes; 82.22% used; 112476348 free inodes.

server1 `/mnt/raid5`: 370799423488 available bytes; 98.30% used; 337540614 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23095554048 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23095554048 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23095554048 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23095554048 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 311053516800 available bytes; 97.85% used; 445063443 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382924800 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84382924800 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 127193620480 available bytes; 98.24% used; 225808403 free inodes.

server3 `/tmp`: 84382924800 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84382924800 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105673596928 available bytes; 94.10% used; 114349572 free inodes.

server4 `/home`: 105673596928 available bytes; 94.10% used; 114349572 free inodes.

server4 `/data`: 229427048448 available bytes; 96.83% used; 224929206 free inodes.

server4 `/tmp`: 105673596928 available bytes; 94.10% used; 114349572 free inodes.

server4 `/var/tmp`: 105673596928 available bytes; 94.10% used; 114349572 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
