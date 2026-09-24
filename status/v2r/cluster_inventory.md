# V2R cluster inventory

2026-09-24T02:29:52.186344+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325386051584 available bytes; 81.85% used; 112498877 free inodes.

server1 `/home`: 325386051584 available bytes; 81.85% used; 112498877 free inodes.

server1 `/tmp`: 325386051584 available bytes; 81.85% used; 112498877 free inodes.

server1 `/var/tmp`: 325386051584 available bytes; 81.85% used; 112498877 free inodes.

server1 `/mnt/raid5`: 648426446848 available bytes; 97.03% used; 337733260 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40891654144 available bytes; 97.72% used; 110431538 free inodes.

server2 `/home`: 40891654144 available bytes; 97.72% used; 110431538 free inodes.

server2 `/tmp`: 40891654144 available bytes; 97.72% used; 110431538 free inodes.

server2 `/var/tmp`: 40891654144 available bytes; 97.72% used; 110431538 free inodes.

server2 `/mnt/raid5`: 529043324928 available bytes; 96.34% used; 445199772 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291856928768 available bytes; 83.71% used; 114163138 free inodes.

server3 `/home`: 291856928768 available bytes; 83.71% used; 114163138 free inodes.

server3 `/data`: 39758098432 available bytes; 99.45% used; 225846397 free inodes.

server3 `/tmp`: 291856928768 available bytes; 83.71% used; 114163138 free inodes.

server3 `/var/tmp`: 291856928768 available bytes; 83.71% used; 114163138 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106003734528 available bytes; 94.08% used; 114349842 free inodes.

server4 `/home`: 106003734528 available bytes; 94.08% used; 114349842 free inodes.

server4 `/data`: 289734557696 available bytes; 96.00% used; 225387512 free inodes.

server4 `/tmp`: 106003734528 available bytes; 94.08% used; 114349842 free inodes.

server4 `/var/tmp`: 106003734528 available bytes; 94.08% used; 114349842 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
