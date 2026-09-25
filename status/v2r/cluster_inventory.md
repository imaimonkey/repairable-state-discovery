# V2R cluster inventory

2026-09-25T15:45:50.423875+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318682501120 available bytes; 82.22% used; 112476528 free inodes.

server1 `/home`: 318682501120 available bytes; 82.22% used; 112476528 free inodes.

server1 `/tmp`: 318682501120 available bytes; 82.22% used; 112476528 free inodes.

server1 `/var/tmp`: 318682501120 available bytes; 82.22% used; 112476528 free inodes.

server1 `/mnt/raid5`: 363984605184 available bytes; 98.33% used; 337545541 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23109775360 available bytes; 98.71% used; 110407944 free inodes.

server2 `/home`: 23109775360 available bytes; 98.71% used; 110407944 free inodes.

server2 `/tmp`: 23109775360 available bytes; 98.71% used; 110407944 free inodes.

server2 `/var/tmp`: 23109775360 available bytes; 98.71% used; 110407944 free inodes.

server2 `/mnt/raid5`: 319064723456 available bytes; 97.80% used; 445072292 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84427419648 available bytes; 95.29% used; 114153473 free inodes.

server3 `/home`: 84427419648 available bytes; 95.29% used; 114153473 free inodes.

server3 `/data`: 142245138432 available bytes; 98.03% used; 225806970 free inodes.

server3 `/tmp`: 84427419648 available bytes; 95.29% used; 114153473 free inodes.

server3 `/var/tmp`: 84427419648 available bytes; 95.29% used; 114153473 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637486592 available bytes; 94.11% used; 114349678 free inodes.

server4 `/home`: 105637486592 available bytes; 94.11% used; 114349678 free inodes.

server4 `/data`: 231349248000 available bytes; 96.80% used; 224943825 free inodes.

server4 `/tmp`: 105637486592 available bytes; 94.11% used; 114349678 free inodes.

server4 `/var/tmp`: 105637486592 available bytes; 94.11% used; 114349678 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
