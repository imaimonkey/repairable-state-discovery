# V2R cluster inventory

2026-09-24T03:50:54.022193+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324738842624 available bytes; 81.88% used; 112493674 free inodes.

server1 `/home`: 324738842624 available bytes; 81.88% used; 112493674 free inodes.

server1 `/tmp`: 324738842624 available bytes; 81.88% used; 112493674 free inodes.

server1 `/var/tmp`: 324738842624 available bytes; 81.88% used; 112493674 free inodes.

server1 `/mnt/raid5`: 406964260864 available bytes; 98.13% used; 337724808 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40817012736 available bytes; 97.72% used; 110430946 free inodes.

server2 `/home`: 40817012736 available bytes; 97.72% used; 110430946 free inodes.

server2 `/tmp`: 40817012736 available bytes; 97.72% used; 110430946 free inodes.

server2 `/var/tmp`: 40817012736 available bytes; 97.72% used; 110430946 free inodes.

server2 `/mnt/raid5`: 526575239168 available bytes; 96.36% used; 445197169 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292362371072 available bytes; 83.69% used; 114197804 free inodes.

server3 `/home`: 292362371072 available bytes; 83.69% used; 114197804 free inodes.

server3 `/data`: 33874604032 available bytes; 99.53% used; 225842577 free inodes.

server3 `/tmp`: 292362371072 available bytes; 83.69% used; 114197804 free inodes.

server3 `/var/tmp`: 292362371072 available bytes; 83.69% used; 114197804 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105792565248 available bytes; 94.10% used; 114349566 free inodes.

server4 `/home`: 105792565248 available bytes; 94.10% used; 114349566 free inodes.

server4 `/data`: 275186393088 available bytes; 96.20% used; 225384091 free inodes.

server4 `/tmp`: 105792565248 available bytes; 94.10% used; 114349566 free inodes.

server4 `/var/tmp`: 105792565248 available bytes; 94.10% used; 114349566 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
