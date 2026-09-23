# V2R cluster inventory

2026-09-23T21:58:14.854462+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325711405056 available bytes; 81.83% used; 112501408 free inodes.

server1 `/home`: 325711405056 available bytes; 81.83% used; 112501408 free inodes.

server1 `/tmp`: 325711405056 available bytes; 81.83% used; 112501408 free inodes.

server1 `/var/tmp`: 325711405056 available bytes; 81.83% used; 112501408 free inodes.

server1 `/mnt/raid5`: 1388114382848 available bytes; 93.63% used; 337739895 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41104097280 available bytes; 97.71% used; 110432649 free inodes.

server2 `/home`: 41104097280 available bytes; 97.71% used; 110432649 free inodes.

server2 `/tmp`: 41104097280 available bytes; 97.71% used; 110432649 free inodes.

server2 `/var/tmp`: 41104097280 available bytes; 97.71% used; 110432649 free inodes.

server2 `/mnt/raid5`: 537661304832 available bytes; 96.28% used; 445207729 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293037797376 available bytes; 83.65% used; 114222951 free inodes.

server3 `/home`: 293037797376 available bytes; 83.65% used; 114222951 free inodes.

server3 `/data`: 82459557888 available bytes; 98.86% used; 225847924 free inodes.

server3 `/tmp`: 293037797376 available bytes; 83.65% used; 114222951 free inodes.

server3 `/var/tmp`: 293037797376 available bytes; 83.65% used; 114222951 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106452230144 available bytes; 94.06% used; 114355670 free inodes.

server4 `/home`: 106452230144 available bytes; 94.06% used; 114355670 free inodes.

server4 `/data`: 300211314688 available bytes; 95.85% used; 225445491 free inodes.

server4 `/tmp`: 106452230144 available bytes; 94.06% used; 114355670 free inodes.

server4 `/var/tmp`: 106452230144 available bytes; 94.06% used; 114355670 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
