# V2R cluster inventory

2026-09-25T11:37:38.694920+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319061975040 available bytes; 82.20% used; 112478822 free inodes.

server1 `/home`: 319061975040 available bytes; 82.20% used; 112478822 free inodes.

server1 `/tmp`: 319061975040 available bytes; 82.20% used; 112478822 free inodes.

server1 `/var/tmp`: 319061975040 available bytes; 82.20% used; 112478822 free inodes.

server1 `/mnt/raid5`: 364276375552 available bytes; 98.33% used; 337549728 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22909530112 available bytes; 98.72% used; 110409980 free inodes.

server2 `/home`: 22909530112 available bytes; 98.72% used; 110409980 free inodes.

server2 `/tmp`: 22909530112 available bytes; 98.72% used; 110409980 free inodes.

server2 `/var/tmp`: 22909530112 available bytes; 98.72% used; 110409980 free inodes.

server2 `/mnt/raid5`: 327144665088 available bytes; 97.74% used; 445083250 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84131311616 available bytes; 95.31% used; 114155500 free inodes.

server3 `/home`: 84131311616 available bytes; 95.31% used; 114155500 free inodes.

server3 `/data`: 142162096128 available bytes; 98.04% used; 225813545 free inodes.

server3 `/tmp`: 84131311616 available bytes; 95.31% used; 114155500 free inodes.

server3 `/var/tmp`: 84131311616 available bytes; 95.31% used; 114155500 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105602940928 available bytes; 94.11% used; 114350248 free inodes.

server4 `/home`: 105602940928 available bytes; 94.11% used; 114350248 free inodes.

server4 `/data`: 234965671936 available bytes; 96.75% used; 224976778 free inodes.

server4 `/tmp`: 105602940928 available bytes; 94.11% used; 114350248 free inodes.

server4 `/var/tmp`: 105602940928 available bytes; 94.11% used; 114350248 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
