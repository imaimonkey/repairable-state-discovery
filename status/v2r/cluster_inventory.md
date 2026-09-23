# V2R cluster inventory

2026-09-23T16:04:50.370100+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41416028160 available bytes; 97.69% used; 110435187 free inodes.

server2 `/home`: 41416028160 available bytes; 97.69% used; 110435187 free inodes.

server2 `/tmp`: 41416028160 available bytes; 97.69% used; 110435187 free inodes.

server2 `/var/tmp`: 41416028160 available bytes; 97.69% used; 110435187 free inodes.

server2 `/mnt/raid5`: 549541801984 available bytes; 96.20% used; 445218431 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 352776142848 available bytes; 80.31% used; 114296096 free inodes.

server3 `/home`: 352776142848 available bytes; 80.31% used; 114296096 free inodes.

server3 `/data`: 125334847488 available bytes; 98.27% used; 225854530 free inodes.

server3 `/tmp`: 352776142848 available bytes; 80.31% used; 114296096 free inodes.

server3 `/var/tmp`: 352776142848 available bytes; 80.31% used; 114296096 free inodes.
| server4 | True | ['3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499026432 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499026432 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 37484101632 available bytes; 99.48% used; 225486607 free inodes.

server4 `/tmp`: 111499026432 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499026432 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
