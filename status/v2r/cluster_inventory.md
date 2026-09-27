# V2R cluster inventory

2026-09-27T01:35:24.182155+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315144830976 available bytes; 82.42% used; 112443369 free inodes.

server1 `/home`: 315144830976 available bytes; 82.42% used; 112443369 free inodes.

server1 `/tmp`: 315144830976 available bytes; 82.42% used; 112443369 free inodes.

server1 `/var/tmp`: 315144830976 available bytes; 82.42% used; 112443369 free inodes.

server1 `/mnt/raid5`: 637514498048 available bytes; 97.08% used; 337405520 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17628778496 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17628778496 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17628778496 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17628778496 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 582529122304 available bytes; 95.97% used; 444886237 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 79395438592 available bytes; 95.57% used; 114067717 free inodes.

server3 `/home`: 79395438592 available bytes; 95.57% used; 114067717 free inodes.

server3 `/data`: 1342366244864 available bytes; 81.45% used; 225763305 free inodes.

server3 `/tmp`: 79395438592 available bytes; 95.57% used; 114067717 free inodes.

server3 `/var/tmp`: 79395438592 available bytes; 95.57% used; 114067717 free inodes.
| server4 | True | ['0', '1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105869336576 available bytes; 94.09% used; 114347851 free inodes.

server4 `/home`: 105869336576 available bytes; 94.09% used; 114347851 free inodes.

server4 `/data`: 406536638464 available bytes; 94.38% used; 224782881 free inodes.

server4 `/tmp`: 105869336576 available bytes; 94.09% used; 114347851 free inodes.

server4 `/var/tmp`: 105869336576 available bytes; 94.09% used; 114347851 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
