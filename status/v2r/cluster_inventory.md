# V2R cluster inventory

2026-09-25T07:10:44.674066+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318873718784 available bytes; 82.21% used; 112480378 free inodes.

server1 `/home`: 318873718784 available bytes; 82.21% used; 112480378 free inodes.

server1 `/tmp`: 318873718784 available bytes; 82.21% used; 112480378 free inodes.

server1 `/var/tmp`: 318873718784 available bytes; 82.21% used; 112480378 free inodes.

server1 `/mnt/raid5`: 399705133056 available bytes; 98.17% used; 337558542 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22869622784 available bytes; 98.72% used; 110410502 free inodes.

server2 `/home`: 22869622784 available bytes; 98.72% used; 110410502 free inodes.

server2 `/tmp`: 22869622784 available bytes; 98.72% used; 110410502 free inodes.

server2 `/var/tmp`: 22869622784 available bytes; 98.72% used; 110410502 free inodes.

server2 `/mnt/raid5`: 330275065856 available bytes; 97.72% used; 445098216 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84448776192 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84448776192 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142457950208 available bytes; 98.03% used; 225813045 free inodes.

server3 `/tmp`: 84448776192 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84448776192 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638457344 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638457344 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249482997760 available bytes; 96.55% used; 225016408 free inodes.

server4 `/tmp`: 105638457344 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638457344 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
