# V2R cluster inventory

2026-09-24T18:43:09.357255+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324003004416 available bytes; 81.93% used; 112481449 free inodes.

server1 `/home`: 324003004416 available bytes; 81.93% used; 112481449 free inodes.

server1 `/tmp`: 324003004416 available bytes; 81.93% used; 112481449 free inodes.

server1 `/var/tmp`: 324003004416 available bytes; 81.93% used; 112481449 free inodes.

server1 `/mnt/raid5`: 416293777408 available bytes; 98.09% used; 337637875 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54480420864 available bytes; 96.96% used; 110411943 free inodes.

server2 `/home`: 54480420864 available bytes; 96.96% used; 110411943 free inodes.

server2 `/tmp`: 54480420864 available bytes; 96.96% used; 110411943 free inodes.

server2 `/var/tmp`: 54480420864 available bytes; 96.96% used; 110411943 free inodes.

server2 `/mnt/raid5`: 496322772992 available bytes; 96.57% used; 445160229 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84406472704 available bytes; 95.29% used; 114156135 free inodes.

server3 `/home`: 84406472704 available bytes; 95.29% used; 114156135 free inodes.

server3 `/data`: 152758136832 available bytes; 97.89% used; 225800327 free inodes.

server3 `/tmp`: 84406472704 available bytes; 95.29% used; 114156135 free inodes.

server3 `/var/tmp`: 84406472704 available bytes; 95.29% used; 114156135 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105661861888 available bytes; 94.10% used; 114348505 free inodes.

server4 `/home`: 105661861888 available bytes; 94.10% used; 114348505 free inodes.

server4 `/data`: 90023862272 available bytes; 98.76% used; 225267752 free inodes.

server4 `/tmp`: 105661861888 available bytes; 94.10% used; 114348505 free inodes.

server4 `/var/tmp`: 105661861888 available bytes; 94.10% used; 114348505 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
