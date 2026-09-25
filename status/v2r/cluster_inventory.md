# V2R cluster inventory

2026-09-25T16:05:44.789954+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318674849792 available bytes; 82.22% used; 112476515 free inodes.

server1 `/home`: 318674849792 available bytes; 82.22% used; 112476515 free inodes.

server1 `/tmp`: 318674849792 available bytes; 82.22% used; 112476515 free inodes.

server1 `/var/tmp`: 318674849792 available bytes; 82.22% used; 112476515 free inodes.

server1 `/mnt/raid5`: 363943374848 available bytes; 98.33% used; 337545199 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23116402688 available bytes; 98.71% used; 110407944 free inodes.

server2 `/home`: 23116402688 available bytes; 98.71% used; 110407944 free inodes.

server2 `/tmp`: 23116402688 available bytes; 98.71% used; 110407944 free inodes.

server2 `/var/tmp`: 23116402688 available bytes; 98.71% used; 110407944 free inodes.

server2 `/mnt/raid5`: 319068487680 available bytes; 97.80% used; 445071406 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84402819072 available bytes; 95.29% used; 114152682 free inodes.

server3 `/home`: 84402819072 available bytes; 95.29% used; 114152682 free inodes.

server3 `/data`: 135967256576 available bytes; 98.12% used; 225806391 free inodes.

server3 `/tmp`: 84402819072 available bytes; 95.29% used; 114152682 free inodes.

server3 `/var/tmp`: 84402819072 available bytes; 95.29% used; 114152682 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636876288 available bytes; 94.11% used; 114349663 free inodes.

server4 `/home`: 105636876288 available bytes; 94.11% used; 114349663 free inodes.

server4 `/data`: 231291318272 available bytes; 96.80% used; 224943233 free inodes.

server4 `/tmp`: 105636876288 available bytes; 94.11% used; 114349663 free inodes.

server4 `/var/tmp`: 105636876288 available bytes; 94.11% used; 114349663 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
