# V2R cluster inventory

2026-09-26T12:46:55.898104+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318160130048 available bytes; 82.25% used; 112474503 free inodes.

server1 `/home`: 318160130048 available bytes; 82.25% used; 112474503 free inodes.

server1 `/tmp`: 318160130048 available bytes; 82.25% used; 112474503 free inodes.

server1 `/var/tmp`: 318160130048 available bytes; 82.25% used; 112474503 free inodes.

server1 `/mnt/raid5`: 679644418048 available bytes; 96.88% used; 337537767 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 19732029440 available bytes; 98.90% used; 110381951 free inodes.

server2 `/home`: 19732029440 available bytes; 98.90% used; 110381951 free inodes.

server2 `/tmp`: 19732029440 available bytes; 98.90% used; 110381951 free inodes.

server2 `/var/tmp`: 19732029440 available bytes; 98.90% used; 110381951 free inodes.

server2 `/mnt/raid5`: 637970911232 available bytes; 95.59% used; 444978152 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82648358912 available bytes; 95.39% used; 114110821 free inodes.

server3 `/home`: 82648358912 available bytes; 95.39% used; 114110821 free inodes.

server3 `/data`: 1347681476608 available bytes; 81.37% used; 225823527 free inodes.

server3 `/tmp`: 82648358912 available bytes; 95.39% used; 114110821 free inodes.

server3 `/var/tmp`: 82648358912 available bytes; 95.39% used; 114110821 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899364352 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105899364352 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 414306078720 available bytes; 94.27% used; 224867630 free inodes.

server4 `/tmp`: 105899364352 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105899364352 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
