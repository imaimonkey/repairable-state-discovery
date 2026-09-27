# V2R cluster inventory

2026-09-27T00:39:47.260992+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315153494016 available bytes; 82.42% used; 112443469 free inodes.

server1 `/home`: 315153494016 available bytes; 82.42% used; 112443469 free inodes.

server1 `/tmp`: 315153494016 available bytes; 82.42% used; 112443469 free inodes.

server1 `/var/tmp`: 315153494016 available bytes; 82.42% used; 112443469 free inodes.

server1 `/mnt/raid5`: 637679370240 available bytes; 97.07% used; 337407668 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17623072768 available bytes; 99.02% used; 110365010 free inodes.

server2 `/home`: 17623072768 available bytes; 99.02% used; 110365010 free inodes.

server2 `/tmp`: 17623072768 available bytes; 99.02% used; 110365010 free inodes.

server2 `/var/tmp`: 17623072768 available bytes; 99.02% used; 110365010 free inodes.

server2 `/mnt/raid5`: 592925097984 available bytes; 95.90% used; 444956732 free inodes.
| server3 | True | ['0', '3'] | [] | reference_compatible=True |

server3 `/`: 79370055680 available bytes; 95.57% used; 114068693 free inodes.

server3 `/home`: 79370055680 available bytes; 95.57% used; 114068693 free inodes.

server3 `/data`: 1348996231168 available bytes; 81.36% used; 225825462 free inodes.

server3 `/tmp`: 79370055680 available bytes; 95.57% used; 114068693 free inodes.

server3 `/var/tmp`: 79370055680 available bytes; 95.57% used; 114068693 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105879089152 available bytes; 94.09% used; 114347836 free inodes.

server4 `/home`: 105879089152 available bytes; 94.09% used; 114347836 free inodes.

server4 `/data`: 409206562816 available bytes; 94.34% used; 224820609 free inodes.

server4 `/tmp`: 105879089152 available bytes; 94.09% used; 114347836 free inodes.

server4 `/var/tmp`: 105879089152 available bytes; 94.09% used; 114347836 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
