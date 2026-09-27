# V2R cluster inventory

2026-09-27T10:39:45.275175+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314439319552 available bytes; 82.46% used; 112440656 free inodes.

server1 `/home`: 314439319552 available bytes; 82.46% used; 112440656 free inodes.

server1 `/tmp`: 314439319552 available bytes; 82.46% used; 112440656 free inodes.

server1 `/var/tmp`: 314439319552 available bytes; 82.46% used; 112440656 free inodes.

server1 `/mnt/raid5`: 635415457792 available bytes; 97.09% used; 337424414 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 16497168384 available bytes; 99.08% used; 110355926 free inodes.

server2 `/home`: 16497168384 available bytes; 99.08% used; 110355926 free inodes.

server2 `/tmp`: 16497168384 available bytes; 99.08% used; 110355926 free inodes.

server2 `/var/tmp`: 16497168384 available bytes; 99.08% used; 110355926 free inodes.

server2 `/mnt/raid5`: 571505340416 available bytes; 96.05% used; 444738707 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78543970304 available bytes; 95.62% used; 114062824 free inodes.

server3 `/home`: 78543970304 available bytes; 95.62% used; 114062824 free inodes.

server3 `/data`: 1332196995072 available bytes; 81.59% used; 225760813 free inodes.

server3 `/tmp`: 78543970304 available bytes; 95.62% used; 114062824 free inodes.

server3 `/var/tmp`: 78543970304 available bytes; 95.62% used; 114062824 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111031668736 available bytes; 93.80% used; 114372825 free inodes.

server4 `/home`: 111031668736 available bytes; 93.80% used; 114372825 free inodes.

server4 `/data`: 363358466048 available bytes; 94.98% used; 224766864 free inodes.

server4 `/tmp`: 111031668736 available bytes; 93.80% used; 114372825 free inodes.

server4 `/var/tmp`: 111031668736 available bytes; 93.80% used; 114372825 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
