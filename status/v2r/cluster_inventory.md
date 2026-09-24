# V2R cluster inventory

2026-09-24T08:13:03.589210+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324406018048 available bytes; 81.90% used; 112490639 free inodes.

server1 `/home`: 324406018048 available bytes; 81.90% used; 112490639 free inodes.

server1 `/tmp`: 324406018048 available bytes; 81.90% used; 112490639 free inodes.

server1 `/var/tmp`: 324406018048 available bytes; 81.90% used; 112490639 free inodes.

server1 `/mnt/raid5`: 496618119168 available bytes; 97.72% used; 337721358 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57818062848 available bytes; 96.77% used; 110431040 free inodes.

server2 `/home`: 57818062848 available bytes; 96.77% used; 110431040 free inodes.

server2 `/tmp`: 57818062848 available bytes; 96.77% used; 110431040 free inodes.

server2 `/var/tmp`: 57818062848 available bytes; 96.77% used; 110431040 free inodes.

server2 `/mnt/raid5`: 516689260544 available bytes; 96.43% used; 445180406 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85482868736 available bytes; 95.23% used; 114175164 free inodes.

server3 `/home`: 85482868736 available bytes; 95.23% used; 114175164 free inodes.

server3 `/data`: 176258969600 available bytes; 97.56% used; 225838143 free inodes.

server3 `/tmp`: 85482868736 available bytes; 95.23% used; 114175164 free inodes.

server3 `/var/tmp`: 85482868736 available bytes; 95.23% used; 114175164 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778589696 available bytes; 94.10% used; 114349150 free inodes.

server4 `/home`: 105778589696 available bytes; 94.10% used; 114349150 free inodes.

server4 `/data`: 283892789248 available bytes; 96.08% used; 225365772 free inodes.

server4 `/tmp`: 105778589696 available bytes; 94.10% used; 114349150 free inodes.

server4 `/var/tmp`: 105778589696 available bytes; 94.10% used; 114349150 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
