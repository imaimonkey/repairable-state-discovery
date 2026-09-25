# V2R cluster inventory

2026-09-25T15:09:11.190380+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319114526720 available bytes; 82.20% used; 112476957 free inodes.

server1 `/home`: 319114526720 available bytes; 82.20% used; 112476957 free inodes.

server1 `/tmp`: 319114526720 available bytes; 82.20% used; 112476957 free inodes.

server1 `/var/tmp`: 319114526720 available bytes; 82.20% used; 112476957 free inodes.

server1 `/mnt/raid5`: 369672634368 available bytes; 98.30% used; 337546044 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23111172096 available bytes; 98.71% used; 110407928 free inodes.

server2 `/home`: 23111172096 available bytes; 98.71% used; 110407928 free inodes.

server2 `/tmp`: 23111172096 available bytes; 98.71% used; 110407928 free inodes.

server2 `/var/tmp`: 23111172096 available bytes; 98.71% used; 110407928 free inodes.

server2 `/mnt/raid5`: 320566411264 available bytes; 97.78% used; 445073882 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84426231808 available bytes; 95.29% used; 114153448 free inodes.

server3 `/home`: 84426231808 available bytes; 95.29% used; 114153448 free inodes.

server3 `/data`: 142183911424 available bytes; 98.03% used; 225808058 free inodes.

server3 `/tmp`: 84426231808 available bytes; 95.29% used; 114153448 free inodes.

server3 `/var/tmp`: 84426231808 available bytes; 95.29% used; 114153448 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638555648 available bytes; 94.10% used; 114349692 free inodes.

server4 `/home`: 105638555648 available bytes; 94.10% used; 114349692 free inodes.

server4 `/data`: 231352606720 available bytes; 96.80% used; 224944822 free inodes.

server4 `/tmp`: 105638555648 available bytes; 94.10% used; 114349692 free inodes.

server4 `/var/tmp`: 105638555648 available bytes; 94.10% used; 114349692 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
