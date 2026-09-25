# V2R cluster inventory

2026-09-25T10:56:48.032775+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319064293376 available bytes; 82.20% used; 112478862 free inodes.

server1 `/home`: 319064293376 available bytes; 82.20% used; 112478862 free inodes.

server1 `/tmp`: 319064293376 available bytes; 82.20% used; 112478862 free inodes.

server1 `/var/tmp`: 319064293376 available bytes; 82.20% used; 112478862 free inodes.

server1 `/mnt/raid5`: 367095840768 available bytes; 98.32% used; 337555225 free inodes.
| server2 | True | ['1', '2', '3', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22913007616 available bytes; 98.72% used; 110409992 free inodes.

server2 `/home`: 22913007616 available bytes; 98.72% used; 110409992 free inodes.

server2 `/tmp`: 22913007616 available bytes; 98.72% used; 110409992 free inodes.

server2 `/var/tmp`: 22913007616 available bytes; 98.72% used; 110409992 free inodes.

server2 `/mnt/raid5`: 329207742464 available bytes; 97.73% used; 445089185 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84502757376 available bytes; 95.28% used; 114155533 free inodes.

server3 `/home`: 84502757376 available bytes; 95.28% used; 114155533 free inodes.

server3 `/data`: 142005784576 available bytes; 98.04% used; 225815261 free inodes.

server3 `/tmp`: 84502757376 available bytes; 95.28% used; 114155533 free inodes.

server3 `/var/tmp`: 84502757376 available bytes; 95.28% used; 114155533 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105612578816 available bytes; 94.11% used; 114350252 free inodes.

server4 `/home`: 105612578816 available bytes; 94.11% used; 114350252 free inodes.

server4 `/data`: 238574977024 available bytes; 96.70% used; 224984321 free inodes.

server4 `/tmp`: 105612578816 available bytes; 94.11% used; 114350252 free inodes.

server4 `/var/tmp`: 105612578816 available bytes; 94.11% used; 114350252 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
