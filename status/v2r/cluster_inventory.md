# V2R cluster inventory

2026-09-23T11:57:51.141491+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41819037696 available bytes; 97.67% used; 110436695 free inodes.

server2 `/home`: 41819037696 available bytes; 97.67% used; 110436695 free inodes.

server2 `/tmp`: 41819037696 available bytes; 97.67% used; 110436695 free inodes.

server2 `/var/tmp`: 41819037696 available bytes; 97.67% used; 110436695 free inodes.

server2 `/mnt/raid5`: 558288982016 available bytes; 96.14% used; 445231745 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 380032811008 available bytes; 78.79% used; 114344990 free inodes.

server3 `/home`: 380032811008 available bytes; 78.79% used; 114344990 free inodes.

server3 `/data`: 137515122688 available bytes; 98.10% used; 225864315 free inodes.

server3 `/tmp`: 380032811008 available bytes; 78.79% used; 114344990 free inodes.

server3 `/var/tmp`: 380032811008 available bytes; 78.79% used; 114344990 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605219328 available bytes; 93.77% used; 114379004 free inodes.

server4 `/home`: 111605219328 available bytes; 93.77% used; 114379004 free inodes.

server4 `/data`: 66540711936 available bytes; 99.08% used; 225411705 free inodes.

server4 `/tmp`: 111605219328 available bytes; 93.77% used; 114379004 free inodes.

server4 `/var/tmp`: 111605219328 available bytes; 93.77% used; 114379004 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
