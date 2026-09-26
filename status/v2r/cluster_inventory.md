# V2R cluster inventory

2026-09-26T07:55:03.985910+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318752718848 available bytes; 82.22% used; 112476268 free inodes.

server1 `/home`: 318752718848 available bytes; 82.22% used; 112476268 free inodes.

server1 `/tmp`: 318752718848 available bytes; 82.22% used; 112476268 free inodes.

server1 `/var/tmp`: 318752718848 available bytes; 82.22% used; 112476268 free inodes.

server1 `/mnt/raid5`: 219181457408 available bytes; 98.99% used; 337539115 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22318809088 available bytes; 98.75% used; 110403903 free inodes.

server2 `/home`: 22318809088 available bytes; 98.75% used; 110403903 free inodes.

server2 `/tmp`: 22318809088 available bytes; 98.75% used; 110403903 free inodes.

server2 `/var/tmp`: 22318809088 available bytes; 98.75% used; 110403903 free inodes.

server2 `/mnt/raid5`: 249884753920 available bytes; 98.27% used; 445025965 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82679607296 available bytes; 95.39% used; 114110852 free inodes.

server3 `/home`: 82679607296 available bytes; 95.39% used; 114110852 free inodes.

server3 `/data`: 123904421888 available bytes; 98.29% used; 225820619 free inodes.

server3 `/tmp`: 82679607296 available bytes; 95.39% used; 114110852 free inodes.

server3 `/var/tmp`: 82679607296 available bytes; 95.39% used; 114110852 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106073690112 available bytes; 94.08% used; 114348159 free inodes.

server4 `/home`: 106073690112 available bytes; 94.08% used; 114348159 free inodes.

server4 `/data`: 105654132736 available bytes; 98.54% used; 224922427 free inodes.

server4 `/tmp`: 106073690112 available bytes; 94.08% used; 114348159 free inodes.

server4 `/var/tmp`: 106073690112 available bytes; 94.08% used; 114348159 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
