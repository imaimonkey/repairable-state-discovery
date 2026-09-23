# V2R cluster inventory

2026-09-23T21:38:12.817893+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325715148800 available bytes; 81.83% used; 112501434 free inodes.

server1 `/home`: 325715148800 available bytes; 81.83% used; 112501434 free inodes.

server1 `/tmp`: 325715148800 available bytes; 81.83% used; 112501434 free inodes.

server1 `/var/tmp`: 325715148800 available bytes; 81.83% used; 112501434 free inodes.

server1 `/mnt/raid5`: 1388131696640 available bytes; 93.63% used; 337739933 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41118666752 available bytes; 97.71% used; 110432683 free inodes.

server2 `/home`: 41118666752 available bytes; 97.71% used; 110432683 free inodes.

server2 `/tmp`: 41118666752 available bytes; 97.71% used; 110432683 free inodes.

server2 `/var/tmp`: 41118666752 available bytes; 97.71% used; 110432683 free inodes.

server2 `/mnt/raid5`: 538260402176 available bytes; 96.28% used; 445208474 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293062520832 available bytes; 83.65% used; 114221977 free inodes.

server3 `/home`: 293062520832 available bytes; 83.65% used; 114221977 free inodes.

server3 `/data`: 52273156096 available bytes; 99.28% used; 225848622 free inodes.

server3 `/tmp`: 293062520832 available bytes; 83.65% used; 114221977 free inodes.

server3 `/var/tmp`: 293062520832 available bytes; 83.65% used; 114221977 free inodes.
| server4 | True | ['0', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106475495424 available bytes; 94.06% used; 114355990 free inodes.

server4 `/home`: 106475495424 available bytes; 94.06% used; 114355990 free inodes.

server4 `/data`: 300265095168 available bytes; 95.85% used; 225449300 free inodes.

server4 `/tmp`: 106475495424 available bytes; 94.06% used; 114355990 free inodes.

server4 `/var/tmp`: 106475495424 available bytes; 94.06% used; 114355990 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
