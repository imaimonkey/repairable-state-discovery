# V2R cluster inventory

2026-09-25T04:27:29.518297+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318929174528 available bytes; 82.21% used; 112480361 free inodes.

server1 `/home`: 318929174528 available bytes; 82.21% used; 112480361 free inodes.

server1 `/tmp`: 318929174528 available bytes; 82.21% used; 112480361 free inodes.

server1 `/var/tmp`: 318929174528 available bytes; 82.21% used; 112480361 free inodes.

server1 `/mnt/raid5`: 408743833600 available bytes; 98.12% used; 337592017 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22955167744 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22955167744 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22955167744 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22955167744 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 462577676288 available bytes; 96.80% used; 445109859 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341772288 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84341772288 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 143637692416 available bytes; 98.01% used; 225816190 free inodes.

server3 `/tmp`: 84341772288 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84341772288 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105671524352 available bytes; 94.10% used; 114350875 free inodes.

server4 `/home`: 105671524352 available bytes; 94.10% used; 114350875 free inodes.

server4 `/data`: 32804171776 available bytes; 99.55% used; 224963077 free inodes.

server4 `/tmp`: 105671524352 available bytes; 94.10% used; 114350875 free inodes.

server4 `/var/tmp`: 105671524352 available bytes; 94.10% used; 114350875 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
