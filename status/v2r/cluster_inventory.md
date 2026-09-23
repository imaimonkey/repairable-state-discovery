# V2R cluster inventory

2026-09-23T22:53:40.714086+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325748928512 available bytes; 81.83% used; 112501732 free inodes.

server1 `/home`: 325748928512 available bytes; 81.83% used; 112501732 free inodes.

server1 `/tmp`: 325748928512 available bytes; 81.83% used; 112501732 free inodes.

server1 `/var/tmp`: 325748928512 available bytes; 81.83% used; 112501732 free inodes.

server1 `/mnt/raid5`: 1388094652416 available bytes; 93.63% used; 337739937 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41069641728 available bytes; 97.71% used; 110432618 free inodes.

server2 `/home`: 41069641728 available bytes; 97.71% used; 110432618 free inodes.

server2 `/tmp`: 41069641728 available bytes; 97.71% used; 110432618 free inodes.

server2 `/var/tmp`: 41069641728 available bytes; 97.71% used; 110432618 free inodes.

server2 `/mnt/raid5`: 535976329216 available bytes; 96.30% used; 445206320 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292537946112 available bytes; 83.68% used; 114192880 free inodes.

server3 `/home`: 292537946112 available bytes; 83.68% used; 114192880 free inodes.

server3 `/data`: 82365399040 available bytes; 98.86% used; 225846780 free inodes.

server3 `/tmp`: 292537946112 available bytes; 83.68% used; 114192880 free inodes.

server3 `/var/tmp`: 292537946112 available bytes; 83.68% used; 114192880 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106311581696 available bytes; 94.07% used; 114353683 free inodes.

server4 `/home`: 106311581696 available bytes; 94.07% used; 114353683 free inodes.

server4 `/data`: 300092346368 available bytes; 95.85% used; 225433346 free inodes.

server4 `/tmp`: 106311581696 available bytes; 94.07% used; 114353683 free inodes.

server4 `/var/tmp`: 106311581696 available bytes; 94.07% used; 114353683 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
