# V2R cluster inventory

2026-09-25T03:08:52.039281+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318940979200 available bytes; 82.21% used; 112480385 free inodes.

server1 `/home`: 318940979200 available bytes; 82.21% used; 112480385 free inodes.

server1 `/tmp`: 318940979200 available bytes; 82.21% used; 112480385 free inodes.

server1 `/var/tmp`: 318940979200 available bytes; 82.21% used; 112480385 free inodes.

server1 `/mnt/raid5`: 416125566976 available bytes; 98.09% used; 337601400 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22991364096 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22991364096 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22991364096 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22991364096 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 465825771520 available bytes; 96.78% used; 445112471 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84345028608 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84345028608 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 144892456960 available bytes; 98.00% used; 225810301 free inodes.

server3 `/tmp`: 84345028608 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84345028608 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105692983296 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692983296 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 50252292096 available bytes; 99.31% used; 224967408 free inodes.

server4 `/tmp`: 105692983296 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692983296 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
