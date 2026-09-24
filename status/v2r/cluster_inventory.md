# V2R cluster inventory

2026-09-24T22:25:21.474146+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323945742336 available bytes; 81.93% used; 112481420 free inodes.

server1 `/home`: 323945742336 available bytes; 81.93% used; 112481420 free inodes.

server1 `/tmp`: 323945742336 available bytes; 81.93% used; 112481420 free inodes.

server1 `/var/tmp`: 323945742336 available bytes; 81.93% used; 112481420 free inodes.

server1 `/mnt/raid5`: 415383621632 available bytes; 98.09% used; 337620890 free inodes.
| server2 | True | [] | [] |

server2 `/`: 25293393920 available bytes; 98.59% used; 110411077 free inodes.

server2 `/home`: 25293393920 available bytes; 98.59% used; 110411077 free inodes.

server2 `/tmp`: 25293393920 available bytes; 98.59% used; 110411077 free inodes.

server2 `/var/tmp`: 25293393920 available bytes; 98.59% used; 110411077 free inodes.

server2 `/mnt/raid5`: 488696291328 available bytes; 96.62% used; 445153306 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84378152960 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84378152960 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 149362577408 available bytes; 97.94% used; 225802160 free inodes.

server3 `/tmp`: 84378152960 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84378152960 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810509824 available bytes; 94.10% used; 114348324 free inodes.

server4 `/home`: 105810509824 available bytes; 94.10% used; 114348324 free inodes.

server4 `/data`: 73315205120 available bytes; 98.99% used; 225228318 free inodes.

server4 `/tmp`: 105810509824 available bytes; 94.10% used; 114348324 free inodes.

server4 `/var/tmp`: 105810509824 available bytes; 94.10% used; 114348324 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
