# V2R cluster inventory

2026-09-25T22:06:18.787149+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318694666240 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318694666240 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318694666240 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318694666240 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 360296996864 available bytes; 98.35% used; 337539061 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22904860672 available bytes; 98.72% used; 110405688 free inodes.

server2 `/home`: 22904860672 available bytes; 98.72% used; 110405688 free inodes.

server2 `/tmp`: 22904860672 available bytes; 98.72% used; 110405688 free inodes.

server2 `/var/tmp`: 22904860672 available bytes; 98.72% used; 110405688 free inodes.

server2 `/mnt/raid5`: 300098334720 available bytes; 97.93% used; 445053928 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84359991296 available bytes; 95.29% used; 114152632 free inodes.

server3 `/home`: 84359991296 available bytes; 95.29% used; 114152632 free inodes.

server3 `/data`: 125877927936 available bytes; 98.26% used; 225806376 free inodes.

server3 `/tmp`: 84359991296 available bytes; 95.29% used; 114152632 free inodes.

server3 `/var/tmp`: 84359991296 available bytes; 95.29% used; 114152632 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105312346112 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105312346112 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208749322240 available bytes; 97.12% used; 224919051 free inodes.

server4 `/tmp`: 105312346112 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105312346112 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
