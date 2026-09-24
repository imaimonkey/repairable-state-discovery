# V2R cluster inventory

2026-09-24T13:43:35.411299+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324027645952 available bytes; 81.92% used; 112481504 free inodes.

server1 `/home`: 324027645952 available bytes; 81.92% used; 112481504 free inodes.

server1 `/tmp`: 324027645952 available bytes; 81.92% used; 112481504 free inodes.

server1 `/var/tmp`: 324027645952 available bytes; 81.92% used; 112481504 free inodes.

server1 `/mnt/raid5`: 417001394176 available bytes; 98.09% used; 337673640 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57509105664 available bytes; 96.79% used; 110428582 free inodes.

server2 `/home`: 57509105664 available bytes; 96.79% used; 110428582 free inodes.

server2 `/tmp`: 57509105664 available bytes; 96.79% used; 110428582 free inodes.

server2 `/var/tmp`: 57509105664 available bytes; 96.79% used; 110428582 free inodes.

server2 `/mnt/raid5`: 506216640512 available bytes; 96.50% used; 445169376 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84699594752 available bytes; 95.27% used; 114165397 free inodes.

server3 `/home`: 84699594752 available bytes; 95.27% used; 114165397 free inodes.

server3 `/data`: 161164447744 available bytes; 97.77% used; 225802899 free inodes.

server3 `/tmp`: 84699594752 available bytes; 95.27% used; 114165397 free inodes.

server3 `/var/tmp`: 84699594752 available bytes; 95.27% used; 114165397 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105760845824 available bytes; 94.10% used; 114348733 free inodes.

server4 `/home`: 105760845824 available bytes; 94.10% used; 114348733 free inodes.

server4 `/data`: 90042146816 available bytes; 98.76% used; 225257170 free inodes.

server4 `/tmp`: 105760845824 available bytes; 94.10% used; 114348733 free inodes.

server4 `/var/tmp`: 105760845824 available bytes; 94.10% used; 114348733 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
