# V2R cluster inventory

2026-09-23T21:22:46.929269+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325719896064 available bytes; 81.83% used; 112501429 free inodes.

server1 `/home`: 325719896064 available bytes; 81.83% used; 112501429 free inodes.

server1 `/tmp`: 325719896064 available bytes; 81.83% used; 112501429 free inodes.

server1 `/var/tmp`: 325719896064 available bytes; 81.83% used; 112501429 free inodes.

server1 `/mnt/raid5`: 1388135178240 available bytes; 93.63% used; 337739965 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41110646784 available bytes; 97.71% used; 110432686 free inodes.

server2 `/home`: 41110646784 available bytes; 97.71% used; 110432686 free inodes.

server2 `/tmp`: 41110646784 available bytes; 97.71% used; 110432686 free inodes.

server2 `/var/tmp`: 41110646784 available bytes; 97.71% used; 110432686 free inodes.

server2 `/mnt/raid5`: 538745069568 available bytes; 96.28% used; 445208945 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292956123136 available bytes; 83.65% used; 114208568 free inodes.

server3 `/home`: 292956123136 available bytes; 83.65% used; 114208568 free inodes.

server3 `/data`: 52292882432 available bytes; 99.28% used; 225848939 free inodes.

server3 `/tmp`: 292956123136 available bytes; 83.65% used; 114208568 free inodes.

server3 `/var/tmp`: 292956123136 available bytes; 83.65% used; 114208568 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106486177792 available bytes; 94.06% used; 114356019 free inodes.

server4 `/home`: 106486177792 available bytes; 94.06% used; 114356019 free inodes.

server4 `/data`: 300385599488 available bytes; 95.85% used; 225452397 free inodes.

server4 `/tmp`: 106486177792 available bytes; 94.06% used; 114356019 free inodes.

server4 `/var/tmp`: 106486177792 available bytes; 94.06% used; 114356019 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
