# V2R cluster inventory

2026-09-26T22:31:50.955670+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315471278080 available bytes; 82.40% used; 112445698 free inodes.

server1 `/home`: 315471278080 available bytes; 82.40% used; 112445698 free inodes.

server1 `/tmp`: 315471278080 available bytes; 82.40% used; 112445698 free inodes.

server1 `/var/tmp`: 315471278080 available bytes; 82.40% used; 112445698 free inodes.

server1 `/mnt/raid5`: 645852332032 available bytes; 97.04% used; 337467240 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17941598208 available bytes; 99.00% used; 110367507 free inodes.

server2 `/home`: 17941598208 available bytes; 99.00% used; 110367507 free inodes.

server2 `/tmp`: 17941598208 available bytes; 99.00% used; 110367507 free inodes.

server2 `/var/tmp`: 17941598208 available bytes; 99.00% used; 110367507 free inodes.

server2 `/mnt/raid5`: 597005602816 available bytes; 95.87% used; 444961050 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81082814464 available bytes; 95.48% used; 114069873 free inodes.

server3 `/home`: 81082814464 available bytes; 95.48% used; 114069873 free inodes.

server3 `/data`: 1349249531904 available bytes; 81.35% used; 225827030 free inodes.

server3 `/tmp`: 81082814464 available bytes; 95.48% used; 114069873 free inodes.

server3 `/var/tmp`: 81082814464 available bytes; 95.48% used; 114069873 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899175936 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105899175936 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409636773888 available bytes; 94.34% used; 224823835 free inodes.

server4 `/tmp`: 105899175936 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105899175936 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
