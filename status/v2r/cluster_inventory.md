# V2R cluster inventory

2026-09-24T02:36:06.612324+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325386657792 available bytes; 81.85% used; 112498824 free inodes.

server1 `/home`: 325386657792 available bytes; 81.85% used; 112498824 free inodes.

server1 `/tmp`: 325386657792 available bytes; 81.85% used; 112498824 free inodes.

server1 `/var/tmp`: 325386657792 available bytes; 81.85% used; 112498824 free inodes.

server1 `/mnt/raid5`: 601163214848 available bytes; 97.24% used; 337733234 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40888463360 available bytes; 97.72% used; 110431494 free inodes.

server2 `/home`: 40888463360 available bytes; 97.72% used; 110431494 free inodes.

server2 `/tmp`: 40888463360 available bytes; 97.72% used; 110431494 free inodes.

server2 `/var/tmp`: 40888463360 available bytes; 97.72% used; 110431494 free inodes.

server2 `/mnt/raid5`: 528822210560 available bytes; 96.35% used; 445199268 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292289728512 available bytes; 83.69% used; 114187092 free inodes.

server3 `/home`: 292289728512 available bytes; 83.69% used; 114187092 free inodes.

server3 `/data`: 39744028672 available bytes; 99.45% used; 225846219 free inodes.

server3 `/tmp`: 292289728512 available bytes; 83.69% used; 114187092 free inodes.

server3 `/var/tmp`: 292289728512 available bytes; 83.69% used; 114187092 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106003456000 available bytes; 94.08% used; 114349838 free inodes.

server4 `/home`: 106003456000 available bytes; 94.08% used; 114349838 free inodes.

server4 `/data`: 289732702208 available bytes; 96.00% used; 225387392 free inodes.

server4 `/tmp`: 106003456000 available bytes; 94.08% used; 114349838 free inodes.

server4 `/var/tmp`: 106003456000 available bytes; 94.08% used; 114349838 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
