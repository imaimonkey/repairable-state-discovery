# V2R cluster inventory

2026-09-24T00:35:04.734992+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325547253760 available bytes; 81.84% used; 112500540 free inodes.

server1 `/home`: 325547253760 available bytes; 81.84% used; 112500540 free inodes.

server1 `/tmp`: 325547253760 available bytes; 81.84% used; 112500540 free inodes.

server1 `/var/tmp`: 325547253760 available bytes; 81.84% used; 112500540 free inodes.

server1 `/mnt/raid5`: 1122944548864 available bytes; 94.85% used; 337735093 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40993067008 available bytes; 97.71% used; 110432323 free inodes.

server2 `/home`: 40993067008 available bytes; 97.71% used; 110432323 free inodes.

server2 `/tmp`: 40993067008 available bytes; 97.71% used; 110432323 free inodes.

server2 `/var/tmp`: 40993067008 available bytes; 97.71% used; 110432323 free inodes.

server2 `/mnt/raid5`: 532627525632 available bytes; 96.32% used; 445203164 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292291403776 available bytes; 83.69% used; 114187574 free inodes.

server3 `/home`: 292291403776 available bytes; 83.69% used; 114187574 free inodes.

server3 `/data`: 82235748352 available bytes; 98.86% used; 225844136 free inodes.

server3 `/tmp`: 292291403776 available bytes; 83.69% used; 114187574 free inodes.

server3 `/var/tmp`: 292291403776 available bytes; 83.69% used; 114187574 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106071580672 available bytes; 94.08% used; 114350214 free inodes.

server4 `/home`: 106071580672 available bytes; 94.08% used; 114350214 free inodes.

server4 `/data`: 292919181312 available bytes; 95.95% used; 225414581 free inodes.

server4 `/tmp`: 106071580672 available bytes; 94.08% used; 114350214 free inodes.

server4 `/var/tmp`: 106071580672 available bytes; 94.08% used; 114350214 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
