# V2R cluster inventory

2026-09-25T04:32:06.766037+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318929776640 available bytes; 82.21% used; 112480367 free inodes.

server1 `/home`: 318929776640 available bytes; 82.21% used; 112480367 free inodes.

server1 `/tmp`: 318929776640 available bytes; 82.21% used; 112480367 free inodes.

server1 `/var/tmp`: 318929776640 available bytes; 82.21% used; 112480367 free inodes.

server1 `/mnt/raid5`: 408729088000 available bytes; 98.13% used; 337591462 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22949609472 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22949609472 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22949609472 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22949609472 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 462971625472 available bytes; 96.80% used; 445109902 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341248000 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84341248000 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 143485599744 available bytes; 98.02% used; 225816109 free inodes.

server3 `/tmp`: 84341248000 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84341248000 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105671389184 available bytes; 94.10% used; 114350875 free inodes.

server4 `/home`: 105671389184 available bytes; 94.10% used; 114350875 free inodes.

server4 `/data`: 32796344320 available bytes; 99.55% used; 224962863 free inodes.

server4 `/tmp`: 105671389184 available bytes; 94.10% used; 114350875 free inodes.

server4 `/var/tmp`: 105671389184 available bytes; 94.10% used; 114350875 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
