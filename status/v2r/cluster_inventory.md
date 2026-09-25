# V2R cluster inventory

2026-09-25T07:05:37.341734+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318873038848 available bytes; 82.21% used; 112480379 free inodes.

server1 `/home`: 318873038848 available bytes; 82.21% used; 112480379 free inodes.

server1 `/tmp`: 318873038848 available bytes; 82.21% used; 112480379 free inodes.

server1 `/var/tmp`: 318873038848 available bytes; 82.21% used; 112480379 free inodes.

server1 `/mnt/raid5`: 399691141120 available bytes; 98.17% used; 337560435 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22872686592 available bytes; 98.72% used; 110410532 free inodes.

server2 `/home`: 22872686592 available bytes; 98.72% used; 110410532 free inodes.

server2 `/tmp`: 22872686592 available bytes; 98.72% used; 110410532 free inodes.

server2 `/var/tmp`: 22872686592 available bytes; 98.72% used; 110410532 free inodes.

server2 `/mnt/raid5`: 330406928384 available bytes; 97.72% used; 445097984 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84446720000 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84446720000 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142455361536 available bytes; 98.03% used; 225813129 free inodes.

server3 `/tmp`: 84446720000 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84446720000 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638617088 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638617088 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249493049344 available bytes; 96.55% used; 225016886 free inodes.

server4 `/tmp`: 105638617088 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638617088 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
