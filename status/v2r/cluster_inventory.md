# V2R cluster inventory

2026-09-24T00:43:18.845361+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325540126720 available bytes; 81.84% used; 112500453 free inodes.

server1 `/home`: 325540126720 available bytes; 81.84% used; 112500453 free inodes.

server1 `/tmp`: 325540126720 available bytes; 81.84% used; 112500453 free inodes.

server1 `/var/tmp`: 325540126720 available bytes; 81.84% used; 112500453 free inodes.

server1 `/mnt/raid5`: 1088255787008 available bytes; 95.01% used; 337735002 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40983179264 available bytes; 97.71% used; 110432289 free inodes.

server2 `/home`: 40983179264 available bytes; 97.71% used; 110432289 free inodes.

server2 `/tmp`: 40983179264 available bytes; 97.71% used; 110432289 free inodes.

server2 `/var/tmp`: 40983179264 available bytes; 97.71% used; 110432289 free inodes.

server2 `/mnt/raid5`: 531829473280 available bytes; 96.33% used; 445202768 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292050841600 available bytes; 83.70% used; 114180399 free inodes.

server3 `/home`: 292050841600 available bytes; 83.70% used; 114180399 free inodes.

server3 `/data`: 82219302912 available bytes; 98.86% used; 225843615 free inodes.

server3 `/tmp`: 292050841600 available bytes; 83.70% used; 114180399 free inodes.

server3 `/var/tmp`: 292050841600 available bytes; 83.70% used; 114180399 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106057609216 available bytes; 94.08% used; 114349998 free inodes.

server4 `/home`: 106057609216 available bytes; 94.08% used; 114349998 free inodes.

server4 `/data`: 292915806208 available bytes; 95.95% used; 225414578 free inodes.

server4 `/tmp`: 106057609216 available bytes; 94.08% used; 114349998 free inodes.

server4 `/var/tmp`: 106057609216 available bytes; 94.08% used; 114349998 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
