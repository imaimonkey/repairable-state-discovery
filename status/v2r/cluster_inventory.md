# V2R cluster inventory

2026-09-26T03:21:26.225490+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416564224 available bytes; 82.24% used; 112476264 free inodes.

server1 `/home`: 318416564224 available bytes; 82.24% used; 112476264 free inodes.

server1 `/tmp`: 318416564224 available bytes; 82.24% used; 112476264 free inodes.

server1 `/var/tmp`: 318416564224 available bytes; 82.24% used; 112476264 free inodes.

server1 `/mnt/raid5`: 331040210944 available bytes; 98.48% used; 337545864 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22933475328 available bytes; 98.72% used; 110406210 free inodes.

server2 `/home`: 22933475328 available bytes; 98.72% used; 110406210 free inodes.

server2 `/tmp`: 22933475328 available bytes; 98.72% used; 110406210 free inodes.

server2 `/var/tmp`: 22933475328 available bytes; 98.72% used; 110406210 free inodes.

server2 `/mnt/raid5`: 287486300160 available bytes; 98.01% used; 445052660 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84308721664 available bytes; 95.30% used; 114152364 free inodes.

server3 `/home`: 84308721664 available bytes; 95.30% used; 114152364 free inodes.

server3 `/data`: 125432635392 available bytes; 98.27% used; 225830755 free inodes.

server3 `/tmp`: 84308721664 available bytes; 95.30% used; 114152364 free inodes.

server3 `/var/tmp`: 84308721664 available bytes; 95.30% used; 114152364 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105876099072 available bytes; 94.09% used; 114347046 free inodes.

server4 `/home`: 105876099072 available bytes; 94.09% used; 114347046 free inodes.

server4 `/data`: 108981096448 available bytes; 98.49% used; 224914830 free inodes.

server4 `/tmp`: 105876099072 available bytes; 94.09% used; 114347046 free inodes.

server4 `/var/tmp`: 105876099072 available bytes; 94.09% used; 114347046 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
