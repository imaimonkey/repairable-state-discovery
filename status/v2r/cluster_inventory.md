# V2R cluster inventory

2026-09-23T15:40:22.955235+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41427013632 available bytes; 97.69% used; 110435185 free inodes.

server2 `/home`: 41427013632 available bytes; 97.69% used; 110435185 free inodes.

server2 `/tmp`: 41427013632 available bytes; 97.69% used; 110435185 free inodes.

server2 `/var/tmp`: 41427013632 available bytes; 97.69% used; 110435185 free inodes.

server2 `/mnt/raid5`: 550463696896 available bytes; 96.20% used; 445223298 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 377320747008 available bytes; 78.94% used; 114303963 free inodes.

server3 `/home`: 377320747008 available bytes; 78.94% used; 114303963 free inodes.

server3 `/data`: 125632184320 available bytes; 98.26% used; 225855584 free inodes.

server3 `/tmp`: 377320747008 available bytes; 78.94% used; 114303963 free inodes.

server3 `/var/tmp`: 377320747008 available bytes; 78.94% used; 114303963 free inodes.
| server4 | True | ['1', '2', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499468800 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499468800 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 38806188032 available bytes; 99.46% used; 225495023 free inodes.

server4 `/tmp`: 111499468800 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499468800 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
