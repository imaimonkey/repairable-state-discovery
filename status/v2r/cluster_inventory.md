# V2R cluster inventory

2026-09-25T18:00:30.910885+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318662537216 available bytes; 82.22% used; 112476344 free inodes.

server1 `/home`: 318662537216 available bytes; 82.22% used; 112476344 free inodes.

server1 `/tmp`: 318662537216 available bytes; 82.22% used; 112476344 free inodes.

server1 `/var/tmp`: 318662537216 available bytes; 82.22% used; 112476344 free inodes.

server1 `/mnt/raid5`: 371232821248 available bytes; 98.30% used; 337542507 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23104929792 available bytes; 98.71% used; 110407930 free inodes.

server2 `/home`: 23104929792 available bytes; 98.71% used; 110407930 free inodes.

server2 `/tmp`: 23104929792 available bytes; 98.71% used; 110407930 free inodes.

server2 `/var/tmp`: 23104929792 available bytes; 98.71% used; 110407930 free inodes.

server2 `/mnt/raid5`: 314853437440 available bytes; 97.82% used; 445067722 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84395524096 available bytes; 95.29% used; 114152619 free inodes.

server3 `/home`: 84395524096 available bytes; 95.29% used; 114152619 free inodes.

server3 `/data`: 131477708800 available bytes; 98.18% used; 225810492 free inodes.

server3 `/tmp`: 84395524096 available bytes; 95.29% used; 114152619 free inodes.

server3 `/var/tmp`: 84395524096 available bytes; 95.29% used; 114152619 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616683008 available bytes; 94.11% used; 114349604 free inodes.

server4 `/home`: 105616683008 available bytes; 94.11% used; 114349604 free inodes.

server4 `/data`: 229736816640 available bytes; 96.82% used; 224932418 free inodes.

server4 `/tmp`: 105616683008 available bytes; 94.11% used; 114349604 free inodes.

server4 `/var/tmp`: 105616683008 available bytes; 94.11% used; 114349604 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
