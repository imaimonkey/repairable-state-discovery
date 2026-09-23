# V2R cluster inventory

2026-09-23T18:03:58.785406+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41368309760 available bytes; 97.69% used; 110435428 free inodes.

server2 `/home`: 41368309760 available bytes; 97.69% used; 110435428 free inodes.

server2 `/tmp`: 41368309760 available bytes; 97.69% used; 110435428 free inodes.

server2 `/var/tmp`: 41368309760 available bytes; 97.69% used; 110435428 free inodes.

server2 `/mnt/raid5`: 545905176576 available bytes; 96.23% used; 445214913 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293903900672 available bytes; 83.60% used; 114252959 free inodes.

server3 `/home`: 293903900672 available bytes; 83.60% used; 114252959 free inodes.

server3 `/data`: 52988391424 available bytes; 99.27% used; 225851257 free inodes.

server3 `/tmp`: 293903900672 available bytes; 83.60% used; 114252959 free inodes.

server3 `/var/tmp`: 293903900672 available bytes; 83.60% used; 114252959 free inodes.
| server4 | True | ['0', '1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111488061440 available bytes; 93.78% used; 114375774 free inodes.

server4 `/home`: 111488061440 available bytes; 93.78% used; 114375774 free inodes.

server4 `/data`: 3010560 available bytes; 100.00% used; 225457243 free inodes.

server4 `/tmp`: 111488061440 available bytes; 93.78% used; 114375774 free inodes.

server4 `/var/tmp`: 111488061440 available bytes; 93.78% used; 114375774 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
