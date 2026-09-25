# V2R cluster inventory

2026-09-25T03:55:04.406523+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318929879040 available bytes; 82.21% used; 112480358 free inodes.

server1 `/home`: 318929879040 available bytes; 82.21% used; 112480358 free inodes.

server1 `/tmp`: 318929879040 available bytes; 82.21% used; 112480358 free inodes.

server1 `/var/tmp`: 318929879040 available bytes; 82.21% used; 112480358 free inodes.

server1 `/mnt/raid5`: 415719698432 available bytes; 98.09% used; 337595918 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22972325888 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22972325888 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22972325888 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22972325888 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 464121638912 available bytes; 96.79% used; 445110863 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84346175488 available bytes; 95.29% used; 114156064 free inodes.

server3 `/home`: 84346175488 available bytes; 95.29% used; 114156064 free inodes.

server3 `/data`: 144178778112 available bytes; 98.01% used; 225816873 free inodes.

server3 `/tmp`: 84346175488 available bytes; 95.29% used; 114156064 free inodes.

server3 `/var/tmp`: 84346175488 available bytes; 95.29% used; 114156064 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683075072 available bytes; 94.10% used; 114350896 free inodes.

server4 `/home`: 105683075072 available bytes; 94.10% used; 114350896 free inodes.

server4 `/data`: 38552690688 available bytes; 99.47% used; 224964916 free inodes.

server4 `/tmp`: 105683075072 available bytes; 94.10% used; 114350896 free inodes.

server4 `/var/tmp`: 105683075072 available bytes; 94.10% used; 114350896 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
