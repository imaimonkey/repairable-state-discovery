# V2R cluster inventory

2026-09-24T22:28:26.135138+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323945226240 available bytes; 81.93% used; 112481420 free inodes.

server1 `/home`: 323945226240 available bytes; 81.93% used; 112481420 free inodes.

server1 `/tmp`: 323945226240 available bytes; 81.93% used; 112481420 free inodes.

server1 `/var/tmp`: 323945226240 available bytes; 81.93% used; 112481420 free inodes.

server1 `/mnt/raid5`: 415377743872 available bytes; 98.09% used; 337620530 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23216668672 available bytes; 98.70% used; 110410948 free inodes.

server2 `/home`: 23216668672 available bytes; 98.70% used; 110410948 free inodes.

server2 `/tmp`: 23216668672 available bytes; 98.70% used; 110410948 free inodes.

server2 `/var/tmp`: 23216668672 available bytes; 98.70% used; 110410948 free inodes.

server2 `/mnt/raid5`: 488592134144 available bytes; 96.62% used; 445153005 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84377825280 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84377825280 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 149329367040 available bytes; 97.94% used; 225802105 free inodes.

server3 `/tmp`: 84377825280 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84377825280 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['0', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810403328 available bytes; 94.10% used; 114348324 free inodes.

server4 `/home`: 105810403328 available bytes; 94.10% used; 114348324 free inodes.

server4 `/data`: 73292234752 available bytes; 98.99% used; 225227017 free inodes.

server4 `/tmp`: 105810403328 available bytes; 94.10% used; 114348324 free inodes.

server4 `/var/tmp`: 105810403328 available bytes; 94.10% used; 114348324 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
