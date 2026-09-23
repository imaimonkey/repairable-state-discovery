# V2R cluster inventory

2026-09-23T18:49:45.764585+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41345220608 available bytes; 97.69% used; 110435450 free inodes.

server2 `/home`: 41345220608 available bytes; 97.69% used; 110435450 free inodes.

server2 `/tmp`: 41345220608 available bytes; 97.69% used; 110435450 free inodes.

server2 `/var/tmp`: 41345220608 available bytes; 97.69% used; 110435450 free inodes.

server2 `/mnt/raid5`: 544351383552 available bytes; 96.24% used; 445213446 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294162149376 available bytes; 83.58% used; 114268432 free inodes.

server3 `/home`: 294162149376 available bytes; 83.58% used; 114268432 free inodes.

server3 `/data`: 52819853312 available bytes; 99.27% used; 225846737 free inodes.

server3 `/tmp`: 294162149376 available bytes; 83.58% used; 114268432 free inodes.

server3 `/var/tmp`: 294162149376 available bytes; 83.58% used; 114268432 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111412092928 available bytes; 93.78% used; 114373055 free inodes.

server4 `/home`: 111412092928 available bytes; 93.78% used; 114373055 free inodes.

server4 `/data`: 18227200 available bytes; 100.00% used; 225458135 free inodes.

server4 `/tmp`: 111412092928 available bytes; 93.78% used; 114373055 free inodes.

server4 `/var/tmp`: 111412092928 available bytes; 93.78% used; 114373055 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
