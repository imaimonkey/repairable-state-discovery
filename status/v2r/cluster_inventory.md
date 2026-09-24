# V2R cluster inventory

2026-09-24T12:59:57.891307+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324039524352 available bytes; 81.92% used; 112481555 free inodes.

server1 `/home`: 324039524352 available bytes; 81.92% used; 112481555 free inodes.

server1 `/tmp`: 324039524352 available bytes; 81.92% used; 112481555 free inodes.

server1 `/var/tmp`: 324039524352 available bytes; 81.92% used; 112481555 free inodes.

server1 `/mnt/raid5`: 417083977728 available bytes; 98.09% used; 337678733 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57560342528 available bytes; 96.79% used; 110429035 free inodes.

server2 `/home`: 57560342528 available bytes; 96.79% used; 110429035 free inodes.

server2 `/tmp`: 57560342528 available bytes; 96.79% used; 110429035 free inodes.

server2 `/var/tmp`: 57560342528 available bytes; 96.79% used; 110429035 free inodes.

server2 `/mnt/raid5`: 507583504384 available bytes; 96.49% used; 445170601 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85241663488 available bytes; 95.24% used; 114169148 free inodes.

server3 `/home`: 85241663488 available bytes; 95.24% used; 114169148 free inodes.

server3 `/data`: 163025412096 available bytes; 97.75% used; 225813746 free inodes.

server3 `/tmp`: 85241663488 available bytes; 95.24% used; 114169148 free inodes.

server3 `/var/tmp`: 85241663488 available bytes; 95.24% used; 114169148 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779392512 available bytes; 94.10% used; 114348765 free inodes.

server4 `/home`: 105779392512 available bytes; 94.10% used; 114348765 free inodes.

server4 `/data`: 90025730048 available bytes; 98.76% used; 225257181 free inodes.

server4 `/tmp`: 105779392512 available bytes; 94.10% used; 114348765 free inodes.

server4 `/var/tmp`: 105779392512 available bytes; 94.10% used; 114348765 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
