# V2R cluster inventory

2026-09-24T20:57:22.142592+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323979730944 available bytes; 81.93% used; 112481435 free inodes.

server1 `/home`: 323979730944 available bytes; 81.93% used; 112481435 free inodes.

server1 `/tmp`: 323979730944 available bytes; 81.93% used; 112481435 free inodes.

server1 `/var/tmp`: 323979730944 available bytes; 81.93% used; 112481435 free inodes.

server1 `/mnt/raid5`: 415564230656 available bytes; 98.09% used; 337631276 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30143680512 available bytes; 98.32% used; 110411380 free inodes.

server2 `/home`: 30143680512 available bytes; 98.32% used; 110411380 free inodes.

server2 `/tmp`: 30143680512 available bytes; 98.32% used; 110411380 free inodes.

server2 `/var/tmp`: 30143680512 available bytes; 98.32% used; 110411380 free inodes.

server2 `/mnt/raid5`: 491440058368 available bytes; 96.60% used; 445156114 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84385558528 available bytes; 95.29% used; 114156103 free inodes.

server3 `/home`: 84385558528 available bytes; 95.29% used; 114156103 free inodes.

server3 `/data`: 150927298560 available bytes; 97.91% used; 225803806 free inodes.

server3 `/tmp`: 84385558528 available bytes; 95.29% used; 114156103 free inodes.

server3 `/var/tmp`: 84385558528 available bytes; 95.29% used; 114156103 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639178240 available bytes; 94.10% used; 114348377 free inodes.

server4 `/home`: 105639178240 available bytes; 94.10% used; 114348377 free inodes.

server4 `/data`: 77656031232 available bytes; 98.93% used; 225255468 free inodes.

server4 `/tmp`: 105639178240 available bytes; 94.10% used; 114348377 free inodes.

server4 `/var/tmp`: 105639178240 available bytes; 94.10% used; 114348377 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
