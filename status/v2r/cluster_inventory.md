# V2R cluster inventory

2026-09-25T05:04:25.898208+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318901563392 available bytes; 82.21% used; 112480334 free inodes.

server1 `/home`: 318901563392 available bytes; 82.21% used; 112480334 free inodes.

server1 `/tmp`: 318901563392 available bytes; 82.21% used; 112480334 free inodes.

server1 `/var/tmp`: 318901563392 available bytes; 82.21% used; 112480334 free inodes.

server1 `/mnt/raid5`: 408615936000 available bytes; 98.13% used; 337571532 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22937358336 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22937358336 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22937358336 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22937358336 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 461966266368 available bytes; 96.81% used; 445109173 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340461568 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84340461568 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 142885339136 available bytes; 98.03% used; 225815473 free inodes.

server3 `/tmp`: 84340461568 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84340461568 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105659240448 available bytes; 94.10% used; 114350405 free inodes.

server4 `/home`: 105659240448 available bytes; 94.10% used; 114350405 free inodes.

server4 `/data`: 27939864576 available bytes; 99.61% used; 224960986 free inodes.

server4 `/tmp`: 105659240448 available bytes; 94.10% used; 114350405 free inodes.

server4 `/var/tmp`: 105659240448 available bytes; 94.10% used; 114350405 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
