# V2R cluster inventory

2026-09-26T01:29:15.356010+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318649405440 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318649405440 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318649405440 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318649405440 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 345502875648 available bytes; 98.42% used; 337546561 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22929879040 available bytes; 98.72% used; 110406222 free inodes.

server2 `/home`: 22929879040 available bytes; 98.72% used; 110406222 free inodes.

server2 `/tmp`: 22929879040 available bytes; 98.72% used; 110406222 free inodes.

server2 `/var/tmp`: 22929879040 available bytes; 98.72% used; 110406222 free inodes.

server2 `/mnt/raid5`: 290756456448 available bytes; 97.99% used; 445056009 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84336164864 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84336164864 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124870967296 available bytes; 98.27% used; 225818056 free inodes.

server3 `/tmp`: 84336164864 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84336164864 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105264152576 available bytes; 94.13% used; 114347079 free inodes.

server4 `/home`: 105264152576 available bytes; 94.13% used; 114347079 free inodes.

server4 `/data`: 141687791616 available bytes; 98.04% used; 224917297 free inodes.

server4 `/tmp`: 105264152576 available bytes; 94.13% used; 114347079 free inodes.

server4 `/var/tmp`: 105264152576 available bytes; 94.13% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
