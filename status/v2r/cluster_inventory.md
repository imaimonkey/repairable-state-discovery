# V2R cluster inventory

2026-09-25T22:03:14.108512+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318694281216 available bytes; 82.22% used; 112476295 free inodes.

server1 `/home`: 318694281216 available bytes; 82.22% used; 112476295 free inodes.

server1 `/tmp`: 318694281216 available bytes; 82.22% used; 112476295 free inodes.

server1 `/var/tmp`: 318694281216 available bytes; 82.22% used; 112476295 free inodes.

server1 `/mnt/raid5`: 360301441024 available bytes; 98.35% used; 337539065 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22904233984 available bytes; 98.72% used; 110405686 free inodes.

server2 `/home`: 22904233984 available bytes; 98.72% used; 110405686 free inodes.

server2 `/tmp`: 22904233984 available bytes; 98.72% used; 110405686 free inodes.

server2 `/var/tmp`: 22904233984 available bytes; 98.72% used; 110405686 free inodes.

server2 `/mnt/raid5`: 300159795200 available bytes; 97.93% used; 445053327 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84359303168 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84359303168 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 125882212352 available bytes; 98.26% used; 225806427 free inodes.

server3 `/tmp`: 84359303168 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84359303168 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105312444416 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105312444416 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208744800256 available bytes; 97.12% used; 224919068 free inodes.

server4 `/tmp`: 105312444416 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105312444416 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
