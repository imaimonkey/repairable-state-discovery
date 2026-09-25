# V2R cluster inventory

2026-09-25T16:16:30.090161+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318671626240 available bytes; 82.22% used; 112476328 free inodes.

server1 `/home`: 318671626240 available bytes; 82.22% used; 112476328 free inodes.

server1 `/tmp`: 318671626240 available bytes; 82.22% used; 112476328 free inodes.

server1 `/var/tmp`: 318671626240 available bytes; 82.22% used; 112476328 free inodes.

server1 `/mnt/raid5`: 363900694528 available bytes; 98.33% used; 337544951 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23108653056 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23108653056 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23108653056 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23108653056 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 318752784384 available bytes; 97.80% used; 445070875 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84401942528 available bytes; 95.29% used; 114152674 free inodes.

server3 `/home`: 84401942528 available bytes; 95.29% used; 114152674 free inodes.

server3 `/data`: 134928101376 available bytes; 98.14% used; 225806161 free inodes.

server3 `/tmp`: 84401942528 available bytes; 95.29% used; 114152674 free inodes.

server3 `/var/tmp`: 84401942528 available bytes; 95.29% used; 114152674 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636507648 available bytes; 94.11% used; 114349647 free inodes.

server4 `/home`: 105636507648 available bytes; 94.11% used; 114349647 free inodes.

server4 `/data`: 230240931840 available bytes; 96.82% used; 224934482 free inodes.

server4 `/tmp`: 105636507648 available bytes; 94.11% used; 114349647 free inodes.

server4 `/var/tmp`: 105636507648 available bytes; 94.11% used; 114349647 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
