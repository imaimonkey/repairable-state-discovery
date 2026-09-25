# V2R cluster inventory

2026-09-25T05:21:23.343013+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318877605888 available bytes; 82.21% used; 112480257 free inodes.

server1 `/home`: 318877605888 available bytes; 82.21% used; 112480257 free inodes.

server1 `/tmp`: 318877605888 available bytes; 82.21% used; 112480257 free inodes.

server1 `/var/tmp`: 318877605888 available bytes; 82.21% used; 112480257 free inodes.

server1 `/mnt/raid5`: 408523411456 available bytes; 98.13% used; 337569327 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22929805312 available bytes; 98.72% used; 110410443 free inodes.

server2 `/home`: 22929805312 available bytes; 98.72% used; 110410443 free inodes.

server2 `/tmp`: 22929805312 available bytes; 98.72% used; 110410443 free inodes.

server2 `/var/tmp`: 22929805312 available bytes; 98.72% used; 110410443 free inodes.

server2 `/mnt/raid5`: 461454094336 available bytes; 96.81% used; 445108582 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84338008064 available bytes; 95.29% used; 114156044 free inodes.

server3 `/home`: 84338008064 available bytes; 95.29% used; 114156044 free inodes.

server3 `/data`: 142778101760 available bytes; 98.03% used; 225814982 free inodes.

server3 `/tmp`: 84338008064 available bytes; 95.29% used; 114156044 free inodes.

server3 `/var/tmp`: 84338008064 available bytes; 95.29% used; 114156044 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658695680 available bytes; 94.10% used; 114350403 free inodes.

server4 `/home`: 105658695680 available bytes; 94.10% used; 114350403 free inodes.

server4 `/data`: 26285780992 available bytes; 99.64% used; 224959831 free inodes.

server4 `/tmp`: 105658695680 available bytes; 94.10% used; 114350403 free inodes.

server4 `/var/tmp`: 105658695680 available bytes; 94.10% used; 114350403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
