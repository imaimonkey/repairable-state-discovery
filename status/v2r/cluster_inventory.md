# V2R cluster inventory

2026-09-24T23:00:51.813383+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 321178640384 available bytes; 82.08% used; 112480883 free inodes.

server1 `/home`: 321178640384 available bytes; 82.08% used; 112480883 free inodes.

server1 `/tmp`: 321178640384 available bytes; 82.08% used; 112480883 free inodes.

server1 `/var/tmp`: 321178640384 available bytes; 82.08% used; 112480883 free inodes.

server1 `/mnt/raid5`: 415294713856 available bytes; 98.09% used; 337616666 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23132327936 available bytes; 98.71% used; 110410836 free inodes.

server2 `/home`: 23132327936 available bytes; 98.71% used; 110410836 free inodes.

server2 `/tmp`: 23132327936 available bytes; 98.71% used; 110410836 free inodes.

server2 `/var/tmp`: 23132327936 available bytes; 98.71% used; 110410836 free inodes.

server2 `/mnt/raid5`: 487577014272 available bytes; 96.63% used; 445152150 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84369846272 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84369846272 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148774211584 available bytes; 97.94% used; 225801506 free inodes.

server3 `/tmp`: 84369846272 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84369846272 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800826880 available bytes; 94.10% used; 114348316 free inodes.

server4 `/home`: 105800826880 available bytes; 94.10% used; 114348316 free inodes.

server4 `/data`: 62006546432 available bytes; 99.14% used; 225190765 free inodes.

server4 `/tmp`: 105800826880 available bytes; 94.10% used; 114348316 free inodes.

server4 `/var/tmp`: 105800826880 available bytes; 94.10% used; 114348316 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
