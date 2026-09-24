# V2R cluster inventory

2026-09-24T19:40:08.721953+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323990007808 available bytes; 81.93% used; 112481457 free inodes.

server1 `/home`: 323990007808 available bytes; 81.93% used; 112481457 free inodes.

server1 `/tmp`: 323990007808 available bytes; 81.93% used; 112481457 free inodes.

server1 `/var/tmp`: 323990007808 available bytes; 81.93% used; 112481457 free inodes.

server1 `/mnt/raid5`: 415598841856 available bytes; 98.09% used; 337631196 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 53242486784 available bytes; 97.03% used; 110411822 free inodes.

server2 `/home`: 53242486784 available bytes; 97.03% used; 110411822 free inodes.

server2 `/tmp`: 53242486784 available bytes; 97.03% used; 110411822 free inodes.

server2 `/var/tmp`: 53242486784 available bytes; 97.03% used; 110411822 free inodes.

server2 `/mnt/raid5`: 494547664896 available bytes; 96.58% used; 445158320 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84399443968 available bytes; 95.29% used; 114156141 free inodes.

server3 `/home`: 84399443968 available bytes; 95.29% used; 114156141 free inodes.

server3 `/data`: 152175001600 available bytes; 97.90% used; 225799317 free inodes.

server3 `/tmp`: 84399443968 available bytes; 95.29% used; 114156141 free inodes.

server3 `/var/tmp`: 84399443968 available bytes; 95.29% used; 114156141 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105659248640 available bytes; 94.10% used; 114348430 free inodes.

server4 `/home`: 105659248640 available bytes; 94.10% used; 114348430 free inodes.

server4 `/data`: 89861611520 available bytes; 98.76% used; 225266662 free inodes.

server4 `/tmp`: 105659248640 available bytes; 94.10% used; 114348430 free inodes.

server4 `/var/tmp`: 105659248640 available bytes; 94.10% used; 114348430 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
