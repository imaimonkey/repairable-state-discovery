# V2R cluster inventory

2026-09-24T10:08:06.003013+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324421021696 available bytes; 81.90% used; 112489465 free inodes.

server1 `/home`: 324421021696 available bytes; 81.90% used; 112489465 free inodes.

server1 `/tmp`: 324421021696 available bytes; 81.90% used; 112489465 free inodes.

server1 `/var/tmp`: 324421021696 available bytes; 81.90% used; 112489465 free inodes.

server1 `/mnt/raid5`: 500674035712 available bytes; 97.70% used; 337700418 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57746014208 available bytes; 96.78% used; 110430717 free inodes.

server2 `/home`: 57746014208 available bytes; 96.78% used; 110430717 free inodes.

server2 `/tmp`: 57746014208 available bytes; 96.78% used; 110430717 free inodes.

server2 `/var/tmp`: 57746014208 available bytes; 96.78% used; 110430717 free inodes.

server2 `/mnt/raid5`: 513415618560 available bytes; 96.45% used; 445176517 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85379178496 available bytes; 95.24% used; 114173496 free inodes.

server3 `/home`: 85379178496 available bytes; 95.24% used; 114173496 free inodes.

server3 `/data`: 164459556864 available bytes; 97.73% used; 225819121 free inodes.

server3 `/tmp`: 85379178496 available bytes; 95.24% used; 114173496 free inodes.

server3 `/var/tmp`: 85379178496 available bytes; 95.24% used; 114173496 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747554304 available bytes; 94.10% used; 114349001 free inodes.

server4 `/home`: 105747554304 available bytes; 94.10% used; 114349001 free inodes.

server4 `/data`: 153504608256 available bytes; 97.88% used; 225258641 free inodes.

server4 `/tmp`: 105747554304 available bytes; 94.10% used; 114349001 free inodes.

server4 `/var/tmp`: 105747554304 available bytes; 94.10% used; 114349001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
