# V2R cluster inventory

2026-09-25T12:37:43.335794+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319125385216 available bytes; 82.20% used; 112477607 free inodes.

server1 `/home`: 319125385216 available bytes; 82.20% used; 112477607 free inodes.

server1 `/tmp`: 319125385216 available bytes; 82.20% used; 112477607 free inodes.

server1 `/var/tmp`: 319125385216 available bytes; 82.20% used; 112477607 free inodes.

server1 `/mnt/raid5`: 364273795072 available bytes; 98.33% used; 337548105 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22974996480 available bytes; 98.72% used; 110409446 free inodes.

server2 `/home`: 22974996480 available bytes; 98.72% used; 110409446 free inodes.

server2 `/tmp`: 22974996480 available bytes; 98.72% used; 110409446 free inodes.

server2 `/var/tmp`: 22974996480 available bytes; 98.72% used; 110409446 free inodes.

server2 `/mnt/raid5`: 324908105728 available bytes; 97.75% used; 445079384 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84210278400 available bytes; 95.30% used; 114154974 free inodes.

server3 `/home`: 84210278400 available bytes; 95.30% used; 114154974 free inodes.

server3 `/data`: 142281740288 available bytes; 98.03% used; 225811084 free inodes.

server3 `/tmp`: 84210278400 available bytes; 95.30% used; 114154974 free inodes.

server3 `/var/tmp`: 84210278400 available bytes; 95.30% used; 114154974 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105665855488 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665855488 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231953317888 available bytes; 96.79% used; 224963523 free inodes.

server4 `/tmp`: 105665855488 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665855488 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
