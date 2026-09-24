# V2R cluster inventory

2026-09-24T22:17:40.086311+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323948486656 available bytes; 81.93% used; 112481421 free inodes.

server1 `/home`: 323948486656 available bytes; 81.93% used; 112481421 free inodes.

server1 `/tmp`: 323948486656 available bytes; 81.93% used; 112481421 free inodes.

server1 `/var/tmp`: 323948486656 available bytes; 81.93% used; 112481421 free inodes.

server1 `/mnt/raid5`: 415398285312 available bytes; 98.09% used; 337621781 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30113071104 available bytes; 98.32% used; 110411302 free inodes.

server2 `/home`: 30113071104 available bytes; 98.32% used; 110411302 free inodes.

server2 `/tmp`: 30113071104 available bytes; 98.32% used; 110411302 free inodes.

server2 `/var/tmp`: 30113071104 available bytes; 98.32% used; 110411302 free inodes.

server2 `/mnt/raid5`: 488385417216 available bytes; 96.63% used; 445153531 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381847552 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84381847552 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 149488214016 available bytes; 97.93% used; 225802299 free inodes.

server3 `/tmp`: 84381847552 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84381847552 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810685952 available bytes; 94.10% used; 114348326 free inodes.

server4 `/home`: 105810685952 available bytes; 94.10% used; 114348326 free inodes.

server4 `/data`: 73395023872 available bytes; 98.99% used; 225232432 free inodes.

server4 `/tmp`: 105810685952 available bytes; 94.10% used; 114348326 free inodes.

server4 `/var/tmp`: 105810685952 available bytes; 94.10% used; 114348326 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
