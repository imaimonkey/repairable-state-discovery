# V2R cluster inventory

2026-09-25T13:05:00.162160+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319112105984 available bytes; 82.20% used; 112477578 free inodes.

server1 `/home`: 319112105984 available bytes; 82.20% used; 112477578 free inodes.

server1 `/tmp`: 319112105984 available bytes; 82.20% used; 112477578 free inodes.

server1 `/var/tmp`: 319112105984 available bytes; 82.20% used; 112477578 free inodes.

server1 `/mnt/raid5`: 364236132352 available bytes; 98.33% used; 337547893 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 8295723008 available bytes; 99.54% used; 110408774 free inodes.

server2 `/home`: 8295723008 available bytes; 99.54% used; 110408774 free inodes.

server2 `/tmp`: 8295723008 available bytes; 99.54% used; 110408774 free inodes.

server2 `/var/tmp`: 8295723008 available bytes; 99.54% used; 110408774 free inodes.

server2 `/mnt/raid5`: 324169715712 available bytes; 97.76% used; 445077832 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84207124480 available bytes; 95.30% used; 114154966 free inodes.

server3 `/home`: 84207124480 available bytes; 95.30% used; 114154966 free inodes.

server3 `/data`: 142354190336 available bytes; 98.03% used; 225810120 free inodes.

server3 `/tmp`: 84207124480 available bytes; 95.30% used; 114154966 free inodes.

server3 `/var/tmp`: 84207124480 available bytes; 95.30% used; 114154966 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105656643584 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656643584 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231994957824 available bytes; 96.79% used; 224959584 free inodes.

server4 `/tmp`: 105656643584 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656643584 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
