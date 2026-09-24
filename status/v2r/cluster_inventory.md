# V2R cluster inventory

2026-09-24T04:16:16.623188+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324709261312 available bytes; 81.89% used; 112493367 free inodes.

server1 `/home`: 324709261312 available bytes; 81.89% used; 112493367 free inodes.

server1 `/tmp`: 324709261312 available bytes; 81.89% used; 112493367 free inodes.

server1 `/var/tmp`: 324709261312 available bytes; 81.89% used; 112493367 free inodes.

server1 `/mnt/raid5`: 410497544192 available bytes; 98.12% used; 337724742 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40797278208 available bytes; 97.72% used; 110430754 free inodes.

server2 `/home`: 40797278208 available bytes; 97.72% used; 110430754 free inodes.

server2 `/tmp`: 40797278208 available bytes; 97.72% used; 110430754 free inodes.

server2 `/var/tmp`: 40797278208 available bytes; 97.72% used; 110430754 free inodes.

server2 `/mnt/raid5`: 525793292288 available bytes; 96.37% used; 445196286 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292422492160 available bytes; 83.68% used; 114200761 free inodes.

server3 `/home`: 292422492160 available bytes; 83.68% used; 114200761 free inodes.

server3 `/data`: 31716065280 available bytes; 99.56% used; 225841748 free inodes.

server3 `/tmp`: 292422492160 available bytes; 83.68% used; 114200761 free inodes.

server3 `/var/tmp`: 292422492160 available bytes; 83.68% used; 114200761 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105790459904 available bytes; 94.10% used; 114349453 free inodes.

server4 `/home`: 105790459904 available bytes; 94.10% used; 114349453 free inodes.

server4 `/data`: 256707989504 available bytes; 96.45% used; 225381797 free inodes.

server4 `/tmp`: 105790459904 available bytes; 94.10% used; 114349453 free inodes.

server4 `/var/tmp`: 105790459904 available bytes; 94.10% used; 114349453 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
