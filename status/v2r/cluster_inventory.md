# V2R cluster inventory

2026-09-25T13:55:33.514001+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319154073600 available bytes; 82.20% used; 112476961 free inodes.

server1 `/home`: 319154073600 available bytes; 82.20% used; 112476961 free inodes.

server1 `/tmp`: 319154073600 available bytes; 82.20% used; 112476961 free inodes.

server1 `/var/tmp`: 319154073600 available bytes; 82.20% used; 112476961 free inodes.

server1 `/mnt/raid5`: 364091486208 available bytes; 98.33% used; 337547521 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 4735180800 available bytes; 99.74% used; 110407474 free inodes.

server2 `/home`: 4735180800 available bytes; 99.74% used; 110407474 free inodes.

server2 `/tmp`: 4735180800 available bytes; 99.74% used; 110407474 free inodes.

server2 `/var/tmp`: 4735180800 available bytes; 99.74% used; 110407474 free inodes.

server2 `/mnt/raid5`: 322449158144 available bytes; 97.77% used; 445076426 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84280557568 available bytes; 95.30% used; 114154464 free inodes.

server3 `/home`: 84280557568 available bytes; 95.30% used; 114154464 free inodes.

server3 `/data`: 142290018304 available bytes; 98.03% used; 225809291 free inodes.

server3 `/tmp`: 84280557568 available bytes; 95.30% used; 114154464 free inodes.

server3 `/var/tmp`: 84280557568 available bytes; 95.30% used; 114154464 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655197696 available bytes; 94.10% used; 114349712 free inodes.

server4 `/home`: 105655197696 available bytes; 94.10% used; 114349712 free inodes.

server4 `/data`: 231433916416 available bytes; 96.80% used; 224949347 free inodes.

server4 `/tmp`: 105655197696 available bytes; 94.10% used; 114349712 free inodes.

server4 `/var/tmp`: 105655197696 available bytes; 94.10% used; 114349712 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
