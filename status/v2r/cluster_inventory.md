# V2R cluster inventory

2026-09-25T19:26:08.162773+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318735896576 available bytes; 82.22% used; 112476332 free inodes.

server1 `/home`: 318735896576 available bytes; 82.22% used; 112476332 free inodes.

server1 `/tmp`: 318735896576 available bytes; 82.22% used; 112476332 free inodes.

server1 `/var/tmp`: 318735896576 available bytes; 82.22% used; 112476332 free inodes.

server1 `/mnt/raid5`: 370868224000 available bytes; 98.30% used; 337540808 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23094996992 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23094996992 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23094996992 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23094996992 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 311657234432 available bytes; 97.85% used; 445064691 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382744576 available bytes; 95.29% used; 114152627 free inodes.

server3 `/home`: 84382744576 available bytes; 95.29% used; 114152627 free inodes.

server3 `/data`: 129279823872 available bytes; 98.21% used; 225808665 free inodes.

server3 `/tmp`: 84382744576 available bytes; 95.29% used; 114152627 free inodes.

server3 `/var/tmp`: 84382744576 available bytes; 95.29% used; 114152627 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674932224 available bytes; 94.10% used; 114349586 free inodes.

server4 `/home`: 105674932224 available bytes; 94.10% used; 114349586 free inodes.

server4 `/data`: 229633048576 available bytes; 96.83% used; 224930106 free inodes.

server4 `/tmp`: 105674932224 available bytes; 94.10% used; 114349586 free inodes.

server4 `/var/tmp`: 105674932224 available bytes; 94.10% used; 114349586 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
