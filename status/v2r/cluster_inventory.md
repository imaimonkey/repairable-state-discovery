# V2R cluster inventory

2026-09-24T20:35:46.901996+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323981955072 available bytes; 81.93% used; 112481433 free inodes.

server1 `/home`: 323981955072 available bytes; 81.93% used; 112481433 free inodes.

server1 `/tmp`: 323981955072 available bytes; 81.93% used; 112481433 free inodes.

server1 `/var/tmp`: 323981955072 available bytes; 81.93% used; 112481433 free inodes.

server1 `/mnt/raid5`: 415611027456 available bytes; 98.09% used; 337633792 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30151405568 available bytes; 98.32% used; 110411376 free inodes.

server2 `/home`: 30151405568 available bytes; 98.32% used; 110411376 free inodes.

server2 `/tmp`: 30151405568 available bytes; 98.32% used; 110411376 free inodes.

server2 `/var/tmp`: 30151405568 available bytes; 98.32% used; 110411376 free inodes.

server2 `/mnt/raid5`: 492099411968 available bytes; 96.60% used; 445156897 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84397166592 available bytes; 95.29% used; 114156104 free inodes.

server3 `/home`: 84397166592 available bytes; 95.29% used; 114156104 free inodes.

server3 `/data`: 151376179200 available bytes; 97.91% used; 225804259 free inodes.

server3 `/tmp`: 84397166592 available bytes; 95.29% used; 114156104 free inodes.

server3 `/var/tmp`: 84397166592 available bytes; 95.29% used; 114156104 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105640026112 available bytes; 94.10% used; 114348380 free inodes.

server4 `/home`: 105640026112 available bytes; 94.10% used; 114348380 free inodes.

server4 `/data`: 85462171648 available bytes; 98.82% used; 225257640 free inodes.

server4 `/tmp`: 105640026112 available bytes; 94.10% used; 114348380 free inodes.

server4 `/var/tmp`: 105640026112 available bytes; 94.10% used; 114348380 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
