# V2R cluster inventory

2026-09-25T10:15:29.897309+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318834417664 available bytes; 82.21% used; 112480394 free inodes.

server1 `/home`: 318834417664 available bytes; 82.21% used; 112480394 free inodes.

server1 `/tmp`: 318834417664 available bytes; 82.21% used; 112480394 free inodes.

server1 `/var/tmp`: 318834417664 available bytes; 82.21% used; 112480394 free inodes.

server1 `/mnt/raid5`: 370335473664 available bytes; 98.30% used; 337556479 free inodes.
| server2 | True | ['3', '6'] | [] | reference_compatible=False |

server2 `/`: 22834094080 available bytes; 98.73% used; 110410482 free inodes.

server2 `/home`: 22834094080 available bytes; 98.73% used; 110410482 free inodes.

server2 `/tmp`: 22834094080 available bytes; 98.73% used; 110410482 free inodes.

server2 `/var/tmp`: 22834094080 available bytes; 98.73% used; 110410482 free inodes.

server2 `/mnt/raid5`: 316600291328 available bytes; 97.81% used; 445090961 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417441792 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84417441792 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142026452992 available bytes; 98.04% used; 225816113 free inodes.

server3 `/tmp`: 84417441792 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84417441792 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105613938688 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105613938688 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240065576960 available bytes; 96.68% used; 224989348 free inodes.

server4 `/tmp`: 105613938688 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105613938688 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
