# V2R cluster inventory

2026-09-26T20:43:44.414967+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315483680768 available bytes; 82.40% used; 112444691 free inodes.

server1 `/home`: 315483680768 available bytes; 82.40% used; 112444691 free inodes.

server1 `/tmp`: 315483680768 available bytes; 82.40% used; 112444691 free inodes.

server1 `/var/tmp`: 315483680768 available bytes; 82.40% used; 112444691 free inodes.

server1 `/mnt/raid5`: 645854613504 available bytes; 97.04% used; 337467121 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17973538816 available bytes; 99.00% used; 110367099 free inodes.

server2 `/home`: 17973538816 available bytes; 99.00% used; 110367099 free inodes.

server2 `/tmp`: 17973538816 available bytes; 99.00% used; 110367099 free inodes.

server2 `/var/tmp`: 17973538816 available bytes; 99.00% used; 110367099 free inodes.

server2 `/mnt/raid5`: 600294825984 available bytes; 95.85% used; 444964156 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81262878720 available bytes; 95.47% used; 114065287 free inodes.

server3 `/home`: 81262878720 available bytes; 95.47% used; 114065287 free inodes.

server3 `/data`: 1348603752448 available bytes; 81.36% used; 225831396 free inodes.

server3 `/tmp`: 81262878720 available bytes; 95.47% used; 114065287 free inodes.

server3 `/var/tmp`: 81262878720 available bytes; 95.47% used; 114065287 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105918722048 available bytes; 94.09% used; 114347838 free inodes.

server4 `/home`: 105918722048 available bytes; 94.09% used; 114347838 free inodes.

server4 `/data`: 410081042432 available bytes; 94.33% used; 224823711 free inodes.

server4 `/tmp`: 105918722048 available bytes; 94.09% used; 114347838 free inodes.

server4 `/var/tmp`: 105918722048 available bytes; 94.09% used; 114347838 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
