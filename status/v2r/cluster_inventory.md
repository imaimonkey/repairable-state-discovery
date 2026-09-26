# V2R cluster inventory

2026-09-26T02:47:06.090259+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318418354176 available bytes; 82.24% used; 112476261 free inodes.

server1 `/home`: 318418354176 available bytes; 82.24% used; 112476261 free inodes.

server1 `/tmp`: 318418354176 available bytes; 82.24% used; 112476261 free inodes.

server1 `/var/tmp`: 318418354176 available bytes; 82.24% used; 112476261 free inodes.

server1 `/mnt/raid5`: 331118678016 available bytes; 98.48% used; 337546034 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22936162304 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22936162304 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22936162304 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22936162304 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 288486817792 available bytes; 98.01% used; 445053835 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84319784960 available bytes; 95.29% used; 114152370 free inodes.

server3 `/home`: 84319784960 available bytes; 95.29% used; 114152370 free inodes.

server3 `/data`: 124784881664 available bytes; 98.28% used; 225816703 free inodes.

server3 `/tmp`: 84319784960 available bytes; 95.29% used; 114152370 free inodes.

server3 `/var/tmp`: 84319784960 available bytes; 95.29% used; 114152370 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105919266816 available bytes; 94.09% used; 114347153 free inodes.

server4 `/home`: 105919266816 available bytes; 94.09% used; 114347153 free inodes.

server4 `/data`: 109770403840 available bytes; 98.48% used; 224915405 free inodes.

server4 `/tmp`: 105919266816 available bytes; 94.09% used; 114347153 free inodes.

server4 `/var/tmp`: 105919266816 available bytes; 94.09% used; 114347153 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
