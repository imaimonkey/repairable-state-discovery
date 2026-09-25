# V2R cluster inventory

2026-09-25T17:40:37.294823+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318670831616 available bytes; 82.22% used; 112476352 free inodes.

server1 `/home`: 318670831616 available bytes; 82.22% used; 112476352 free inodes.

server1 `/tmp`: 318670831616 available bytes; 82.22% used; 112476352 free inodes.

server1 `/var/tmp`: 318670831616 available bytes; 82.22% used; 112476352 free inodes.

server1 `/mnt/raid5`: 363770425344 available bytes; 98.33% used; 337542854 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23097257984 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23097257984 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23097257984 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23097257984 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 315706511360 available bytes; 97.82% used; 445067544 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84391608320 available bytes; 95.29% used; 114152611 free inodes.

server3 `/home`: 84391608320 available bytes; 95.29% used; 114152611 free inodes.

server3 `/data`: 132542586880 available bytes; 98.17% used; 225810975 free inodes.

server3 `/tmp`: 84391608320 available bytes; 95.29% used; 114152611 free inodes.

server3 `/var/tmp`: 84391608320 available bytes; 95.29% used; 114152611 free inodes.
| server4 | True | ['1', '3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105617362944 available bytes; 94.11% used; 114349646 free inodes.

server4 `/home`: 105617362944 available bytes; 94.11% used; 114349646 free inodes.

server4 `/data`: 229795762176 available bytes; 96.82% used; 224932716 free inodes.

server4 `/tmp`: 105617362944 available bytes; 94.11% used; 114349646 free inodes.

server4 `/var/tmp`: 105617362944 available bytes; 94.11% used; 114349646 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
