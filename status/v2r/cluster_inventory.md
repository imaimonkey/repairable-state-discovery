# V2R cluster inventory

2026-09-24T12:08:19.863263+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324267909120 available bytes; 81.91% used; 112488313 free inodes.

server1 `/home`: 324267909120 available bytes; 81.91% used; 112488313 free inodes.

server1 `/tmp`: 324267909120 available bytes; 81.91% used; 112488313 free inodes.

server1 `/var/tmp`: 324267909120 available bytes; 81.91% used; 112488313 free inodes.

server1 `/mnt/raid5`: 405252042752 available bytes; 98.14% used; 337684945 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57623875584 available bytes; 96.79% used; 110429618 free inodes.

server2 `/home`: 57623875584 available bytes; 96.79% used; 110429618 free inodes.

server2 `/tmp`: 57623875584 available bytes; 96.79% used; 110429618 free inodes.

server2 `/var/tmp`: 57623875584 available bytes; 96.79% used; 110429618 free inodes.

server2 `/mnt/raid5`: 509169938432 available bytes; 96.48% used; 445172453 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85324636160 available bytes; 95.24% used; 114172950 free inodes.

server3 `/home`: 85324636160 available bytes; 95.24% used; 114172950 free inodes.

server3 `/data`: 163532038144 available bytes; 97.74% used; 225815523 free inodes.

server3 `/tmp`: 85324636160 available bytes; 95.24% used; 114172950 free inodes.

server3 `/var/tmp`: 85324636160 available bytes; 95.24% used; 114172950 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105781534720 available bytes; 94.10% used; 114348816 free inodes.

server4 `/home`: 105781534720 available bytes; 94.10% used; 114348816 free inodes.

server4 `/data`: 90432278528 available bytes; 98.75% used; 225257320 free inodes.

server4 `/tmp`: 105781534720 available bytes; 94.10% used; 114348816 free inodes.

server4 `/var/tmp`: 105781534720 available bytes; 94.10% used; 114348816 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
