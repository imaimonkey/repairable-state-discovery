# V2R cluster inventory

2026-09-25T02:19:40.633981+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318969921536 available bytes; 82.21% used; 112480554 free inodes.

server1 `/home`: 318969921536 available bytes; 82.21% used; 112480554 free inodes.

server1 `/tmp`: 318969921536 available bytes; 82.21% used; 112480554 free inodes.

server1 `/var/tmp`: 318969921536 available bytes; 82.21% used; 112480554 free inodes.

server1 `/mnt/raid5`: 416234192896 available bytes; 98.09% used; 337607156 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23015636992 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 23015636992 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 23015636992 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 23015636992 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 483726094336 available bytes; 96.66% used; 445113919 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351344640 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84351344640 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 125124161536 available bytes; 98.27% used; 225811260 free inodes.

server3 `/tmp`: 84351344640 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84351344640 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105896251392 available bytes; 94.09% used; 114351001 free inodes.

server4 `/home`: 105896251392 available bytes; 94.09% used; 114351001 free inodes.

server4 `/data`: 38511415296 available bytes; 99.47% used; 224970341 free inodes.

server4 `/tmp`: 105896251392 available bytes; 94.09% used; 114351001 free inodes.

server4 `/var/tmp`: 105896251392 available bytes; 94.09% used; 114351001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
