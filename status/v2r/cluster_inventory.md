# V2R cluster inventory

2026-09-25T12:49:56.346852+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319117860864 available bytes; 82.20% used; 112477582 free inodes.

server1 `/home`: 319117860864 available bytes; 82.20% used; 112477582 free inodes.

server1 `/tmp`: 319117860864 available bytes; 82.20% used; 112477582 free inodes.

server1 `/var/tmp`: 319117860864 available bytes; 82.20% used; 112477582 free inodes.

server1 `/mnt/raid5`: 365359063040 available bytes; 98.32% used; 337547989 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 16119357440 available bytes; 99.10% used; 110409212 free inodes.

server2 `/home`: 16119357440 available bytes; 99.10% used; 110409212 free inodes.

server2 `/tmp`: 16119357440 available bytes; 99.10% used; 110409212 free inodes.

server2 `/var/tmp`: 16119357440 available bytes; 99.10% used; 110409212 free inodes.

server2 `/mnt/raid5`: 324554657792 available bytes; 97.76% used; 445078887 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84209766400 available bytes; 95.30% used; 114154974 free inodes.

server3 `/home`: 84209766400 available bytes; 95.30% used; 114154974 free inodes.

server3 `/data`: 142275969024 available bytes; 98.03% used; 225810893 free inodes.

server3 `/tmp`: 84209766400 available bytes; 95.30% used; 114154974 free inodes.

server3 `/var/tmp`: 84209766400 available bytes; 95.30% used; 114154974 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105665507328 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665507328 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 232015593472 available bytes; 96.79% used; 224961417 free inodes.

server4 `/tmp`: 105665507328 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665507328 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
