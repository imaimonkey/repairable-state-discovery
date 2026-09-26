# V2R cluster inventory

2026-09-26T01:46:02.305561+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318647967744 available bytes; 82.22% used; 112476293 free inodes.

server1 `/home`: 318647967744 available bytes; 82.22% used; 112476293 free inodes.

server1 `/tmp`: 318647967744 available bytes; 82.22% used; 112476293 free inodes.

server1 `/var/tmp`: 318647967744 available bytes; 82.22% used; 112476293 free inodes.

server1 `/mnt/raid5`: 345466363904 available bytes; 98.42% used; 337546417 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22938624000 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22938624000 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22938624000 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22938624000 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 290249707520 available bytes; 97.99% used; 445055281 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84326293504 available bytes; 95.29% used; 114152364 free inodes.

server3 `/home`: 84326293504 available bytes; 95.29% used; 114152364 free inodes.

server3 `/data`: 124796301312 available bytes; 98.28% used; 225817744 free inodes.

server3 `/tmp`: 84326293504 available bytes; 95.29% used; 114152364 free inodes.

server3 `/var/tmp`: 84326293504 available bytes; 95.29% used; 114152364 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105196511232 available bytes; 94.13% used; 114346905 free inodes.

server4 `/home`: 105196511232 available bytes; 94.13% used; 114346905 free inodes.

server4 `/data`: 131384049664 available bytes; 98.18% used; 224915851 free inodes.

server4 `/tmp`: 105196511232 available bytes; 94.13% used; 114346905 free inodes.

server4 `/var/tmp`: 105196511232 available bytes; 94.13% used; 114346905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
