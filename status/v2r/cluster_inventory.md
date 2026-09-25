# V2R cluster inventory

2026-09-25T22:13:56.352691+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318692306944 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318692306944 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318692306944 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318692306944 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 360276209664 available bytes; 98.35% used; 337539018 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22947708928 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22947708928 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22947708928 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22947708928 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 298911993856 available bytes; 97.93% used; 445053659 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84358062080 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84358062080 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 125875707904 available bytes; 98.26% used; 225806258 free inodes.

server3 `/tmp`: 84358062080 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84358062080 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105312153600 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105312153600 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208635281408 available bytes; 97.12% used; 224919025 free inodes.

server4 `/tmp`: 105312153600 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105312153600 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
