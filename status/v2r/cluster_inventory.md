# V2R cluster inventory

2026-09-23T23:53:21.681023+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325584957440 available bytes; 81.84% used; 112500985 free inodes.

server1 `/home`: 325584957440 available bytes; 81.84% used; 112500985 free inodes.

server1 `/tmp`: 325584957440 available bytes; 81.84% used; 112500985 free inodes.

server1 `/var/tmp`: 325584957440 available bytes; 81.84% used; 112500985 free inodes.

server1 `/mnt/raid5`: 1295140933632 available bytes; 94.06% used; 337735418 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41022976000 available bytes; 97.71% used; 110432474 free inodes.

server2 `/home`: 41022976000 available bytes; 97.71% used; 110432474 free inodes.

server2 `/tmp`: 41022976000 available bytes; 97.71% used; 110432474 free inodes.

server2 `/var/tmp`: 41022976000 available bytes; 97.71% used; 110432474 free inodes.

server2 `/mnt/raid5`: 533735092224 available bytes; 96.31% used; 445204578 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292808142848 available bytes; 83.66% used; 114214059 free inodes.

server3 `/home`: 292808142848 available bytes; 83.66% used; 114214059 free inodes.

server3 `/data`: 82280546304 available bytes; 98.86% used; 225844965 free inodes.

server3 `/tmp`: 292808142848 available bytes; 83.66% used; 114214059 free inodes.

server3 `/var/tmp`: 292808142848 available bytes; 83.66% used; 114214059 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106153492480 available bytes; 94.08% used; 114351507 free inodes.

server4 `/home`: 106153492480 available bytes; 94.08% used; 114351507 free inodes.

server4 `/data`: 292961943552 available bytes; 95.95% used; 225417109 free inodes.

server4 `/tmp`: 106153492480 available bytes; 94.08% used; 114351507 free inodes.

server4 `/var/tmp`: 106153492480 available bytes; 94.08% used; 114351507 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
