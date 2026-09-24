# V2R cluster inventory

2026-09-24T03:31:09.720069+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325193310208 available bytes; 81.86% used; 112497327 free inodes.

server1 `/home`: 325193310208 available bytes; 81.86% used; 112497327 free inodes.

server1 `/tmp`: 325193310208 available bytes; 81.86% used; 112497327 free inodes.

server1 `/var/tmp`: 325193310208 available bytes; 81.86% used; 112497327 free inodes.

server1 `/mnt/raid5`: 378813583360 available bytes; 98.26% used; 337734047 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40835375104 available bytes; 97.72% used; 110431096 free inodes.

server2 `/home`: 40835375104 available bytes; 97.72% used; 110431096 free inodes.

server2 `/tmp`: 40835375104 available bytes; 97.72% used; 110431096 free inodes.

server2 `/var/tmp`: 40835375104 available bytes; 97.72% used; 110431096 free inodes.

server2 `/mnt/raid5`: 527181901824 available bytes; 96.36% used; 445197894 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292364791808 available bytes; 83.68% used; 114200778 free inodes.

server3 `/home`: 292364791808 available bytes; 83.68% used; 114200778 free inodes.

server3 `/data`: 36013125632 available bytes; 99.50% used; 225843012 free inodes.

server3 `/tmp`: 292364791808 available bytes; 83.68% used; 114200778 free inodes.

server3 `/var/tmp`: 292364791808 available bytes; 83.68% used; 114200778 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105987035136 available bytes; 94.09% used; 114349606 free inodes.

server4 `/home`: 105987035136 available bytes; 94.09% used; 114349606 free inodes.

server4 `/data`: 282329128960 available bytes; 96.10% used; 225385521 free inodes.

server4 `/tmp`: 105987035136 available bytes; 94.09% used; 114349606 free inodes.

server4 `/var/tmp`: 105987035136 available bytes; 94.09% used; 114349606 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
