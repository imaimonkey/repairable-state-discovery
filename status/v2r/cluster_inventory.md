# V2R cluster inventory

2026-09-26T21:19:17.390372+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315481374720 available bytes; 82.40% used; 112445681 free inodes.

server1 `/home`: 315481374720 available bytes; 82.40% used; 112445681 free inodes.

server1 `/tmp`: 315481374720 available bytes; 82.40% used; 112445681 free inodes.

server1 `/var/tmp`: 315481374720 available bytes; 82.40% used; 112445681 free inodes.

server1 `/mnt/raid5`: 645854130176 available bytes; 97.04% used; 337467121 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17930883072 available bytes; 99.00% used; 110367525 free inodes.

server2 `/home`: 17930883072 available bytes; 99.00% used; 110367525 free inodes.

server2 `/tmp`: 17930883072 available bytes; 99.00% used; 110367525 free inodes.

server2 `/var/tmp`: 17930883072 available bytes; 99.00% used; 110367525 free inodes.

server2 `/mnt/raid5`: 599010611200 available bytes; 95.86% used; 444963175 free inodes.
| server3 | True | [] | [] |

server3 `/`: 80983429120 available bytes; 95.48% used; 114058021 free inodes.

server3 `/home`: 80983429120 available bytes; 95.48% used; 114058021 free inodes.

server3 `/data`: 1351103811584 available bytes; 81.33% used; 225830772 free inodes.

server3 `/tmp`: 80983429120 available bytes; 95.48% used; 114058021 free inodes.

server3 `/var/tmp`: 80983429120 available bytes; 95.48% used; 114058021 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105909387264 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105909387264 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409908768768 available bytes; 94.33% used; 224823845 free inodes.

server4 `/tmp`: 105909387264 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105909387264 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
