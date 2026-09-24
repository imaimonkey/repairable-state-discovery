# V2R cluster inventory

2026-09-24T00:41:16.019877+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325540667392 available bytes; 81.84% used; 112500466 free inodes.

server1 `/home`: 325540667392 available bytes; 81.84% used; 112500466 free inodes.

server1 `/tmp`: 325540667392 available bytes; 81.84% used; 112500466 free inodes.

server1 `/var/tmp`: 325540667392 available bytes; 81.84% used; 112500466 free inodes.

server1 `/mnt/raid5`: 1097269137408 available bytes; 94.97% used; 337735035 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40984113152 available bytes; 97.71% used; 110432297 free inodes.

server2 `/home`: 40984113152 available bytes; 97.71% used; 110432297 free inodes.

server2 `/tmp`: 40984113152 available bytes; 97.71% used; 110432297 free inodes.

server2 `/var/tmp`: 40984113152 available bytes; 97.71% used; 110432297 free inodes.

server2 `/mnt/raid5`: 531898925056 available bytes; 96.32% used; 445202965 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292289306624 available bytes; 83.69% used; 114187336 free inodes.

server3 `/home`: 292289306624 available bytes; 83.69% used; 114187336 free inodes.

server3 `/data`: 82230587392 available bytes; 98.86% used; 225843973 free inodes.

server3 `/tmp`: 292289306624 available bytes; 83.69% used; 114187336 free inodes.

server3 `/var/tmp`: 292289306624 available bytes; 83.69% used; 114187336 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106060722176 available bytes; 94.08% used; 114350046 free inodes.

server4 `/home`: 106060722176 available bytes; 94.08% used; 114350046 free inodes.

server4 `/data`: 292918448128 available bytes; 95.95% used; 225414580 free inodes.

server4 `/tmp`: 106060722176 available bytes; 94.08% used; 114350046 free inodes.

server4 `/var/tmp`: 106060722176 available bytes; 94.08% used; 114350046 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
