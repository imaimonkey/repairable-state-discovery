# V2R cluster inventory

2026-09-27T15:06:56.340272+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304748986368 available bytes; 83.00% used; 112401393 free inodes.

server1 `/home`: 304748986368 available bytes; 83.00% used; 112401393 free inodes.

server1 `/tmp`: 304748986368 available bytes; 83.00% used; 112401393 free inodes.

server1 `/var/tmp`: 304748986368 available bytes; 83.00% used; 112401393 free inodes.

server1 `/mnt/raid5`: 630113976320 available bytes; 97.11% used; 337424040 free inodes.
| server2 | True | ['2', '3', '4', '5', '6', '7'] | [] |

server2 `/`: 13406826496 available bytes; 99.25% used; 110351802 free inodes.

server2 `/home`: 13406826496 available bytes; 99.25% used; 110351802 free inodes.

server2 `/tmp`: 13406826496 available bytes; 99.25% used; 110351802 free inodes.

server2 `/var/tmp`: 13406826496 available bytes; 99.25% used; 110351802 free inodes.

server2 `/mnt/raid5`: 524569718784 available bytes; 96.38% used; 444721185 free inodes.
| server3 | True | ['0', '1', '2'] | [] |

server3 `/`: 78557085696 available bytes; 95.62% used; 114062763 free inodes.

server3 `/home`: 78557085696 available bytes; 95.62% used; 114062763 free inodes.

server3 `/data`: 1326756536320 available bytes; 81.66% used; 225756343 free inodes.

server3 `/tmp`: 78557085696 available bytes; 95.62% used; 114062763 free inodes.

server3 `/var/tmp`: 78557085696 available bytes; 95.62% used; 114062763 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 108944990208 available bytes; 93.92% used; 114372741 free inodes.

server4 `/home`: 108944990208 available bytes; 93.92% used; 114372741 free inodes.

server4 `/data`: 350406086656 available bytes; 95.16% used; 224727205 free inodes.

server4 `/tmp`: 108944990208 available bytes; 93.92% used; 114372741 free inodes.

server4 `/var/tmp`: 108944990208 available bytes; 93.92% used; 114372741 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
