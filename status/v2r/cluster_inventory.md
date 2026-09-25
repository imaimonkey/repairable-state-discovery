# V2R cluster inventory

2026-09-25T12:35:54.811712+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319125880832 available bytes; 82.20% used; 112477613 free inodes.

server1 `/home`: 319125880832 available bytes; 82.20% used; 112477613 free inodes.

server1 `/tmp`: 319125880832 available bytes; 82.20% used; 112477613 free inodes.

server1 `/var/tmp`: 319125880832 available bytes; 82.20% used; 112477613 free inodes.

server1 `/mnt/raid5`: 364278599680 available bytes; 98.33% used; 337548116 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22894010368 available bytes; 98.72% used; 110409956 free inodes.

server2 `/home`: 22894010368 available bytes; 98.72% used; 110409956 free inodes.

server2 `/tmp`: 22894010368 available bytes; 98.72% used; 110409956 free inodes.

server2 `/var/tmp`: 22894010368 available bytes; 98.72% used; 110409956 free inodes.

server2 `/mnt/raid5`: 324410540032 available bytes; 97.76% used; 445079291 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84210810880 available bytes; 95.30% used; 114154974 free inodes.

server3 `/home`: 84210810880 available bytes; 95.30% used; 114154974 free inodes.

server3 `/data`: 142283055104 available bytes; 98.03% used; 225811116 free inodes.

server3 `/tmp`: 84210810880 available bytes; 95.30% used; 114154974 free inodes.

server3 `/var/tmp`: 84210810880 available bytes; 95.30% used; 114154974 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105665916928 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665916928 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231957770240 available bytes; 96.79% used; 224963774 free inodes.

server4 `/tmp`: 105665916928 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665916928 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
