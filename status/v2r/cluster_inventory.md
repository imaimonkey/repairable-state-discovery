# V2R cluster inventory

2026-09-24T12:41:13.845913+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324043530240 available bytes; 81.92% used; 112481555 free inodes.

server1 `/home`: 324043530240 available bytes; 81.92% used; 112481555 free inodes.

server1 `/tmp`: 324043530240 available bytes; 81.92% used; 112481555 free inodes.

server1 `/var/tmp`: 324043530240 available bytes; 81.92% used; 112481555 free inodes.

server1 `/mnt/raid5`: 403383767040 available bytes; 98.15% used; 337681020 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57584017408 available bytes; 96.79% used; 110429229 free inodes.

server2 `/home`: 57584017408 available bytes; 96.79% used; 110429229 free inodes.

server2 `/tmp`: 57584017408 available bytes; 96.79% used; 110429229 free inodes.

server2 `/var/tmp`: 57584017408 available bytes; 96.79% used; 110429229 free inodes.

server2 `/mnt/raid5`: 508158070784 available bytes; 96.49% used; 445171423 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85703860224 available bytes; 95.22% used; 114197828 free inodes.

server3 `/home`: 85703860224 available bytes; 95.22% used; 114197828 free inodes.

server3 `/data`: 163223408640 available bytes; 97.74% used; 225814545 free inodes.

server3 `/tmp`: 85703860224 available bytes; 95.22% used; 114197828 free inodes.

server3 `/var/tmp`: 85703860224 available bytes; 95.22% used; 114197828 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780207616 available bytes; 94.10% used; 114348789 free inodes.

server4 `/home`: 105780207616 available bytes; 94.10% used; 114348789 free inodes.

server4 `/data`: 90051731456 available bytes; 98.76% used; 225257233 free inodes.

server4 `/tmp`: 105780207616 available bytes; 94.10% used; 114348789 free inodes.

server4 `/var/tmp`: 105780207616 available bytes; 94.10% used; 114348789 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
