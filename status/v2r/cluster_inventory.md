# V2R cluster inventory

2026-09-26T03:04:38.045587+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416674816 available bytes; 82.24% used; 112476267 free inodes.

server1 `/home`: 318416674816 available bytes; 82.24% used; 112476267 free inodes.

server1 `/tmp`: 318416674816 available bytes; 82.24% used; 112476267 free inodes.

server1 `/var/tmp`: 318416674816 available bytes; 82.24% used; 112476267 free inodes.

server1 `/mnt/raid5`: 331071668224 available bytes; 98.48% used; 337545943 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939803648 available bytes; 98.72% used; 110406212 free inodes.

server2 `/home`: 22939803648 available bytes; 98.72% used; 110406212 free inodes.

server2 `/tmp`: 22939803648 available bytes; 98.72% used; 110406212 free inodes.

server2 `/var/tmp`: 22939803648 available bytes; 98.72% used; 110406212 free inodes.

server2 `/mnt/raid5`: 287958757376 available bytes; 98.01% used; 445053211 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84308385792 available bytes; 95.30% used; 114152368 free inodes.

server3 `/home`: 84308385792 available bytes; 95.30% used; 114152368 free inodes.

server3 `/data`: 125439033344 available bytes; 98.27% used; 225831107 free inodes.

server3 `/tmp`: 84308385792 available bytes; 95.30% used; 114152368 free inodes.

server3 `/var/tmp`: 84308385792 available bytes; 95.30% used; 114152368 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105885122560 available bytes; 94.09% used; 114347062 free inodes.

server4 `/home`: 105885122560 available bytes; 94.09% used; 114347062 free inodes.

server4 `/data`: 109658767360 available bytes; 98.48% used; 224915297 free inodes.

server4 `/tmp`: 105885122560 available bytes; 94.09% used; 114347062 free inodes.

server4 `/var/tmp`: 105885122560 available bytes; 94.09% used; 114347062 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
