# V2R cluster inventory

2026-09-24T12:50:38.921930+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324039020544 available bytes; 81.92% used; 112481560 free inodes.

server1 `/home`: 324039020544 available bytes; 81.92% used; 112481560 free inodes.

server1 `/tmp`: 324039020544 available bytes; 81.92% used; 112481560 free inodes.

server1 `/var/tmp`: 324039020544 available bytes; 81.92% used; 112481560 free inodes.

server1 `/mnt/raid5`: 403356000256 available bytes; 98.15% used; 337679853 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57574981632 available bytes; 96.79% used; 110429129 free inodes.

server2 `/home`: 57574981632 available bytes; 96.79% used; 110429129 free inodes.

server2 `/tmp`: 57574981632 available bytes; 96.79% used; 110429129 free inodes.

server2 `/var/tmp`: 57574981632 available bytes; 96.79% used; 110429129 free inodes.

server2 `/mnt/raid5`: 507856543744 available bytes; 96.49% used; 445171017 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85670830080 available bytes; 95.22% used; 114194691 free inodes.

server3 `/home`: 85670830080 available bytes; 95.22% used; 114194691 free inodes.

server3 `/data`: 163098075136 available bytes; 97.75% used; 225814341 free inodes.

server3 `/tmp`: 85670830080 available bytes; 95.22% used; 114194691 free inodes.

server3 `/var/tmp`: 85670830080 available bytes; 95.22% used; 114194691 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779744768 available bytes; 94.10% used; 114348776 free inodes.

server4 `/home`: 105779744768 available bytes; 94.10% used; 114348776 free inodes.

server4 `/data`: 90048638976 available bytes; 98.76% used; 225257224 free inodes.

server4 `/tmp`: 105779744768 available bytes; 94.10% used; 114348776 free inodes.

server4 `/var/tmp`: 105779744768 available bytes; 94.10% used; 114348776 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
