# V2R cluster inventory

2026-09-25T11:16:13.709217+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319061258240 available bytes; 82.20% used; 112478867 free inodes.

server1 `/home`: 319061258240 available bytes; 82.20% used; 112478867 free inodes.

server1 `/tmp`: 319061258240 available bytes; 82.20% used; 112478867 free inodes.

server1 `/var/tmp`: 319061258240 available bytes; 82.20% used; 112478867 free inodes.

server1 `/mnt/raid5`: 366617595904 available bytes; 98.32% used; 337554589 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] |

server2 `/`: 22907047936 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22907047936 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22907047936 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22907047936 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 328616734720 available bytes; 97.73% used; 445088345 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84139843584 available bytes; 95.30% used; 114155492 free inodes.

server3 `/home`: 84139843584 available bytes; 95.30% used; 114155492 free inodes.

server3 `/data`: 142083530752 available bytes; 98.04% used; 225814425 free inodes.

server3 `/tmp`: 84139843584 available bytes; 95.30% used; 114155492 free inodes.

server3 `/var/tmp`: 84139843584 available bytes; 95.30% used; 114155492 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105611898880 available bytes; 94.11% used; 114350250 free inodes.

server4 `/home`: 105611898880 available bytes; 94.11% used; 114350250 free inodes.

server4 `/data`: 238633275392 available bytes; 96.70% used; 224981779 free inodes.

server4 `/tmp`: 105611898880 available bytes; 94.11% used; 114350250 free inodes.

server4 `/var/tmp`: 105611898880 available bytes; 94.11% used; 114350250 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
