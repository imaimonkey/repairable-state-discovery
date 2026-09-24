# V2R cluster inventory

2026-09-24T08:28:35.652109+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324401930240 available bytes; 81.90% used; 112490474 free inodes.

server1 `/home`: 324401930240 available bytes; 81.90% used; 112490474 free inodes.

server1 `/tmp`: 324401930240 available bytes; 81.90% used; 112490474 free inodes.

server1 `/var/tmp`: 324401930240 available bytes; 81.90% used; 112490474 free inodes.

server1 `/mnt/raid5`: 510143111168 available bytes; 97.66% used; 337721220 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57808826368 available bytes; 96.78% used; 110431004 free inodes.

server2 `/home`: 57808826368 available bytes; 96.78% used; 110431004 free inodes.

server2 `/tmp`: 57808826368 available bytes; 96.78% used; 110431004 free inodes.

server2 `/var/tmp`: 57808826368 available bytes; 96.78% used; 110431004 free inodes.

server2 `/mnt/raid5`: 516190277632 available bytes; 96.43% used; 445179471 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85482676224 available bytes; 95.23% used; 114174994 free inodes.

server3 `/home`: 85482676224 available bytes; 95.23% used; 114174994 free inodes.

server3 `/data`: 175079063552 available bytes; 97.58% used; 225823004 free inodes.

server3 `/tmp`: 85482676224 available bytes; 95.23% used; 114174994 free inodes.

server3 `/var/tmp`: 85482676224 available bytes; 95.23% used; 114174994 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769324544 available bytes; 94.10% used; 114349121 free inodes.

server4 `/home`: 105769324544 available bytes; 94.10% used; 114349121 free inodes.

server4 `/data`: 280435343360 available bytes; 96.12% used; 225350777 free inodes.

server4 `/tmp`: 105769324544 available bytes; 94.10% used; 114349121 free inodes.

server4 `/var/tmp`: 105769324544 available bytes; 94.10% used; 114349121 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
