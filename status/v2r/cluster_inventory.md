# V2R cluster inventory

2026-09-25T04:25:57.394857+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318929645568 available bytes; 82.21% used; 112480358 free inodes.

server1 `/home`: 318929645568 available bytes; 82.21% used; 112480358 free inodes.

server1 `/tmp`: 318929645568 available bytes; 82.21% used; 112480358 free inodes.

server1 `/var/tmp`: 318929645568 available bytes; 82.21% used; 112480358 free inodes.

server1 `/mnt/raid5`: 408751226880 available bytes; 98.12% used; 337592208 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22955470848 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22955470848 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22955470848 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22955470848 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 463172722688 available bytes; 96.80% used; 445110049 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84343345152 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84343345152 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 143658455040 available bytes; 98.01% used; 225816230 free inodes.

server3 `/tmp`: 84343345152 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84343345152 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105671561216 available bytes; 94.10% used; 114350875 free inodes.

server4 `/home`: 105671561216 available bytes; 94.10% used; 114350875 free inodes.

server4 `/data`: 32803241984 available bytes; 99.55% used; 224963131 free inodes.

server4 `/tmp`: 105671561216 available bytes; 94.10% used; 114350875 free inodes.

server4 `/var/tmp`: 105671561216 available bytes; 94.10% used; 114350875 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
