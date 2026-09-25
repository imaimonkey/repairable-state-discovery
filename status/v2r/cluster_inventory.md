# V2R cluster inventory

2026-09-25T02:21:12.577565+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318971203584 available bytes; 82.21% used; 112480502 free inodes.

server1 `/home`: 318971203584 available bytes; 82.21% used; 112480502 free inodes.

server1 `/tmp`: 318971203584 available bytes; 82.21% used; 112480502 free inodes.

server1 `/var/tmp`: 318971203584 available bytes; 82.21% used; 112480502 free inodes.

server1 `/mnt/raid5`: 416229593088 available bytes; 98.09% used; 337606968 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23016992768 available bytes; 98.72% used; 110410439 free inodes.

server2 `/home`: 23016992768 available bytes; 98.72% used; 110410439 free inodes.

server2 `/tmp`: 23016992768 available bytes; 98.72% used; 110410439 free inodes.

server2 `/var/tmp`: 23016992768 available bytes; 98.72% used; 110410439 free inodes.

server2 `/mnt/raid5`: 483698745344 available bytes; 96.66% used; 445114275 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351258624 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84351258624 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145748033536 available bytes; 97.99% used; 225811230 free inodes.

server3 `/tmp`: 84351258624 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84351258624 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105896198144 available bytes; 94.09% used; 114351001 free inodes.

server4 `/home`: 105896198144 available bytes; 94.09% used; 114351001 free inodes.

server4 `/data`: 38122160128 available bytes; 99.47% used; 224970328 free inodes.

server4 `/tmp`: 105896198144 available bytes; 94.09% used; 114351001 free inodes.

server4 `/var/tmp`: 105896198144 available bytes; 94.09% used; 114351001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
