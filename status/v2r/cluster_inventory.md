# V2R cluster inventory

2026-09-25T02:16:34.374636+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318969597952 available bytes; 82.21% used; 112480559 free inodes.

server1 `/home`: 318969597952 available bytes; 82.21% used; 112480559 free inodes.

server1 `/tmp`: 318969597952 available bytes; 82.21% used; 112480559 free inodes.

server1 `/var/tmp`: 318969597952 available bytes; 82.21% used; 112480559 free inodes.

server1 `/mnt/raid5`: 416239988736 available bytes; 98.09% used; 337607512 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23017517056 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 23017517056 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 23017517056 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 23017517056 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 483813695488 available bytes; 96.66% used; 445114048 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350480384 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84350480384 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 145816006656 available bytes; 97.98% used; 225811370 free inodes.

server3 `/tmp`: 84350480384 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84350480384 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105752289280 available bytes; 94.10% used; 114348239 free inodes.

server4 `/home`: 105752289280 available bytes; 94.10% used; 114348239 free inodes.

server4 `/data`: 37548113920 available bytes; 99.48% used; 224974386 free inodes.

server4 `/tmp`: 105752289280 available bytes; 94.10% used; 114348239 free inodes.

server4 `/var/tmp`: 105752289280 available bytes; 94.10% used; 114348239 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
