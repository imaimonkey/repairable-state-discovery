# V2R cluster inventory

2026-09-25T05:26:01.049346+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871904256 available bytes; 82.21% used; 112480343 free inodes.

server1 `/home`: 318871904256 available bytes; 82.21% used; 112480343 free inodes.

server1 `/tmp`: 318871904256 available bytes; 82.21% used; 112480343 free inodes.

server1 `/var/tmp`: 318871904256 available bytes; 82.21% used; 112480343 free inodes.

server1 `/mnt/raid5`: 408504688640 available bytes; 98.13% used; 337568772 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22922743808 available bytes; 98.72% used; 110410449 free inodes.

server2 `/home`: 22922743808 available bytes; 98.72% used; 110410449 free inodes.

server2 `/tmp`: 22922743808 available bytes; 98.72% used; 110410449 free inodes.

server2 `/var/tmp`: 22922743808 available bytes; 98.72% used; 110410449 free inodes.

server2 `/mnt/raid5`: 461312004096 available bytes; 96.81% used; 445108433 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84318248960 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84318248960 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142776283136 available bytes; 98.03% used; 225814886 free inodes.

server3 `/tmp`: 84318248960 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84318248960 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658560512 available bytes; 94.10% used; 114350403 free inodes.

server4 `/home`: 105658560512 available bytes; 94.10% used; 114350403 free inodes.

server4 `/data`: 26272837632 available bytes; 99.64% used; 224959446 free inodes.

server4 `/tmp`: 105658560512 available bytes; 94.10% used; 114350403 free inodes.

server4 `/var/tmp`: 105658560512 available bytes; 94.10% used; 114350403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
