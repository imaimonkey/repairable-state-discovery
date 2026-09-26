# V2R cluster inventory

2026-09-26T23:43:26.610282+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315459461120 available bytes; 82.40% used; 112445680 free inodes.

server1 `/home`: 315459461120 available bytes; 82.40% used; 112445680 free inodes.

server1 `/tmp`: 315459461120 available bytes; 82.40% used; 112445680 free inodes.

server1 `/var/tmp`: 315459461120 available bytes; 82.40% used; 112445680 free inodes.

server1 `/mnt/raid5`: 637718536192 available bytes; 97.07% used; 337408423 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17938075648 available bytes; 99.00% used; 110367460 free inodes.

server2 `/home`: 17938075648 available bytes; 99.00% used; 110367460 free inodes.

server2 `/tmp`: 17938075648 available bytes; 99.00% used; 110367460 free inodes.

server2 `/var/tmp`: 17938075648 available bytes; 99.00% used; 110367460 free inodes.

server2 `/mnt/raid5`: 594703122432 available bytes; 95.89% used; 444959460 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 81082286080 available bytes; 95.48% used; 114069879 free inodes.

server3 `/home`: 81082286080 available bytes; 95.48% used; 114069879 free inodes.

server3 `/data`: 1349227012096 available bytes; 81.35% used; 225826263 free inodes.

server3 `/tmp`: 81082286080 available bytes; 95.48% used; 114069879 free inodes.

server3 `/var/tmp`: 81082286080 available bytes; 95.48% used; 114069879 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105880588288 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105880588288 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409589604352 available bytes; 94.34% used; 224823790 free inodes.

server4 `/tmp`: 105880588288 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105880588288 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
