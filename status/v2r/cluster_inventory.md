# V2R cluster inventory

2026-09-25T05:41:23.538672+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871650304 available bytes; 82.21% used; 112480333 free inodes.

server1 `/home`: 318871650304 available bytes; 82.21% used; 112480333 free inodes.

server1 `/tmp`: 318871650304 available bytes; 82.21% used; 112480333 free inodes.

server1 `/var/tmp`: 318871650304 available bytes; 82.21% used; 112480333 free inodes.

server1 `/mnt/raid5`: 408465756160 available bytes; 98.13% used; 337566929 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22911459328 available bytes; 98.72% used; 110410431 free inodes.

server2 `/home`: 22911459328 available bytes; 98.72% used; 110410431 free inodes.

server2 `/tmp`: 22911459328 available bytes; 98.72% used; 110410431 free inodes.

server2 `/var/tmp`: 22911459328 available bytes; 98.72% used; 110410431 free inodes.

server2 `/mnt/raid5`: 438422376448 available bytes; 96.97% used; 445102800 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84313313280 available bytes; 95.30% used; 114156039 free inodes.

server3 `/home`: 84313313280 available bytes; 95.30% used; 114156039 free inodes.

server3 `/data`: 142776545280 available bytes; 98.03% used; 225814629 free inodes.

server3 `/tmp`: 84313313280 available bytes; 95.30% used; 114156039 free inodes.

server3 `/var/tmp`: 84313313280 available bytes; 95.30% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649664000 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105649664000 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 24765206528 available bytes; 99.66% used; 224966342 free inodes.

server4 `/tmp`: 105649664000 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105649664000 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
