# V2R cluster inventory

2026-09-24T06:12:55.513658+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324519927808 available bytes; 81.90% used; 112491819 free inodes.

server1 `/home`: 324519927808 available bytes; 81.90% used; 112491819 free inodes.

server1 `/tmp`: 324519927808 available bytes; 81.90% used; 112491819 free inodes.

server1 `/var/tmp`: 324519927808 available bytes; 81.90% used; 112491819 free inodes.

server1 `/mnt/raid5`: 517601333248 available bytes; 97.63% used; 337723777 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57894342656 available bytes; 96.77% used; 110431262 free inodes.

server2 `/home`: 57894342656 available bytes; 96.77% used; 110431262 free inodes.

server2 `/tmp`: 57894342656 available bytes; 96.77% used; 110431262 free inodes.

server2 `/var/tmp`: 57894342656 available bytes; 96.77% used; 110431262 free inodes.

server2 `/mnt/raid5`: 520769392640 available bytes; 96.40% used; 445192475 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126802153472 available bytes; 92.92% used; 114174277 free inodes.

server3 `/home`: 126802153472 available bytes; 92.92% used; 114174277 free inodes.

server3 `/data`: 161297432576 available bytes; 97.77% used; 225836086 free inodes.

server3 `/tmp`: 126802153472 available bytes; 92.92% used; 114174277 free inodes.

server3 `/var/tmp`: 126802153472 available bytes; 92.92% used; 114174277 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105806491648 available bytes; 94.10% used; 114349319 free inodes.

server4 `/home`: 105806491648 available bytes; 94.10% used; 114349319 free inodes.

server4 `/data`: 339768901632 available bytes; 95.30% used; 225374015 free inodes.

server4 `/tmp`: 105806491648 available bytes; 94.10% used; 114349319 free inodes.

server4 `/var/tmp`: 105806491648 available bytes; 94.10% used; 114349319 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
