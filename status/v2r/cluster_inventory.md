# V2R cluster inventory

2026-09-25T05:07:30.046104+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318899150848 available bytes; 82.21% used; 112480301 free inodes.

server1 `/home`: 318899150848 available bytes; 82.21% used; 112480301 free inodes.

server1 `/tmp`: 318899150848 available bytes; 82.21% used; 112480301 free inodes.

server1 `/var/tmp`: 318899150848 available bytes; 82.21% used; 112480301 free inodes.

server1 `/mnt/raid5`: 408611315712 available bytes; 98.13% used; 337571149 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22930112512 available bytes; 98.72% used; 110410436 free inodes.

server2 `/home`: 22930112512 available bytes; 98.72% used; 110410436 free inodes.

server2 `/tmp`: 22930112512 available bytes; 98.72% used; 110410436 free inodes.

server2 `/var/tmp`: 22930112512 available bytes; 98.72% used; 110410436 free inodes.

server2 `/mnt/raid5`: 461879717888 available bytes; 96.81% used; 445109053 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339748864 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84339748864 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 142825492480 available bytes; 98.03% used; 225815404 free inodes.

server3 `/tmp`: 84339748864 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84339748864 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105659146240 available bytes; 94.10% used; 114350406 free inodes.

server4 `/home`: 105659146240 available bytes; 94.10% used; 114350406 free inodes.

server4 `/data`: 27930640384 available bytes; 99.61% used; 224960803 free inodes.

server4 `/tmp`: 105659146240 available bytes; 94.10% used; 114350406 free inodes.

server4 `/var/tmp`: 105659146240 available bytes; 94.10% used; 114350406 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
