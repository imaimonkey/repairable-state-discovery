# V2R cluster inventory

2026-09-27T13:23:05.683386+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304671719424 available bytes; 83.00% used; 112401384 free inodes.

server1 `/home`: 304671719424 available bytes; 83.00% used; 112401384 free inodes.

server1 `/tmp`: 304671719424 available bytes; 83.00% used; 112401384 free inodes.

server1 `/var/tmp`: 304671719424 available bytes; 83.00% used; 112401384 free inodes.

server1 `/mnt/raid5`: 634576617472 available bytes; 97.09% used; 337424247 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13415915520 available bytes; 99.25% used; 110351833 free inodes.

server2 `/home`: 13415915520 available bytes; 99.25% used; 110351833 free inodes.

server2 `/tmp`: 13415915520 available bytes; 99.25% used; 110351833 free inodes.

server2 `/var/tmp`: 13415915520 available bytes; 99.25% used; 110351833 free inodes.

server2 `/mnt/raid5`: 528940183552 available bytes; 96.35% used; 444733400 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78572523520 available bytes; 95.62% used; 114062843 free inodes.

server3 `/home`: 78572523520 available bytes; 95.62% used; 114062843 free inodes.

server3 `/data`: 1331274772480 available bytes; 81.60% used; 225757560 free inodes.

server3 `/tmp`: 78572523520 available bytes; 95.62% used; 114062843 free inodes.

server3 `/var/tmp`: 78572523520 available bytes; 95.62% used; 114062843 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111010603008 available bytes; 93.81% used; 114372796 free inodes.

server4 `/home`: 111010603008 available bytes; 93.81% used; 114372796 free inodes.

server4 `/data`: 351399002112 available bytes; 95.14% used; 224727749 free inodes.

server4 `/tmp`: 111010603008 available bytes; 93.81% used; 114372796 free inodes.

server4 `/var/tmp`: 111010603008 available bytes; 93.81% used; 114372796 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
