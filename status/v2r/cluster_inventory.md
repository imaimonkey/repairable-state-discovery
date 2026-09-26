# V2R cluster inventory

2026-09-26T07:04:37.938168+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318769799168 available bytes; 82.22% used; 112476289 free inodes.

server1 `/home`: 318769799168 available bytes; 82.22% used; 112476289 free inodes.

server1 `/tmp`: 318769799168 available bytes; 82.22% used; 112476289 free inodes.

server1 `/var/tmp`: 318769799168 available bytes; 82.22% used; 112476289 free inodes.

server1 `/mnt/raid5`: 219288588288 available bytes; 98.99% used; 337539367 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22315646976 available bytes; 98.76% used; 110403878 free inodes.

server2 `/home`: 22315646976 available bytes; 98.76% used; 110403878 free inodes.

server2 `/tmp`: 22315646976 available bytes; 98.76% used; 110403878 free inodes.

server2 `/var/tmp`: 22315646976 available bytes; 98.76% used; 110403878 free inodes.

server2 `/mnt/raid5`: 271985311744 available bytes; 98.12% used; 445027696 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82688917504 available bytes; 95.39% used; 114110895 free inodes.

server3 `/home`: 82688917504 available bytes; 95.39% used; 114110895 free inodes.

server3 `/data`: 123987652608 available bytes; 98.29% used; 225821525 free inodes.

server3 `/tmp`: 82688917504 available bytes; 95.39% used; 114110895 free inodes.

server3 `/var/tmp`: 82688917504 available bytes; 95.39% used; 114110895 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106075217920 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106075217920 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105881104384 available bytes; 98.54% used; 224922793 free inodes.

server4 `/tmp`: 106075217920 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106075217920 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
