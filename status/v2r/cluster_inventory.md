# V2R cluster inventory

2026-09-23T23:26:01.874811+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325663920128 available bytes; 81.83% used; 112501539 free inodes.

server1 `/home`: 325663920128 available bytes; 81.83% used; 112501539 free inodes.

server1 `/tmp`: 325663920128 available bytes; 81.83% used; 112501539 free inodes.

server1 `/var/tmp`: 325663920128 available bytes; 81.83% used; 112501539 free inodes.

server1 `/mnt/raid5`: 1372285308928 available bytes; 93.70% used; 337739702 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41045192704 available bytes; 97.71% used; 110432582 free inodes.

server2 `/home`: 41045192704 available bytes; 97.71% used; 110432582 free inodes.

server2 `/tmp`: 41045192704 available bytes; 97.71% used; 110432582 free inodes.

server2 `/var/tmp`: 41045192704 available bytes; 97.71% used; 110432582 free inodes.

server2 `/mnt/raid5`: 534640201728 available bytes; 96.31% used; 445205766 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292861317120 available bytes; 83.66% used; 114213236 free inodes.

server3 `/home`: 292861317120 available bytes; 83.66% used; 114213236 free inodes.

server3 `/data`: 82316124160 available bytes; 98.86% used; 225845830 free inodes.

server3 `/tmp`: 292861317120 available bytes; 83.66% used; 114213236 free inodes.

server3 `/var/tmp`: 292861317120 available bytes; 83.66% used; 114213236 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106238369792 available bytes; 94.07% used; 114352502 free inodes.

server4 `/home`: 106238369792 available bytes; 94.07% used; 114352502 free inodes.

server4 `/data`: 293097091072 available bytes; 95.95% used; 225425108 free inodes.

server4 `/tmp`: 106238369792 available bytes; 94.07% used; 114352502 free inodes.

server4 `/var/tmp`: 106238369792 available bytes; 94.07% used; 114352502 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
