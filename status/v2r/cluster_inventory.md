# V2R cluster inventory

2026-09-23T22:19:23.566298+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325708140544 available bytes; 81.83% used; 112501407 free inodes.

server1 `/home`: 325708140544 available bytes; 81.83% used; 112501407 free inodes.

server1 `/tmp`: 325708140544 available bytes; 81.83% used; 112501407 free inodes.

server1 `/var/tmp`: 325708140544 available bytes; 81.83% used; 112501407 free inodes.

server1 `/mnt/raid5`: 1388106416128 available bytes; 93.63% used; 337739858 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41092014080 available bytes; 97.71% used; 110432647 free inodes.

server2 `/home`: 41092014080 available bytes; 97.71% used; 110432647 free inodes.

server2 `/tmp`: 41092014080 available bytes; 97.71% used; 110432647 free inodes.

server2 `/var/tmp`: 41092014080 available bytes; 97.71% used; 110432647 free inodes.

server2 `/mnt/raid5`: 536999403520 available bytes; 96.29% used; 445207057 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292929224704 available bytes; 83.65% used; 114221132 free inodes.

server3 `/home`: 292929224704 available bytes; 83.65% used; 114221132 free inodes.

server3 `/data`: 82440138752 available bytes; 98.86% used; 225847537 free inodes.

server3 `/tmp`: 292929224704 available bytes; 83.65% used; 114221132 free inodes.

server3 `/var/tmp`: 292929224704 available bytes; 83.65% used; 114221132 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106406117376 available bytes; 94.06% used; 114354923 free inodes.

server4 `/home`: 106406117376 available bytes; 94.06% used; 114354923 free inodes.

server4 `/data`: 300112015360 available bytes; 95.85% used; 225439618 free inodes.

server4 `/tmp`: 106406117376 available bytes; 94.06% used; 114354923 free inodes.

server4 `/var/tmp`: 106406117376 available bytes; 94.06% used; 114354923 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
