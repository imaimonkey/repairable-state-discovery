# V2R cluster inventory

2026-09-26T23:45:38.037400+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315449581568 available bytes; 82.40% used; 112445711 free inodes.

server1 `/home`: 315449581568 available bytes; 82.40% used; 112445711 free inodes.

server1 `/tmp`: 315449581568 available bytes; 82.40% used; 112445711 free inodes.

server1 `/var/tmp`: 315449581568 available bytes; 82.40% used; 112445711 free inodes.

server1 `/mnt/raid5`: 637717999616 available bytes; 97.07% used; 337408415 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 17947381760 available bytes; 99.00% used; 110367468 free inodes.

server2 `/home`: 17947381760 available bytes; 99.00% used; 110367468 free inodes.

server2 `/tmp`: 17947381760 available bytes; 99.00% used; 110367468 free inodes.

server2 `/var/tmp`: 17947381760 available bytes; 99.00% used; 110367468 free inodes.

server2 `/mnt/raid5`: 594638217216 available bytes; 95.89% used; 444959372 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 81081851904 available bytes; 95.48% used; 114069879 free inodes.

server3 `/home`: 81081851904 available bytes; 95.48% used; 114069879 free inodes.

server3 `/data`: 1349226418176 available bytes; 81.35% used; 225826220 free inodes.

server3 `/tmp`: 81081851904 available bytes; 95.48% used; 114069879 free inodes.

server3 `/var/tmp`: 81081851904 available bytes; 95.48% used; 114069879 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105880530944 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105880530944 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409588322304 available bytes; 94.34% used; 224823790 free inodes.

server4 `/tmp`: 105880530944 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105880530944 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
