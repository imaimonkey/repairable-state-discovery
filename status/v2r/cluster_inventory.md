# V2R cluster inventory

2026-09-25T03:53:32.197717+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318930132992 available bytes; 82.21% used; 112480352 free inodes.

server1 `/home`: 318930132992 available bytes; 82.21% used; 112480352 free inodes.

server1 `/tmp`: 318930132992 available bytes; 82.21% used; 112480352 free inodes.

server1 `/var/tmp`: 318930132992 available bytes; 82.21% used; 112480352 free inodes.

server1 `/mnt/raid5`: 415723229184 available bytes; 98.09% used; 337596101 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22971514880 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22971514880 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22971514880 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22971514880 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 464174776320 available bytes; 96.79% used; 445111042 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340559872 available bytes; 95.29% used; 114156062 free inodes.

server3 `/home`: 84340559872 available bytes; 95.29% used; 114156062 free inodes.

server3 `/data`: 123549356032 available bytes; 98.29% used; 225816921 free inodes.

server3 `/tmp`: 84340559872 available bytes; 95.29% used; 114156062 free inodes.

server3 `/var/tmp`: 84340559872 available bytes; 95.29% used; 114156062 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683120128 available bytes; 94.10% used; 114350896 free inodes.

server4 `/home`: 105683120128 available bytes; 94.10% used; 114350896 free inodes.

server4 `/data`: 38553616384 available bytes; 99.47% used; 224964928 free inodes.

server4 `/tmp`: 105683120128 available bytes; 94.10% used; 114350896 free inodes.

server4 `/var/tmp`: 105683120128 available bytes; 94.10% used; 114350896 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
