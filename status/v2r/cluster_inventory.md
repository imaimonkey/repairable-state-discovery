# V2R cluster inventory

2026-09-25T17:58:58.993116+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318660849664 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318660849664 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318660849664 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318660849664 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 371231100928 available bytes; 98.30% used; 337542539 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23105482752 available bytes; 98.71% used; 110407930 free inodes.

server2 `/home`: 23105482752 available bytes; 98.71% used; 110407930 free inodes.

server2 `/tmp`: 23105482752 available bytes; 98.71% used; 110407930 free inodes.

server2 `/var/tmp`: 23105482752 available bytes; 98.71% used; 110407930 free inodes.

server2 `/mnt/raid5`: 315205472256 available bytes; 97.82% used; 445067896 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84397203456 available bytes; 95.29% used; 114152619 free inodes.

server3 `/home`: 84397203456 available bytes; 95.29% used; 114152619 free inodes.

server3 `/data`: 132523069440 available bytes; 98.17% used; 225810535 free inodes.

server3 `/tmp`: 84397203456 available bytes; 95.29% used; 114152619 free inodes.

server3 `/var/tmp`: 84397203456 available bytes; 95.29% used; 114152619 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616740352 available bytes; 94.11% used; 114349604 free inodes.

server4 `/home`: 105616740352 available bytes; 94.11% used; 114349604 free inodes.

server4 `/data`: 229736701952 available bytes; 96.82% used; 224932441 free inodes.

server4 `/tmp`: 105616740352 available bytes; 94.11% used; 114349604 free inodes.

server4 `/var/tmp`: 105616740352 available bytes; 94.11% used; 114349604 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
