# V2R cluster inventory

2026-09-24T11:18:12.246727+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324362612736 available bytes; 81.90% used; 112488934 free inodes.

server1 `/home`: 324362612736 available bytes; 81.90% used; 112488934 free inodes.

server1 `/tmp`: 324362612736 available bytes; 81.90% used; 112488934 free inodes.

server1 `/var/tmp`: 324362612736 available bytes; 81.90% used; 112488934 free inodes.

server1 `/mnt/raid5`: 461931200512 available bytes; 97.88% used; 337690737 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57676722176 available bytes; 96.78% used; 110430118 free inodes.

server2 `/home`: 57676722176 available bytes; 96.78% used; 110430118 free inodes.

server2 `/tmp`: 57676722176 available bytes; 96.78% used; 110430118 free inodes.

server2 `/var/tmp`: 57676722176 available bytes; 96.78% used; 110430118 free inodes.

server2 `/mnt/raid5`: 510464557056 available bytes; 96.47% used; 445173835 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85732139008 available bytes; 95.22% used; 114197134 free inodes.

server3 `/home`: 85732139008 available bytes; 95.22% used; 114197134 free inodes.

server3 `/data`: 163889348608 available bytes; 97.73% used; 225816877 free inodes.

server3 `/tmp`: 85732139008 available bytes; 95.22% used; 114197134 free inodes.

server3 `/var/tmp`: 85732139008 available bytes; 95.22% used; 114197134 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105731379200 available bytes; 94.10% used; 114348881 free inodes.

server4 `/home`: 105731379200 available bytes; 94.10% used; 114348881 free inodes.

server4 `/data`: 115647815680 available bytes; 98.40% used; 225258123 free inodes.

server4 `/tmp`: 105731379200 available bytes; 94.10% used; 114348881 free inodes.

server4 `/var/tmp`: 105731379200 available bytes; 94.10% used; 114348881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
