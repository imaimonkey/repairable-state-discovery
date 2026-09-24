# V2R cluster inventory

2026-09-24T04:49:38.317807+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324621758464 available bytes; 81.89% used; 112492819 free inodes.

server1 `/home`: 324621758464 available bytes; 81.89% used; 112492819 free inodes.

server1 `/tmp`: 324621758464 available bytes; 81.89% used; 112492819 free inodes.

server1 `/var/tmp`: 324621758464 available bytes; 81.89% used; 112492819 free inodes.

server1 `/mnt/raid5`: 469828841472 available bytes; 97.84% used; 337724590 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40768544768 available bytes; 97.73% used; 110430458 free inodes.

server2 `/home`: 40768544768 available bytes; 97.73% used; 110430458 free inodes.

server2 `/tmp`: 40768544768 available bytes; 97.73% used; 110430458 free inodes.

server2 `/var/tmp`: 40768544768 available bytes; 97.73% used; 110430458 free inodes.

server2 `/mnt/raid5`: 523917582336 available bytes; 96.38% used; 445195286 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292370608128 available bytes; 83.68% used; 114199698 free inodes.

server3 `/home`: 292370608128 available bytes; 83.68% used; 114199698 free inodes.

server3 `/data`: 24357752832 available bytes; 99.66% used; 225840618 free inodes.

server3 `/tmp`: 292370608128 available bytes; 83.68% used; 114199698 free inodes.

server3 `/var/tmp`: 292370608128 available bytes; 83.68% used; 114199698 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105836032000 available bytes; 94.09% used; 114349397 free inodes.

server4 `/home`: 105836032000 available bytes; 94.09% used; 114349397 free inodes.

server4 `/data`: 253373919232 available bytes; 96.50% used; 225366843 free inodes.

server4 `/tmp`: 105836032000 available bytes; 94.09% used; 114349397 free inodes.

server4 `/var/tmp`: 105836032000 available bytes; 94.09% used; 114349397 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
