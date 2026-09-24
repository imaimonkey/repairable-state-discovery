# V2R cluster inventory

2026-09-24T21:23:45.262671+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323952771072 available bytes; 81.93% used; 112481414 free inodes.

server1 `/home`: 323952771072 available bytes; 81.93% used; 112481414 free inodes.

server1 `/tmp`: 323952771072 available bytes; 81.93% used; 112481414 free inodes.

server1 `/var/tmp`: 323952771072 available bytes; 81.93% used; 112481414 free inodes.

server1 `/mnt/raid5`: 415514877952 available bytes; 98.09% used; 337628209 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30136098816 available bytes; 98.32% used; 110411344 free inodes.

server2 `/home`: 30136098816 available bytes; 98.32% used; 110411344 free inodes.

server2 `/tmp`: 30136098816 available bytes; 98.32% used; 110411344 free inodes.

server2 `/var/tmp`: 30136098816 available bytes; 98.32% used; 110411344 free inodes.

server2 `/mnt/raid5`: 490608594944 available bytes; 96.61% used; 445155181 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382474240 available bytes; 95.29% used; 114156099 free inodes.

server3 `/home`: 84382474240 available bytes; 95.29% used; 114156099 free inodes.

server3 `/data`: 150412115968 available bytes; 97.92% used; 225803301 free inodes.

server3 `/tmp`: 84382474240 available bytes; 95.29% used; 114156099 free inodes.

server3 `/var/tmp`: 84382474240 available bytes; 95.29% used; 114156099 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632268288 available bytes; 94.11% used; 114348353 free inodes.

server4 `/home`: 105632268288 available bytes; 94.11% used; 114348353 free inodes.

server4 `/data`: 84678602752 available bytes; 98.83% used; 225253239 free inodes.

server4 `/tmp`: 105632268288 available bytes; 94.11% used; 114348353 free inodes.

server4 `/var/tmp`: 105632268288 available bytes; 94.11% used; 114348353 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
