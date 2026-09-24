# V2R cluster inventory

2026-09-24T22:57:46.255952+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 322595049472 available bytes; 82.00% used; 112481029 free inodes.

server1 `/home`: 322595049472 available bytes; 82.00% used; 112481029 free inodes.

server1 `/tmp`: 322595049472 available bytes; 82.00% used; 112481029 free inodes.

server1 `/var/tmp`: 322595049472 available bytes; 82.00% used; 112481029 free inodes.

server1 `/mnt/raid5`: 415298588672 available bytes; 98.09% used; 337617058 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23130701824 available bytes; 98.71% used; 110410881 free inodes.

server2 `/home`: 23130701824 available bytes; 98.71% used; 110410881 free inodes.

server2 `/tmp`: 23130701824 available bytes; 98.71% used; 110410881 free inodes.

server2 `/var/tmp`: 23130701824 available bytes; 98.71% used; 110410881 free inodes.

server2 `/mnt/raid5`: 487695962112 available bytes; 96.63% used; 445152433 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84370857984 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84370857984 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 148818907136 available bytes; 97.94% used; 225801559 free inodes.

server3 `/tmp`: 84370857984 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84370857984 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800941568 available bytes; 94.10% used; 114348317 free inodes.

server4 `/home`: 105800941568 available bytes; 94.10% used; 114348317 free inodes.

server4 `/data`: 62506381312 available bytes; 99.14% used; 225195178 free inodes.

server4 `/tmp`: 105800941568 available bytes; 94.10% used; 114348317 free inodes.

server4 `/var/tmp`: 105800941568 available bytes; 94.10% used; 114348317 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
