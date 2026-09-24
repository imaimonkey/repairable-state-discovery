# V2R cluster inventory

2026-09-24T04:06:44.534315+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324717404160 available bytes; 81.89% used; 112493469 free inodes.

server1 `/home`: 324717404160 available bytes; 81.89% used; 112493469 free inodes.

server1 `/tmp`: 324717404160 available bytes; 81.89% used; 112493469 free inodes.

server1 `/var/tmp`: 324717404160 available bytes; 81.89% used; 112493469 free inodes.

server1 `/mnt/raid5`: 421466804224 available bytes; 98.07% used; 337724765 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40802811904 available bytes; 97.72% used; 110430828 free inodes.

server2 `/home`: 40802811904 available bytes; 97.72% used; 110430828 free inodes.

server2 `/tmp`: 40802811904 available bytes; 97.72% used; 110430828 free inodes.

server2 `/var/tmp`: 40802811904 available bytes; 97.72% used; 110430828 free inodes.

server2 `/mnt/raid5`: 526082957312 available bytes; 96.36% used; 445196687 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292027731968 available bytes; 83.70% used; 114176973 free inodes.

server3 `/home`: 292027731968 available bytes; 83.70% used; 114176973 free inodes.

server3 `/data`: 31739203584 available bytes; 99.56% used; 225841918 free inodes.

server3 `/tmp`: 292027731968 available bytes; 83.70% used; 114176973 free inodes.

server3 `/var/tmp`: 292027731968 available bytes; 83.70% used; 114176973 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105791074304 available bytes; 94.10% used; 114349490 free inodes.

server4 `/home`: 105791074304 available bytes; 94.10% used; 114349490 free inodes.

server4 `/data`: 256731422720 available bytes; 96.45% used; 225381884 free inodes.

server4 `/tmp`: 105791074304 available bytes; 94.10% used; 114349490 free inodes.

server4 `/var/tmp`: 105791074304 available bytes; 94.10% used; 114349490 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
