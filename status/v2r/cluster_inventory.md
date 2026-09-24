# V2R cluster inventory

2026-09-24T12:08:10.663048+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324267909120 available bytes; 81.91% used; 112488313 free inodes.

server1 `/home`: 324267909120 available bytes; 81.91% used; 112488313 free inodes.

server1 `/tmp`: 324267909120 available bytes; 81.91% used; 112488313 free inodes.

server1 `/var/tmp`: 324267909120 available bytes; 81.91% used; 112488313 free inodes.

server1 `/mnt/raid5`: 405252337664 available bytes; 98.14% used; 337684961 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57624035328 available bytes; 96.79% used; 110429618 free inodes.

server2 `/home`: 57624035328 available bytes; 96.79% used; 110429618 free inodes.

server2 `/tmp`: 57624035328 available bytes; 96.79% used; 110429618 free inodes.

server2 `/var/tmp`: 57624035328 available bytes; 96.79% used; 110429618 free inodes.

server2 `/mnt/raid5`: 509177245696 available bytes; 96.48% used; 445172461 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85324718080 available bytes; 95.24% used; 114172950 free inodes.

server3 `/home`: 85324718080 available bytes; 95.24% used; 114172950 free inodes.

server3 `/data`: 163532279808 available bytes; 97.74% used; 225815541 free inodes.

server3 `/tmp`: 85324718080 available bytes; 95.24% used; 114172950 free inodes.

server3 `/var/tmp`: 85324718080 available bytes; 95.24% used; 114172950 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105781534720 available bytes; 94.10% used; 114348816 free inodes.

server4 `/home`: 105781534720 available bytes; 94.10% used; 114348816 free inodes.

server4 `/data`: 90432282624 available bytes; 98.75% used; 225257320 free inodes.

server4 `/tmp`: 105781534720 available bytes; 94.10% used; 114348816 free inodes.

server4 `/var/tmp`: 105781534720 available bytes; 94.10% used; 114348816 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
