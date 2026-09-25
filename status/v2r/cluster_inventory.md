# V2R cluster inventory

2026-09-25T17:57:26.345651+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318661341184 available bytes; 82.22% used; 112476341 free inodes.

server1 `/home`: 318661341184 available bytes; 82.22% used; 112476341 free inodes.

server1 `/tmp`: 318661341184 available bytes; 82.22% used; 112476341 free inodes.

server1 `/var/tmp`: 318661341184 available bytes; 82.22% used; 112476341 free inodes.

server1 `/mnt/raid5`: 371231354880 available bytes; 98.30% used; 337542570 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23105814528 available bytes; 98.71% used; 110407930 free inodes.

server2 `/home`: 23105814528 available bytes; 98.71% used; 110407930 free inodes.

server2 `/tmp`: 23105814528 available bytes; 98.71% used; 110407930 free inodes.

server2 `/var/tmp`: 23105814528 available bytes; 98.71% used; 110407930 free inodes.

server2 `/mnt/raid5`: 315254804480 available bytes; 97.82% used; 445068068 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84392923136 available bytes; 95.29% used; 114152617 free inodes.

server3 `/home`: 84392923136 available bytes; 95.29% used; 114152617 free inodes.

server3 `/data`: 132524822528 available bytes; 98.17% used; 225810597 free inodes.

server3 `/tmp`: 84392923136 available bytes; 95.29% used; 114152617 free inodes.

server3 `/var/tmp`: 84392923136 available bytes; 95.29% used; 114152617 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616781312 available bytes; 94.11% used; 114349604 free inodes.

server4 `/home`: 105616781312 available bytes; 94.11% used; 114349604 free inodes.

server4 `/data`: 229737119744 available bytes; 96.82% used; 224932467 free inodes.

server4 `/tmp`: 105616781312 available bytes; 94.11% used; 114349604 free inodes.

server4 `/var/tmp`: 105616781312 available bytes; 94.11% used; 114349604 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
