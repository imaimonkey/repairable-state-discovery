# V2R cluster inventory

2026-09-24T23:34:45.337939+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319011987456 available bytes; 82.20% used; 112480785 free inodes.

server1 `/home`: 319011987456 available bytes; 82.20% used; 112480785 free inodes.

server1 `/tmp`: 319011987456 available bytes; 82.20% used; 112480785 free inodes.

server1 `/var/tmp`: 319011987456 available bytes; 82.20% used; 112480785 free inodes.

server1 `/mnt/raid5`: 415220641792 available bytes; 98.10% used; 337612678 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23114092544 available bytes; 98.71% used; 110410806 free inodes.

server2 `/home`: 23114092544 available bytes; 98.71% used; 110410806 free inodes.

server2 `/tmp`: 23114092544 available bytes; 98.71% used; 110410806 free inodes.

server2 `/var/tmp`: 23114092544 available bytes; 98.71% used; 110410806 free inodes.

server2 `/mnt/raid5`: 486254690304 available bytes; 96.64% used; 445151051 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84360511488 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84360511488 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148133666816 available bytes; 97.95% used; 225800821 free inodes.

server3 `/tmp`: 84360511488 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84360511488 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799421952 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799421952 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 61188812800 available bytes; 99.15% used; 225140687 free inodes.

server4 `/tmp`: 105799421952 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799421952 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
