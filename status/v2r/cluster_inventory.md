# V2R cluster inventory

2026-09-25T06:59:30.174178+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318871519232 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318871519232 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318871519232 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318871519232 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 399711657984 available bytes; 98.17% used; 337560484 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22878240768 available bytes; 98.72% used; 110410524 free inodes.

server2 `/home`: 22878240768 available bytes; 98.72% used; 110410524 free inodes.

server2 `/tmp`: 22878240768 available bytes; 98.72% used; 110410524 free inodes.

server2 `/var/tmp`: 22878240768 available bytes; 98.72% used; 110410524 free inodes.

server2 `/mnt/raid5`: 337882890240 available bytes; 97.67% used; 445098301 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84448063488 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84448063488 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142449655808 available bytes; 98.03% used; 225813230 free inodes.

server3 `/tmp`: 84448063488 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84448063488 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638801408 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638801408 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249501892608 available bytes; 96.55% used; 225017234 free inodes.

server4 `/tmp`: 105638801408 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638801408 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
