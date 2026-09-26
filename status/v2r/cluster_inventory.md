# V2R cluster inventory

2026-09-26T01:37:28.983525+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318649634816 available bytes; 82.22% used; 112476295 free inodes.

server1 `/home`: 318649634816 available bytes; 82.22% used; 112476295 free inodes.

server1 `/tmp`: 318649634816 available bytes; 82.22% used; 112476295 free inodes.

server1 `/var/tmp`: 318649634816 available bytes; 82.22% used; 112476295 free inodes.

server1 `/mnt/raid5`: 345489371136 available bytes; 98.42% used; 337546513 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22941007872 available bytes; 98.72% used; 110406222 free inodes.

server2 `/home`: 22941007872 available bytes; 98.72% used; 110406222 free inodes.

server2 `/tmp`: 22941007872 available bytes; 98.72% used; 110406222 free inodes.

server2 `/var/tmp`: 22941007872 available bytes; 98.72% used; 110406222 free inodes.

server2 `/mnt/raid5`: 290499907584 available bytes; 97.99% used; 445055767 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84335407104 available bytes; 95.29% used; 114152366 free inodes.

server3 `/home`: 84335407104 available bytes; 95.29% used; 114152366 free inodes.

server3 `/data`: 124797947904 available bytes; 98.28% used; 225817887 free inodes.

server3 `/tmp`: 84335407104 available bytes; 95.29% used; 114152366 free inodes.

server3 `/var/tmp`: 84335407104 available bytes; 95.29% used; 114152366 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105196769280 available bytes; 94.13% used; 114346905 free inodes.

server4 `/home`: 105196769280 available bytes; 94.13% used; 114346905 free inodes.

server4 `/data`: 132805091328 available bytes; 98.16% used; 224916318 free inodes.

server4 `/tmp`: 105196769280 available bytes; 94.13% used; 114346905 free inodes.

server4 `/var/tmp`: 105196769280 available bytes; 94.13% used; 114346905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
