# V2R cluster inventory

2026-09-25T16:31:48.213682+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318686064640 available bytes; 82.22% used; 112476338 free inodes.

server1 `/home`: 318686064640 available bytes; 82.22% used; 112476338 free inodes.

server1 `/tmp`: 318686064640 available bytes; 82.22% used; 112476338 free inodes.

server1 `/var/tmp`: 318686064640 available bytes; 82.22% used; 112476338 free inodes.

server1 `/mnt/raid5`: 363911737344 available bytes; 98.33% used; 337544578 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23098212352 available bytes; 98.71% used; 110407930 free inodes.

server2 `/home`: 23098212352 available bytes; 98.71% used; 110407930 free inodes.

server2 `/tmp`: 23098212352 available bytes; 98.71% used; 110407930 free inodes.

server2 `/var/tmp`: 23098212352 available bytes; 98.71% used; 110407930 free inodes.

server2 `/mnt/raid5`: 317220380672 available bytes; 97.81% used; 445070199 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84402077696 available bytes; 95.29% used; 114152664 free inodes.

server3 `/home`: 84402077696 available bytes; 95.29% used; 114152664 free inodes.

server3 `/data`: 133800325120 available bytes; 98.15% used; 225805748 free inodes.

server3 `/tmp`: 84402077696 available bytes; 95.29% used; 114152664 free inodes.

server3 `/var/tmp`: 84402077696 available bytes; 95.29% used; 114152664 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636069376 available bytes; 94.11% used; 114349645 free inodes.

server4 `/home`: 105636069376 available bytes; 94.11% used; 114349645 free inodes.

server4 `/data`: 230029389824 available bytes; 96.82% used; 224934056 free inodes.

server4 `/tmp`: 105636069376 available bytes; 94.11% used; 114349645 free inodes.

server4 `/var/tmp`: 105636069376 available bytes; 94.11% used; 114349645 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
