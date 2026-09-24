# V2R cluster inventory

2026-09-24T21:36:10.094662+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323955556352 available bytes; 81.93% used; 112481418 free inodes.

server1 `/home`: 323955556352 available bytes; 81.93% used; 112481418 free inodes.

server1 `/tmp`: 323955556352 available bytes; 81.93% used; 112481418 free inodes.

server1 `/var/tmp`: 323955556352 available bytes; 81.93% used; 112481418 free inodes.

server1 `/mnt/raid5`: 415489077248 available bytes; 98.09% used; 337626760 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30138322944 available bytes; 98.32% used; 110411326 free inodes.

server2 `/home`: 30138322944 available bytes; 98.32% used; 110411326 free inodes.

server2 `/tmp`: 30138322944 available bytes; 98.32% used; 110411326 free inodes.

server2 `/var/tmp`: 30138322944 available bytes; 98.32% used; 110411326 free inodes.

server2 `/mnt/raid5`: 490214899712 available bytes; 96.61% used; 445154963 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84385980416 available bytes; 95.29% used; 114156093 free inodes.

server3 `/home`: 84385980416 available bytes; 95.29% used; 114156093 free inodes.

server3 `/data`: 150189797376 available bytes; 97.92% used; 225803085 free inodes.

server3 `/tmp`: 84385980416 available bytes; 95.29% used; 114156093 free inodes.

server3 `/var/tmp`: 84385980416 available bytes; 95.29% used; 114156093 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105629974528 available bytes; 94.11% used; 114348349 free inodes.

server4 `/home`: 105629974528 available bytes; 94.11% used; 114348349 free inodes.

server4 `/data`: 82885259264 available bytes; 98.85% used; 225252465 free inodes.

server4 `/tmp`: 105629974528 available bytes; 94.11% used; 114348349 free inodes.

server4 `/var/tmp`: 105629974528 available bytes; 94.11% used; 114348349 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
