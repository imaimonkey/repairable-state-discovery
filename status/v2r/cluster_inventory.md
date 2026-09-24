# V2R cluster inventory

2026-09-24T04:31:12.708838+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324696051712 available bytes; 81.89% used; 112493152 free inodes.

server1 `/home`: 324696051712 available bytes; 81.89% used; 112493152 free inodes.

server1 `/tmp`: 324696051712 available bytes; 81.89% used; 112493152 free inodes.

server1 `/var/tmp`: 324696051712 available bytes; 81.89% used; 112493152 free inodes.

server1 `/mnt/raid5`: 450496520192 available bytes; 97.93% used; 337724679 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40782221312 available bytes; 97.72% used; 110430538 free inodes.

server2 `/home`: 40782221312 available bytes; 97.72% used; 110430538 free inodes.

server2 `/tmp`: 40782221312 available bytes; 97.72% used; 110430538 free inodes.

server2 `/var/tmp`: 40782221312 available bytes; 97.72% used; 110430538 free inodes.

server2 `/mnt/raid5`: 525321732096 available bytes; 96.37% used; 445196038 free inodes.
| server3 | True | ['1', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292003983360 available bytes; 83.71% used; 114176144 free inodes.

server3 `/home`: 292003983360 available bytes; 83.71% used; 114176144 free inodes.

server3 `/data`: 27526664192 available bytes; 99.62% used; 225840952 free inodes.

server3 `/tmp`: 292003983360 available bytes; 83.71% used; 114176144 free inodes.

server3 `/var/tmp`: 292003983360 available bytes; 83.71% used; 114176144 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105844465664 available bytes; 94.09% used; 114349421 free inodes.

server4 `/home`: 105844465664 available bytes; 94.09% used; 114349421 free inodes.

server4 `/data`: 253411520512 available bytes; 96.50% used; 225366911 free inodes.

server4 `/tmp`: 105844465664 available bytes; 94.09% used; 114349421 free inodes.

server4 `/var/tmp`: 105844465664 available bytes; 94.09% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
