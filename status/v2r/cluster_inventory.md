# V2R cluster inventory

2026-09-24T10:11:12.261384+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324419010560 available bytes; 81.90% used; 112489444 free inodes.

server1 `/home`: 324419010560 available bytes; 81.90% used; 112489444 free inodes.

server1 `/tmp`: 324419010560 available bytes; 81.90% used; 112489444 free inodes.

server1 `/var/tmp`: 324419010560 available bytes; 81.90% used; 112489444 free inodes.

server1 `/mnt/raid5`: 500664852480 available bytes; 97.70% used; 337700065 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57744760832 available bytes; 96.78% used; 110430709 free inodes.

server2 `/home`: 57744760832 available bytes; 96.78% used; 110430709 free inodes.

server2 `/tmp`: 57744760832 available bytes; 96.78% used; 110430709 free inodes.

server2 `/var/tmp`: 57744760832 available bytes; 96.78% used; 110430709 free inodes.

server2 `/mnt/raid5`: 513319956480 available bytes; 96.45% used; 445176018 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85377368064 available bytes; 95.24% used; 114173431 free inodes.

server3 `/home`: 85377368064 available bytes; 95.24% used; 114173431 free inodes.

server3 `/data`: 164437336064 available bytes; 97.73% used; 225819036 free inodes.

server3 `/tmp`: 85377368064 available bytes; 95.24% used; 114173431 free inodes.

server3 `/var/tmp`: 85377368064 available bytes; 95.24% used; 114173431 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747464192 available bytes; 94.10% used; 114349001 free inodes.

server4 `/home`: 105747464192 available bytes; 94.10% used; 114349001 free inodes.

server4 `/data`: 153499742208 available bytes; 97.88% used; 225258630 free inodes.

server4 `/tmp`: 105747464192 available bytes; 94.10% used; 114349001 free inodes.

server4 `/var/tmp`: 105747464192 available bytes; 94.10% used; 114349001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
