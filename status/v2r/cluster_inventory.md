# V2R cluster inventory

2026-09-24T14:39:41.491560+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324052099072 available bytes; 81.92% used; 112481477 free inodes.

server1 `/home`: 324052099072 available bytes; 81.92% used; 112481477 free inodes.

server1 `/tmp`: 324052099072 available bytes; 81.92% used; 112481477 free inodes.

server1 `/var/tmp`: 324052099072 available bytes; 81.92% used; 112481477 free inodes.

server1 `/mnt/raid5`: 416870617088 available bytes; 98.09% used; 337667087 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57445732352 available bytes; 96.80% used; 110428013 free inodes.

server2 `/home`: 57445732352 available bytes; 96.80% used; 110428013 free inodes.

server2 `/tmp`: 57445732352 available bytes; 96.80% used; 110428013 free inodes.

server2 `/var/tmp`: 57445732352 available bytes; 96.80% used; 110428013 free inodes.

server2 `/mnt/raid5`: 504196505600 available bytes; 96.52% used; 445167790 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84482514944 available bytes; 95.29% used; 114158854 free inodes.

server3 `/home`: 84482514944 available bytes; 95.29% used; 114158854 free inodes.

server3 `/data`: 160760602624 available bytes; 97.78% used; 225807969 free inodes.

server3 `/tmp`: 84482514944 available bytes; 95.29% used; 114158854 free inodes.

server3 `/var/tmp`: 84482514944 available bytes; 95.29% used; 114158854 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105758580736 available bytes; 94.10% used; 114348687 free inodes.

server4 `/home`: 105758580736 available bytes; 94.10% used; 114348687 free inodes.

server4 `/data`: 69175795712 available bytes; 99.04% used; 225257004 free inodes.

server4 `/tmp`: 105758580736 available bytes; 94.10% used; 114348687 free inodes.

server4 `/var/tmp`: 105758580736 available bytes; 94.10% used; 114348687 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
