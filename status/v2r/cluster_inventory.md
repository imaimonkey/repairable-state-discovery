# V2R cluster inventory

2026-09-26T09:06:53.331585+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318736302080 available bytes; 82.22% used; 112475795 free inodes.

server1 `/home`: 318736302080 available bytes; 82.22% used; 112475795 free inodes.

server1 `/tmp`: 318736302080 available bytes; 82.22% used; 112475795 free inodes.

server1 `/var/tmp`: 318736302080 available bytes; 82.22% used; 112475795 free inodes.

server1 `/mnt/raid5`: 219022790656 available bytes; 99.00% used; 337538768 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22318579712 available bytes; 98.75% used; 110403911 free inodes.

server2 `/home`: 22318579712 available bytes; 98.75% used; 110403911 free inodes.

server2 `/tmp`: 22318579712 available bytes; 98.75% used; 110403911 free inodes.

server2 `/var/tmp`: 22318579712 available bytes; 98.75% used; 110403911 free inodes.

server2 `/mnt/raid5`: 254348869632 available bytes; 98.24% used; 445023676 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82659917824 available bytes; 95.39% used; 114110812 free inodes.

server3 `/home`: 82659917824 available bytes; 95.39% used; 114110812 free inodes.

server3 `/data`: 123660890112 available bytes; 98.29% used; 225828146 free inodes.

server3 `/tmp`: 82659917824 available bytes; 95.39% used; 114110812 free inodes.

server3 `/var/tmp`: 82659917824 available bytes; 95.39% used; 114110812 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106046222336 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106046222336 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89332875264 available bytes; 98.77% used; 224883327 free inodes.

server4 `/tmp`: 106046222336 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106046222336 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
