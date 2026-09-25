# V2R cluster inventory

2026-09-25T02:31:57.025426+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318969581568 available bytes; 82.21% used; 112480497 free inodes.

server1 `/home`: 318969581568 available bytes; 82.21% used; 112480497 free inodes.

server1 `/tmp`: 318969581568 available bytes; 82.21% used; 112480497 free inodes.

server1 `/var/tmp`: 318969581568 available bytes; 82.21% used; 112480497 free inodes.

server1 `/mnt/raid5`: 416211251200 available bytes; 98.09% used; 337605727 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23008890880 available bytes; 98.72% used; 110410431 free inodes.

server2 `/home`: 23008890880 available bytes; 98.72% used; 110410431 free inodes.

server2 `/tmp`: 23008890880 available bytes; 98.72% used; 110410431 free inodes.

server2 `/var/tmp`: 23008890880 available bytes; 98.72% used; 110410431 free inodes.

server2 `/mnt/raid5`: 483051220992 available bytes; 96.66% used; 445113666 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350992384 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84350992384 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145565515776 available bytes; 97.99% used; 225811012 free inodes.

server3 `/tmp`: 84350992384 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84350992384 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105895739392 available bytes; 94.09% used; 114350966 free inodes.

server4 `/home`: 105895739392 available bytes; 94.09% used; 114350966 free inodes.

server4 `/data`: 17264050176 available bytes; 99.76% used; 224969070 free inodes.

server4 `/tmp`: 105895739392 available bytes; 94.09% used; 114350966 free inodes.

server4 `/var/tmp`: 105895739392 available bytes; 94.09% used; 114350966 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
