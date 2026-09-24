# V2R cluster inventory

2026-09-24T03:16:46.017458+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325363322880 available bytes; 81.85% used; 112498292 free inodes.

server1 `/home`: 325363322880 available bytes; 81.85% used; 112498292 free inodes.

server1 `/tmp`: 325363322880 available bytes; 81.85% used; 112498292 free inodes.

server1 `/var/tmp`: 325363322880 available bytes; 81.85% used; 112498292 free inodes.

server1 `/mnt/raid5`: 451313254400 available bytes; 97.93% used; 337732221 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40846135296 available bytes; 97.72% used; 110431192 free inodes.

server2 `/home`: 40846135296 available bytes; 97.72% used; 110431192 free inodes.

server2 `/tmp`: 40846135296 available bytes; 97.72% used; 110431192 free inodes.

server2 `/var/tmp`: 40846135296 available bytes; 97.72% used; 110431192 free inodes.

server2 `/mnt/raid5`: 527552884736 available bytes; 96.35% used; 445197864 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292292653056 available bytes; 83.69% used; 114187092 free inodes.

server3 `/home`: 292292653056 available bytes; 83.69% used; 114187092 free inodes.

server3 `/data`: 39673401344 available bytes; 99.45% used; 225844661 free inodes.

server3 `/tmp`: 292292653056 available bytes; 83.69% used; 114187092 free inodes.

server3 `/var/tmp`: 292292653056 available bytes; 83.69% used; 114187092 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105987670016 available bytes; 94.09% used; 114349616 free inodes.

server4 `/home`: 105987670016 available bytes; 94.09% used; 114349616 free inodes.

server4 `/data`: 289658912768 available bytes; 96.00% used; 225386623 free inodes.

server4 `/tmp`: 105987670016 available bytes; 94.09% used; 114349616 free inodes.

server4 `/var/tmp`: 105987670016 available bytes; 94.09% used; 114349616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
