# V2R cluster inventory

2026-09-25T06:27:32.238362+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318880325632 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318880325632 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318880325632 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318880325632 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 400785862656 available bytes; 98.16% used; 337561463 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22895525888 available bytes; 98.72% used; 110410518 free inodes.

server2 `/home`: 22895525888 available bytes; 98.72% used; 110410518 free inodes.

server2 `/tmp`: 22895525888 available bytes; 98.72% used; 110410518 free inodes.

server2 `/var/tmp`: 22895525888 available bytes; 98.72% used; 110410518 free inodes.

server2 `/mnt/raid5`: 370633793536 available bytes; 97.44% used; 445099574 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84317143040 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84317143040 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142531203072 available bytes; 98.03% used; 225813822 free inodes.

server3 `/tmp`: 84317143040 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84317143040 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648304128 available bytes; 94.10% used; 114350390 free inodes.

server4 `/home`: 105648304128 available bytes; 94.10% used; 114350390 free inodes.

server4 `/data`: 254344413184 available bytes; 96.48% used; 225021164 free inodes.

server4 `/tmp`: 105648304128 available bytes; 94.10% used; 114350390 free inodes.

server4 `/var/tmp`: 105648304128 available bytes; 94.10% used; 114350390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
