# V2R cluster inventory

2026-09-25T07:09:12.800944+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872178688 available bytes; 82.21% used; 112480372 free inodes.

server1 `/home`: 318872178688 available bytes; 82.21% used; 112480372 free inodes.

server1 `/tmp`: 318872178688 available bytes; 82.21% used; 112480372 free inodes.

server1 `/var/tmp`: 318872178688 available bytes; 82.21% used; 112480372 free inodes.

server1 `/mnt/raid5`: 401082912768 available bytes; 98.16% used; 337558502 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22870437888 available bytes; 98.72% used; 110410502 free inodes.

server2 `/home`: 22870437888 available bytes; 98.72% used; 110410502 free inodes.

server2 `/tmp`: 22870437888 available bytes; 98.72% used; 110410502 free inodes.

server2 `/var/tmp`: 22870437888 available bytes; 98.72% used; 110410502 free inodes.

server2 `/mnt/raid5`: 330323148800 available bytes; 97.72% used; 445098377 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84447334400 available bytes; 95.29% used; 114156033 free inodes.

server3 `/home`: 84447334400 available bytes; 95.29% used; 114156033 free inodes.

server3 `/data`: 142459027456 available bytes; 98.03% used; 225813083 free inodes.

server3 `/tmp`: 84447334400 available bytes; 95.29% used; 114156033 free inodes.

server3 `/var/tmp`: 84447334400 available bytes; 95.29% used; 114156033 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638510592 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638510592 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249484271616 available bytes; 96.55% used; 225016571 free inodes.

server4 `/tmp`: 105638510592 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638510592 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
