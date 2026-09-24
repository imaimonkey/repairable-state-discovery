# V2R cluster inventory

2026-09-24T07:48:11.415132+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324425330688 available bytes; 81.90% used; 112490881 free inodes.

server1 `/home`: 324425330688 available bytes; 81.90% used; 112490881 free inodes.

server1 `/tmp`: 324425330688 available bytes; 81.90% used; 112490881 free inodes.

server1 `/var/tmp`: 324425330688 available bytes; 81.90% used; 112490881 free inodes.

server1 `/mnt/raid5`: 510971510784 available bytes; 97.66% used; 337722661 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57831071744 available bytes; 96.77% used; 110431110 free inodes.

server2 `/home`: 57831071744 available bytes; 96.77% used; 110431110 free inodes.

server2 `/tmp`: 57831071744 available bytes; 96.77% used; 110431110 free inodes.

server2 `/var/tmp`: 57831071744 available bytes; 96.77% used; 110431110 free inodes.

server2 `/mnt/raid5`: 517732679680 available bytes; 96.42% used; 445180974 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127150768128 available bytes; 92.90% used; 114199799 free inodes.

server3 `/home`: 127150768128 available bytes; 92.90% used; 114199799 free inodes.

server3 `/data`: 137602461696 available bytes; 98.10% used; 225833365 free inodes.

server3 `/tmp`: 127150768128 available bytes; 92.90% used; 114199799 free inodes.

server3 `/var/tmp`: 127150768128 available bytes; 92.90% used; 114199799 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779859456 available bytes; 94.10% used; 114349172 free inodes.

server4 `/home`: 105779859456 available bytes; 94.10% used; 114349172 free inodes.

server4 `/data`: 285511917568 available bytes; 96.05% used; 225366751 free inodes.

server4 `/tmp`: 105779859456 available bytes; 94.10% used; 114349172 free inodes.

server4 `/var/tmp`: 105779859456 available bytes; 94.10% used; 114349172 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
