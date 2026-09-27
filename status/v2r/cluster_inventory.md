# V2R cluster inventory

2026-09-27T01:09:29.213792+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315136446464 available bytes; 82.42% used; 112443430 free inodes.

server1 `/home`: 315136446464 available bytes; 82.42% used; 112443430 free inodes.

server1 `/tmp`: 315136446464 available bytes; 82.42% used; 112443430 free inodes.

server1 `/var/tmp`: 315136446464 available bytes; 82.42% used; 112443430 free inodes.

server1 `/mnt/raid5`: 637548703744 available bytes; 97.08% used; 337405539 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17628966912 available bytes; 99.02% used; 110364994 free inodes.

server2 `/home`: 17628966912 available bytes; 99.02% used; 110364994 free inodes.

server2 `/tmp`: 17628966912 available bytes; 99.02% used; 110364994 free inodes.

server2 `/var/tmp`: 17628966912 available bytes; 99.02% used; 110364994 free inodes.

server2 `/mnt/raid5`: 583840731136 available bytes; 95.97% used; 444887084 free inodes.
| server3 | True | ['0', '3'] | [] |

server3 `/`: 79497539584 available bytes; 95.56% used; 114068698 free inodes.

server3 `/home`: 79497539584 available bytes; 95.56% used; 114068698 free inodes.

server3 `/data`: 1342458290176 available bytes; 81.45% used; 225763860 free inodes.

server3 `/tmp`: 79497539584 available bytes; 95.56% used; 114068698 free inodes.

server3 `/var/tmp`: 79497539584 available bytes; 95.56% used; 114068698 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105878331392 available bytes; 94.09% used; 114347835 free inodes.

server4 `/home`: 105878331392 available bytes; 94.09% used; 114347835 free inodes.

server4 `/data`: 406580809728 available bytes; 94.38% used; 224782911 free inodes.

server4 `/tmp`: 105878331392 available bytes; 94.09% used; 114347835 free inodes.

server4 `/var/tmp`: 105878331392 available bytes; 94.09% used; 114347835 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
