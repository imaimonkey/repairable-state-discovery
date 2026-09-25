# V2R cluster inventory

2026-09-25T23:14:58.607604+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318683799552 available bytes; 82.22% used; 112476296 free inodes.

server1 `/home`: 318683799552 available bytes; 82.22% used; 112476296 free inodes.

server1 `/tmp`: 318683799552 available bytes; 82.22% used; 112476296 free inodes.

server1 `/var/tmp`: 318683799552 available bytes; 82.22% used; 112476296 free inodes.

server1 `/mnt/raid5`: 360146763776 available bytes; 98.35% used; 337538732 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22950334464 available bytes; 98.72% used; 110406230 free inodes.

server2 `/home`: 22950334464 available bytes; 98.72% used; 110406230 free inodes.

server2 `/tmp`: 22950334464 available bytes; 98.72% used; 110406230 free inodes.

server2 `/var/tmp`: 22950334464 available bytes; 98.72% used; 110406230 free inodes.

server2 `/mnt/raid5`: 297744797696 available bytes; 97.94% used; 445051595 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84348350464 available bytes; 95.29% used; 114152432 free inodes.

server3 `/home`: 84348350464 available bytes; 95.29% used; 114152432 free inodes.

server3 `/data`: 124754898944 available bytes; 98.28% used; 225805188 free inodes.

server3 `/tmp`: 84348350464 available bytes; 95.29% used; 114152432 free inodes.

server3 `/var/tmp`: 84348350464 available bytes; 95.29% used; 114152432 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105159159808 available bytes; 94.13% used; 114346790 free inodes.

server4 `/home`: 105159159808 available bytes; 94.13% used; 114346790 free inodes.

server4 `/data`: 185179340800 available bytes; 97.44% used; 224917643 free inodes.

server4 `/tmp`: 105159159808 available bytes; 94.13% used; 114346790 free inodes.

server4 `/var/tmp`: 105159159808 available bytes; 94.13% used; 114346790 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
