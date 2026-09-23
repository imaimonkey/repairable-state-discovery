# V2R cluster inventory

2026-09-23T16:06:21.979489+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41416359936 available bytes; 97.69% used; 110435187 free inodes.

server2 `/home`: 41416359936 available bytes; 97.69% used; 110435187 free inodes.

server2 `/tmp`: 41416359936 available bytes; 97.69% used; 110435187 free inodes.

server2 `/var/tmp`: 41416359936 available bytes; 97.69% used; 110435187 free inodes.

server2 `/mnt/raid5`: 549506576384 available bytes; 96.20% used; 445218485 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 352774651904 available bytes; 80.31% used; 114296080 free inodes.

server3 `/home`: 352774651904 available bytes; 80.31% used; 114296080 free inodes.

server3 `/data`: 125334126592 available bytes; 98.27% used; 225854524 free inodes.

server3 `/tmp`: 352774651904 available bytes; 80.31% used; 114296080 free inodes.

server3 `/var/tmp`: 352774651904 available bytes; 80.31% used; 114296080 free inodes.
| server4 | True | ['3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498993664 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111498993664 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 37480726528 available bytes; 99.48% used; 225486605 free inodes.

server4 `/tmp`: 111498993664 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111498993664 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
