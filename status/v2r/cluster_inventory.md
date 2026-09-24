# V2R cluster inventory

2026-09-24T03:08:51.220463+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325368987648 available bytes; 81.85% used; 112498446 free inodes.

server1 `/home`: 325368987648 available bytes; 81.85% used; 112498446 free inodes.

server1 `/tmp`: 325368987648 available bytes; 81.85% used; 112498446 free inodes.

server1 `/var/tmp`: 325368987648 available bytes; 81.85% used; 112498446 free inodes.

server1 `/mnt/raid5`: 482152935424 available bytes; 97.79% used; 337732327 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40858984448 available bytes; 97.72% used; 110431264 free inodes.

server2 `/home`: 40858984448 available bytes; 97.72% used; 110431264 free inodes.

server2 `/tmp`: 40858984448 available bytes; 97.72% used; 110431264 free inodes.

server2 `/var/tmp`: 40858984448 available bytes; 97.72% used; 110431264 free inodes.

server2 `/mnt/raid5`: 527805423616 available bytes; 96.35% used; 445198126 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292289863680 available bytes; 83.69% used; 114187183 free inodes.

server3 `/home`: 292289863680 available bytes; 83.69% used; 114187183 free inodes.

server3 `/data`: 39685873664 available bytes; 99.45% used; 225844814 free inodes.

server3 `/tmp`: 292289863680 available bytes; 83.69% used; 114187183 free inodes.

server3 `/var/tmp`: 292289863680 available bytes; 83.69% used; 114187183 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105988055040 available bytes; 94.09% used; 114349625 free inodes.

server4 `/home`: 105988055040 available bytes; 94.09% used; 114349625 free inodes.

server4 `/data`: 289703088128 available bytes; 96.00% used; 225386844 free inodes.

server4 `/tmp`: 105988055040 available bytes; 94.09% used; 114349625 free inodes.

server4 `/var/tmp`: 105988055040 available bytes; 94.09% used; 114349625 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
