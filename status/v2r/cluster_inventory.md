# V2R cluster inventory

2026-09-26T04:48:30.604600+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318400376832 available bytes; 82.24% used; 112476282 free inodes.

server1 `/home`: 318400376832 available bytes; 82.24% used; 112476282 free inodes.

server1 `/tmp`: 318400376832 available bytes; 82.24% used; 112476282 free inodes.

server1 `/var/tmp`: 318400376832 available bytes; 82.24% used; 112476282 free inodes.

server1 `/mnt/raid5`: 330473701376 available bytes; 98.48% used; 337545362 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22936596480 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22936596480 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22936596480 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22936596480 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 284963168256 available bytes; 98.03% used; 445050072 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83998547968 available bytes; 95.31% used; 114155927 free inodes.

server3 `/home`: 83998547968 available bytes; 95.31% used; 114155927 free inodes.

server3 `/data`: 124378087424 available bytes; 98.28% used; 225816975 free inodes.

server3 `/tmp`: 83998547968 available bytes; 95.31% used; 114155927 free inodes.

server3 `/var/tmp`: 83998547968 available bytes; 95.31% used; 114155927 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106001907712 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106001907712 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 107069100032 available bytes; 98.52% used; 224929359 free inodes.

server4 `/tmp`: 106001907712 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106001907712 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
