# V2R cluster inventory

2026-09-26T02:43:14.490276+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318419054592 available bytes; 82.24% used; 112476255 free inodes.

server1 `/home`: 318419054592 available bytes; 82.24% used; 112476255 free inodes.

server1 `/tmp`: 318419054592 available bytes; 82.24% used; 112476255 free inodes.

server1 `/var/tmp`: 318419054592 available bytes; 82.24% used; 112476255 free inodes.

server1 `/mnt/raid5`: 331125055488 available bytes; 98.48% used; 337546045 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22936784896 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22936784896 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22936784896 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22936784896 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 270500634624 available bytes; 98.13% used; 445053934 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84320534528 available bytes; 95.29% used; 114152370 free inodes.

server3 `/home`: 84320534528 available bytes; 95.29% used; 114152370 free inodes.

server3 `/data`: 124788391936 available bytes; 98.28% used; 225816774 free inodes.

server3 `/tmp`: 84320534528 available bytes; 95.29% used; 114152370 free inodes.

server3 `/var/tmp`: 84320534528 available bytes; 95.29% used; 114152370 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105919377408 available bytes; 94.09% used; 114347153 free inodes.

server4 `/home`: 105919377408 available bytes; 94.09% used; 114347153 free inodes.

server4 `/data`: 109772828672 available bytes; 98.48% used; 224915415 free inodes.

server4 `/tmp`: 105919377408 available bytes; 94.09% used; 114347153 free inodes.

server4 `/var/tmp`: 105919377408 available bytes; 94.09% used; 114347153 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
