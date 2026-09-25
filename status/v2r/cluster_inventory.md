# V2R cluster inventory

2026-09-25T04:30:34.626185+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318930206720 available bytes; 82.21% used; 112480365 free inodes.

server1 `/home`: 318930206720 available bytes; 82.21% used; 112480365 free inodes.

server1 `/tmp`: 318930206720 available bytes; 82.21% used; 112480365 free inodes.

server1 `/var/tmp`: 318930206720 available bytes; 82.21% used; 112480365 free inodes.

server1 `/mnt/raid5`: 408735383552 available bytes; 98.12% used; 337591651 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22955855872 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22955855872 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22955855872 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22955855872 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 463020429312 available bytes; 96.80% used; 445110065 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341444608 available bytes; 95.29% used; 114156080 free inodes.

server3 `/home`: 84341444608 available bytes; 95.29% used; 114156080 free inodes.

server3 `/data`: 143507050496 available bytes; 98.02% used; 225816126 free inodes.

server3 `/tmp`: 84341444608 available bytes; 95.29% used; 114156080 free inodes.

server3 `/var/tmp`: 84341444608 available bytes; 95.29% used; 114156080 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105671421952 available bytes; 94.10% used; 114350875 free inodes.

server4 `/home`: 105671421952 available bytes; 94.10% used; 114350875 free inodes.

server4 `/data`: 32799756288 available bytes; 99.55% used; 224962934 free inodes.

server4 `/tmp`: 105671421952 available bytes; 94.10% used; 114350875 free inodes.

server4 `/var/tmp`: 105671421952 available bytes; 94.10% used; 114350875 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
