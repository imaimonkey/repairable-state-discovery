# V2R cluster inventory

2026-09-25T20:19:38.773405+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318707605504 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318707605504 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318707605504 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318707605504 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 369858105344 available bytes; 98.30% used; 337540540 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23085989888 available bytes; 98.71% used; 110407934 free inodes.

server2 `/home`: 23085989888 available bytes; 98.71% used; 110407934 free inodes.

server2 `/tmp`: 23085989888 available bytes; 98.71% used; 110407934 free inodes.

server2 `/var/tmp`: 23085989888 available bytes; 98.71% used; 110407934 free inodes.

server2 `/mnt/raid5`: 310581571584 available bytes; 97.85% used; 445062915 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380110848 available bytes; 95.29% used; 114152620 free inodes.

server3 `/home`: 84380110848 available bytes; 95.29% used; 114152620 free inodes.

server3 `/data`: 127184388096 available bytes; 98.24% used; 225808220 free inodes.

server3 `/tmp`: 84380110848 available bytes; 95.29% used; 114152620 free inodes.

server3 `/var/tmp`: 84380110848 available bytes; 95.29% used; 114152620 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105664835584 available bytes; 94.10% used; 114349570 free inodes.

server4 `/home`: 105664835584 available bytes; 94.10% used; 114349570 free inodes.

server4 `/data`: 229123633152 available bytes; 96.83% used; 224929095 free inodes.

server4 `/tmp`: 105664835584 available bytes; 94.10% used; 114349570 free inodes.

server4 `/var/tmp`: 105664835584 available bytes; 94.10% used; 114349570 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
