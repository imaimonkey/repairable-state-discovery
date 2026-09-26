# V2R cluster inventory

2026-09-26T07:47:54.158957+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318759256064 available bytes; 82.22% used; 112476278 free inodes.

server1 `/home`: 318759256064 available bytes; 82.22% used; 112476278 free inodes.

server1 `/tmp`: 318759256064 available bytes; 82.22% used; 112476278 free inodes.

server1 `/var/tmp`: 318759256064 available bytes; 82.22% used; 112476278 free inodes.

server1 `/mnt/raid5`: 219201650688 available bytes; 98.99% used; 337539162 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22312108032 available bytes; 98.76% used; 110403897 free inodes.

server2 `/home`: 22312108032 available bytes; 98.76% used; 110403897 free inodes.

server2 `/tmp`: 22312108032 available bytes; 98.76% used; 110403897 free inodes.

server2 `/var/tmp`: 22312108032 available bytes; 98.76% used; 110403897 free inodes.

server2 `/mnt/raid5`: 270739959808 available bytes; 98.13% used; 445026328 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82676559872 available bytes; 95.39% used; 114110883 free inodes.

server3 `/home`: 82676559872 available bytes; 95.39% used; 114110883 free inodes.

server3 `/data`: 123918020608 available bytes; 98.29% used; 225820740 free inodes.

server3 `/tmp`: 82676559872 available bytes; 95.39% used; 114110883 free inodes.

server3 `/var/tmp`: 82676559872 available bytes; 95.39% used; 114110883 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106073911296 available bytes; 94.08% used; 114348162 free inodes.

server4 `/home`: 106073911296 available bytes; 94.08% used; 114348162 free inodes.

server4 `/data`: 105677950976 available bytes; 98.54% used; 224922519 free inodes.

server4 `/tmp`: 106073911296 available bytes; 94.08% used; 114348162 free inodes.

server4 `/var/tmp`: 106073911296 available bytes; 94.08% used; 114348162 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
