# V2R cluster inventory

2026-09-25T06:22:56.682073+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318881394688 available bytes; 82.21% used; 112480351 free inodes.

server1 `/home`: 318881394688 available bytes; 82.21% used; 112480351 free inodes.

server1 `/tmp`: 318881394688 available bytes; 82.21% used; 112480351 free inodes.

server1 `/var/tmp`: 318881394688 available bytes; 82.21% used; 112480351 free inodes.

server1 `/mnt/raid5`: 401450586112 available bytes; 98.16% used; 337561897 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22894559232 available bytes; 98.72% used; 110410516 free inodes.

server2 `/home`: 22894559232 available bytes; 98.72% used; 110410516 free inodes.

server2 `/tmp`: 22894559232 available bytes; 98.72% used; 110410516 free inodes.

server2 `/var/tmp`: 22894559232 available bytes; 98.72% used; 110410516 free inodes.

server2 `/mnt/raid5`: 372837113856 available bytes; 97.42% used; 445100002 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84316213248 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84316213248 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142533292032 available bytes; 98.03% used; 225813912 free inodes.

server3 `/tmp`: 84316213248 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84316213248 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648431104 available bytes; 94.10% used; 114350390 free inodes.

server4 `/home`: 105648431104 available bytes; 94.10% used; 114350390 free inodes.

server4 `/data`: 254602756096 available bytes; 96.48% used; 225021973 free inodes.

server4 `/tmp`: 105648431104 available bytes; 94.10% used; 114350390 free inodes.

server4 `/var/tmp`: 105648431104 available bytes; 94.10% used; 114350390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
