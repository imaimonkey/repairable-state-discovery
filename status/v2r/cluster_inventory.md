# V2R cluster inventory

2026-09-24T04:27:23.109721+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324699627520 available bytes; 81.89% used; 112493182 free inodes.

server1 `/home`: 324699627520 available bytes; 81.89% used; 112493182 free inodes.

server1 `/tmp`: 324699627520 available bytes; 81.89% used; 112493182 free inodes.

server1 `/var/tmp`: 324699627520 available bytes; 81.89% used; 112493182 free inodes.

server1 `/mnt/raid5`: 445656915968 available bytes; 97.96% used; 337724686 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 40784896000 available bytes; 97.72% used; 110430574 free inodes.

server2 `/home`: 40784896000 available bytes; 97.72% used; 110430574 free inodes.

server2 `/tmp`: 40784896000 available bytes; 97.72% used; 110430574 free inodes.

server2 `/var/tmp`: 40784896000 available bytes; 97.72% used; 110430574 free inodes.

server2 `/mnt/raid5`: 525450383360 available bytes; 96.37% used; 445195777 free inodes.
| server3 | True | ['1', '3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292002123776 available bytes; 83.71% used; 114176153 free inodes.

server3 `/home`: 292002123776 available bytes; 83.71% used; 114176153 free inodes.

server3 `/data`: 29601918976 available bytes; 99.59% used; 225841081 free inodes.

server3 `/tmp`: 292002123776 available bytes; 83.71% used; 114176153 free inodes.

server3 `/var/tmp`: 292002123776 available bytes; 83.71% used; 114176153 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105844621312 available bytes; 94.09% used; 114349421 free inodes.

server4 `/home`: 105844621312 available bytes; 94.09% used; 114349421 free inodes.

server4 `/data`: 254472101888 available bytes; 96.48% used; 225381757 free inodes.

server4 `/tmp`: 105844621312 available bytes; 94.09% used; 114349421 free inodes.

server4 `/var/tmp`: 105844621312 available bytes; 94.09% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
