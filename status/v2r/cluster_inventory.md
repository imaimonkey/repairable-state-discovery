# V2R cluster inventory

2026-09-25T16:01:08.658247+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318680289280 available bytes; 82.22% used; 112476507 free inodes.

server1 `/home`: 318680289280 available bytes; 82.22% used; 112476507 free inodes.

server1 `/tmp`: 318680289280 available bytes; 82.22% used; 112476507 free inodes.

server1 `/var/tmp`: 318680289280 available bytes; 82.22% used; 112476507 free inodes.

server1 `/mnt/raid5`: 363941818368 available bytes; 98.33% used; 337545233 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23117598720 available bytes; 98.71% used; 110407948 free inodes.

server2 `/home`: 23117598720 available bytes; 98.71% used; 110407948 free inodes.

server2 `/tmp`: 23117598720 available bytes; 98.71% used; 110407948 free inodes.

server2 `/var/tmp`: 23117598720 available bytes; 98.71% used; 110407948 free inodes.

server2 `/mnt/raid5`: 319192629248 available bytes; 97.79% used; 445071540 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 84405002240 available bytes; 95.29% used; 114152687 free inodes.

server3 `/home`: 84405002240 available bytes; 95.29% used; 114152687 free inodes.

server3 `/data`: 138037936128 available bytes; 98.09% used; 225806507 free inodes.

server3 `/tmp`: 84405002240 available bytes; 95.29% used; 114152687 free inodes.

server3 `/var/tmp`: 84405002240 available bytes; 95.29% used; 114152687 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636970496 available bytes; 94.11% used; 114349663 free inodes.

server4 `/home`: 105636970496 available bytes; 94.11% used; 114349663 free inodes.

server4 `/data`: 231294803968 available bytes; 96.80% used; 224943311 free inodes.

server4 `/tmp`: 105636970496 available bytes; 94.11% used; 114349663 free inodes.

server4 `/var/tmp`: 105636970496 available bytes; 94.11% used; 114349663 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
