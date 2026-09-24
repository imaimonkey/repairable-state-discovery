# V2R cluster inventory

2026-09-24T10:34:29.925994+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324409577472 available bytes; 81.90% used; 112489245 free inodes.

server1 `/home`: 324409577472 available bytes; 81.90% used; 112489245 free inodes.

server1 `/tmp`: 324409577472 available bytes; 81.90% used; 112489245 free inodes.

server1 `/var/tmp`: 324409577472 available bytes; 81.90% used; 112489245 free inodes.

server1 `/mnt/raid5`: 500008521728 available bytes; 97.71% used; 337697306 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57729900544 available bytes; 96.78% used; 110430567 free inodes.

server2 `/home`: 57729900544 available bytes; 96.78% used; 110430567 free inodes.

server2 `/tmp`: 57729900544 available bytes; 96.78% used; 110430567 free inodes.

server2 `/var/tmp`: 57729900544 available bytes; 96.78% used; 110430567 free inodes.

server2 `/mnt/raid5`: 512658276352 available bytes; 96.46% used; 445175194 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 85790826496 available bytes; 95.21% used; 114199145 free inodes.

server3 `/home`: 85790826496 available bytes; 95.21% used; 114199145 free inodes.

server3 `/data`: 164195934208 available bytes; 97.73% used; 225818161 free inodes.

server3 `/tmp`: 85790826496 available bytes; 95.21% used; 114199145 free inodes.

server3 `/var/tmp`: 85790826496 available bytes; 95.21% used; 114199145 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744326656 available bytes; 94.10% used; 114348960 free inodes.

server4 `/home`: 105744326656 available bytes; 94.10% used; 114348960 free inodes.

server4 `/data`: 153477222400 available bytes; 97.88% used; 225258392 free inodes.

server4 `/tmp`: 105744326656 available bytes; 94.10% used; 114348960 free inodes.

server4 `/var/tmp`: 105744326656 available bytes; 94.10% used; 114348960 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
