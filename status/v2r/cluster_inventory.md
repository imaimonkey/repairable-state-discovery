# V2R cluster inventory

2026-09-23T12:12:46.400144+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41809453056 available bytes; 97.67% used; 110436695 free inodes.

server2 `/home`: 41809453056 available bytes; 97.67% used; 110436695 free inodes.

server2 `/tmp`: 41809453056 available bytes; 97.67% used; 110436695 free inodes.

server2 `/var/tmp`: 41809453056 available bytes; 97.67% used; 110436695 free inodes.

server2 `/mnt/raid5`: 557793325056 available bytes; 96.15% used; 445230836 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 379895951360 available bytes; 78.80% used; 114340973 free inodes.

server3 `/home`: 379895951360 available bytes; 78.80% used; 114340973 free inodes.

server3 `/data`: 137423118336 available bytes; 98.10% used; 225863966 free inodes.

server3 `/tmp`: 379895951360 available bytes; 78.80% used; 114340973 free inodes.

server3 `/var/tmp`: 379895951360 available bytes; 78.80% used; 114340973 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111604948992 available bytes; 93.77% used; 114378996 free inodes.

server4 `/home`: 111604948992 available bytes; 93.77% used; 114378996 free inodes.

server4 `/data`: 62759763968 available bytes; 99.13% used; 225407001 free inodes.

server4 `/tmp`: 111604948992 available bytes; 93.77% used; 114378996 free inodes.

server4 `/var/tmp`: 111604948992 available bytes; 93.77% used; 114378996 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
