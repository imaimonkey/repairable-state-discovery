# V2R cluster inventory

2026-09-25T12:40:46.864949+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319128956928 available bytes; 82.20% used; 112477610 free inodes.

server1 `/home`: 319128956928 available bytes; 82.20% used; 112477610 free inodes.

server1 `/tmp`: 319128956928 available bytes; 82.20% used; 112477610 free inodes.

server1 `/var/tmp`: 319128956928 available bytes; 82.20% used; 112477610 free inodes.

server1 `/mnt/raid5`: 364257722368 available bytes; 98.33% used; 337548059 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 20257103872 available bytes; 98.87% used; 110409418 free inodes.

server2 `/home`: 20257103872 available bytes; 98.87% used; 110409418 free inodes.

server2 `/tmp`: 20257103872 available bytes; 98.87% used; 110409418 free inodes.

server2 `/var/tmp`: 20257103872 available bytes; 98.87% used; 110409418 free inodes.

server2 `/mnt/raid5`: 324810428416 available bytes; 97.76% used; 445079066 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84209430528 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84209430528 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142279118848 available bytes; 98.03% used; 225811035 free inodes.

server3 `/tmp`: 84209430528 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84209430528 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105665753088 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665753088 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231949271040 available bytes; 96.79% used; 224963154 free inodes.

server4 `/tmp`: 105665753088 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665753088 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
