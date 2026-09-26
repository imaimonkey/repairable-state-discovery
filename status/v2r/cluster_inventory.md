# V2R cluster inventory

2026-09-26T12:57:34.183433+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318154530816 available bytes; 82.25% used; 112474486 free inodes.

server1 `/home`: 318154530816 available bytes; 82.25% used; 112474486 free inodes.

server1 `/tmp`: 318154530816 available bytes; 82.25% used; 112474486 free inodes.

server1 `/var/tmp`: 318154530816 available bytes; 82.25% used; 112474486 free inodes.

server1 `/mnt/raid5`: 678994501632 available bytes; 96.89% used; 337537659 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 19336187904 available bytes; 98.92% used; 110381040 free inodes.

server2 `/home`: 19336187904 available bytes; 98.92% used; 110381040 free inodes.

server2 `/tmp`: 19336187904 available bytes; 98.92% used; 110381040 free inodes.

server2 `/var/tmp`: 19336187904 available bytes; 98.92% used; 110381040 free inodes.

server2 `/mnt/raid5`: 637201858560 available bytes; 95.60% used; 444977212 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82650976256 available bytes; 95.39% used; 114110813 free inodes.

server3 `/home`: 82650976256 available bytes; 95.39% used; 114110813 free inodes.

server3 `/data`: 1347687505920 available bytes; 81.37% used; 225823379 free inodes.

server3 `/tmp`: 82650976256 available bytes; 95.39% used; 114110813 free inodes.

server3 `/var/tmp`: 82650976256 available bytes; 95.39% used; 114110813 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899147264 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105899147264 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 413517795328 available bytes; 94.29% used; 224847009 free inodes.

server4 `/tmp`: 105899147264 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105899147264 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
