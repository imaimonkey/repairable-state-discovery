# V2R cluster inventory

2026-09-24T04:09:57.150740+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324711583744 available bytes; 81.89% used; 112493435 free inodes.

server1 `/home`: 324711583744 available bytes; 81.89% used; 112493435 free inodes.

server1 `/tmp`: 324711583744 available bytes; 81.89% used; 112493435 free inodes.

server1 `/var/tmp`: 324711583744 available bytes; 81.89% used; 112493435 free inodes.

server1 `/mnt/raid5`: 426308296704 available bytes; 98.04% used; 337724760 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40800169984 available bytes; 97.72% used; 110430802 free inodes.

server2 `/home`: 40800169984 available bytes; 97.72% used; 110430802 free inodes.

server2 `/tmp`: 40800169984 available bytes; 97.72% used; 110430802 free inodes.

server2 `/var/tmp`: 40800169984 available bytes; 97.72% used; 110430802 free inodes.

server2 `/mnt/raid5`: 525985181696 available bytes; 96.37% used; 445196571 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292026331136 available bytes; 83.70% used; 114176973 free inodes.

server3 `/home`: 292026331136 available bytes; 83.70% used; 114176973 free inodes.

server3 `/data`: 31734939648 available bytes; 99.56% used; 225841864 free inodes.

server3 `/tmp`: 292026331136 available bytes; 83.70% used; 114176973 free inodes.

server3 `/var/tmp`: 292026331136 available bytes; 83.70% used; 114176973 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105790902272 available bytes; 94.10% used; 114349473 free inodes.

server4 `/home`: 105790902272 available bytes; 94.10% used; 114349473 free inodes.

server4 `/data`: 256723701760 available bytes; 96.45% used; 225381862 free inodes.

server4 `/tmp`: 105790902272 available bytes; 94.10% used; 114349473 free inodes.

server4 `/var/tmp`: 105790902272 available bytes; 94.10% used; 114349473 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
