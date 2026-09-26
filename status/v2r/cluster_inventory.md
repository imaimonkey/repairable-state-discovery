# V2R cluster inventory

2026-09-26T07:54:00.344271+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318754582528 available bytes; 82.22% used; 112476268 free inodes.

server1 `/home`: 318754582528 available bytes; 82.22% used; 112476268 free inodes.

server1 `/tmp`: 318754582528 available bytes; 82.22% used; 112476268 free inodes.

server1 `/var/tmp`: 318754582528 available bytes; 82.22% used; 112476268 free inodes.

server1 `/mnt/raid5`: 219187175424 available bytes; 98.99% used; 337539128 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22318923776 available bytes; 98.75% used; 110403903 free inodes.

server2 `/home`: 22318923776 available bytes; 98.75% used; 110403903 free inodes.

server2 `/tmp`: 22318923776 available bytes; 98.75% used; 110403903 free inodes.

server2 `/var/tmp`: 22318923776 available bytes; 98.75% used; 110403903 free inodes.

server2 `/mnt/raid5`: 258527305728 available bytes; 98.21% used; 445026128 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82679812096 available bytes; 95.39% used; 114110854 free inodes.

server3 `/home`: 82679812096 available bytes; 95.39% used; 114110854 free inodes.

server3 `/data`: 123901210624 available bytes; 98.29% used; 225820639 free inodes.

server3 `/tmp`: 82679812096 available bytes; 95.39% used; 114110854 free inodes.

server3 `/var/tmp`: 82679812096 available bytes; 95.39% used; 114110854 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106073726976 available bytes; 94.08% used; 114348160 free inodes.

server4 `/home`: 106073726976 available bytes; 94.08% used; 114348160 free inodes.

server4 `/data`: 105655685120 available bytes; 98.54% used; 224922432 free inodes.

server4 `/tmp`: 106073726976 available bytes; 94.08% used; 114348160 free inodes.

server4 `/var/tmp`: 106073726976 available bytes; 94.08% used; 114348160 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
