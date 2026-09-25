# V2R cluster inventory

2026-09-25T06:32:12.362512+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872911872 available bytes; 82.21% used; 112480352 free inodes.

server1 `/home`: 318872911872 available bytes; 82.21% used; 112480352 free inodes.

server1 `/tmp`: 318872911872 available bytes; 82.21% used; 112480352 free inodes.

server1 `/var/tmp`: 318872911872 available bytes; 82.21% used; 112480352 free inodes.

server1 `/mnt/raid5`: 399811805184 available bytes; 98.17% used; 337561433 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22889734144 available bytes; 98.72% used; 110410516 free inodes.

server2 `/home`: 22889734144 available bytes; 98.72% used; 110410516 free inodes.

server2 `/tmp`: 22889734144 available bytes; 98.72% used; 110410516 free inodes.

server2 `/var/tmp`: 22889734144 available bytes; 98.72% used; 110410516 free inodes.

server2 `/mnt/raid5`: 369928949760 available bytes; 97.44% used; 445099336 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84450017280 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84450017280 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142537764864 available bytes; 98.03% used; 225813755 free inodes.

server3 `/tmp`: 84450017280 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84450017280 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648107520 available bytes; 94.10% used; 114350389 free inodes.

server4 `/home`: 105648107520 available bytes; 94.10% used; 114350389 free inodes.

server4 `/data`: 253136486400 available bytes; 96.50% used; 225020374 free inodes.

server4 `/tmp`: 105648107520 available bytes; 94.10% used; 114350389 free inodes.

server4 `/var/tmp`: 105648107520 available bytes; 94.10% used; 114350389 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
