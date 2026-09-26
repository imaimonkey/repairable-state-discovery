# V2R cluster inventory

2026-09-26T15:49:46.253950+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318140747776 available bytes; 82.25% used; 112473924 free inodes.

server1 `/home`: 318140747776 available bytes; 82.25% used; 112473924 free inodes.

server1 `/tmp`: 318140747776 available bytes; 82.25% used; 112473924 free inodes.

server1 `/var/tmp`: 318140747776 available bytes; 82.25% used; 112473924 free inodes.

server1 `/mnt/raid5`: 654105993216 available bytes; 97.00% used; 337531411 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18031075328 available bytes; 98.99% used; 110367502 free inodes.

server2 `/home`: 18031075328 available bytes; 98.99% used; 110367502 free inodes.

server2 `/tmp`: 18031075328 available bytes; 98.99% used; 110367502 free inodes.

server2 `/var/tmp`: 18031075328 available bytes; 98.99% used; 110367502 free inodes.

server2 `/mnt/raid5`: 608868634624 available bytes; 95.79% used; 444972491 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82151202816 available bytes; 95.42% used; 114093393 free inodes.

server3 `/home`: 82151202816 available bytes; 95.42% used; 114093393 free inodes.

server3 `/data`: 1349515149312 available bytes; 81.35% used; 225832203 free inodes.

server3 `/tmp`: 82151202816 available bytes; 95.42% used; 114093393 free inodes.

server3 `/var/tmp`: 82151202816 available bytes; 95.42% used; 114093393 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105954385920 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105954385920 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410719170560 available bytes; 94.32% used; 224825361 free inodes.

server4 `/tmp`: 105954385920 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105954385920 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
