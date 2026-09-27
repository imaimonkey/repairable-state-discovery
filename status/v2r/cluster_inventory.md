# V2R cluster inventory

2026-09-27T04:21:35.305752+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314910289920 available bytes; 82.43% used; 112443036 free inodes.

server1 `/home`: 314910289920 available bytes; 82.43% used; 112443036 free inodes.

server1 `/tmp`: 314910289920 available bytes; 82.43% used; 112443036 free inodes.

server1 `/var/tmp`: 314910289920 available bytes; 82.43% used; 112443036 free inodes.

server1 `/mnt/raid5`: 636075429888 available bytes; 97.08% used; 337400377 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17622999040 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17622999040 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17622999040 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17622999040 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 577147322368 available bytes; 96.01% used; 444880952 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78696939520 available bytes; 95.61% used; 114062932 free inodes.

server3 `/home`: 78696939520 available bytes; 95.61% used; 114062932 free inodes.

server3 `/data`: 1335168901120 available bytes; 81.55% used; 225759278 free inodes.

server3 `/tmp`: 78696939520 available bytes; 95.61% used; 114062932 free inodes.

server3 `/var/tmp`: 78696939520 available bytes; 95.61% used; 114062932 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111018336256 available bytes; 93.80% used; 114372940 free inodes.

server4 `/home`: 111018336256 available bytes; 93.80% used; 114372940 free inodes.

server4 `/data`: 382148866048 available bytes; 94.72% used; 224780572 free inodes.

server4 `/tmp`: 111018336256 available bytes; 93.80% used; 114372940 free inodes.

server4 `/var/tmp`: 111018336256 available bytes; 93.80% used; 114372940 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
