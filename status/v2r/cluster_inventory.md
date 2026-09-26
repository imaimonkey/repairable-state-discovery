# V2R cluster inventory

2026-09-26T23:59:21.314284+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315442769920 available bytes; 82.40% used; 112445729 free inodes.

server1 `/home`: 315442769920 available bytes; 82.40% used; 112445729 free inodes.

server1 `/tmp`: 315442769920 available bytes; 82.40% used; 112445729 free inodes.

server1 `/var/tmp`: 315442769920 available bytes; 82.40% used; 112445729 free inodes.

server1 `/mnt/raid5`: 637715718144 available bytes; 97.07% used; 337408339 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 17945468928 available bytes; 99.00% used; 110367450 free inodes.

server2 `/home`: 17945468928 available bytes; 99.00% used; 110367450 free inodes.

server2 `/tmp`: 17945468928 available bytes; 99.00% used; 110367450 free inodes.

server2 `/var/tmp`: 17945468928 available bytes; 99.00% used; 110367450 free inodes.

server2 `/mnt/raid5`: 594256416768 available bytes; 95.89% used; 444958847 free inodes.
| server3 | True | ['2', '3'] | [] |

server3 `/`: 81080885248 available bytes; 95.48% used; 114069890 free inodes.

server3 `/home`: 81080885248 available bytes; 95.48% used; 114069890 free inodes.

server3 `/data`: 1349115777024 available bytes; 81.35% used; 225826077 free inodes.

server3 `/tmp`: 81080885248 available bytes; 95.48% used; 114069890 free inodes.

server3 `/var/tmp`: 81080885248 available bytes; 95.48% used; 114069890 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105880166400 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105880166400 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409582813184 available bytes; 94.34% used; 224823790 free inodes.

server4 `/tmp`: 105880166400 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105880166400 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
