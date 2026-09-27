# V2R cluster inventory

2026-09-27T00:15:25.247933+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315170271232 available bytes; 82.42% used; 112443637 free inodes.

server1 `/home`: 315170271232 available bytes; 82.42% used; 112443637 free inodes.

server1 `/tmp`: 315170271232 available bytes; 82.42% used; 112443637 free inodes.

server1 `/var/tmp`: 315170271232 available bytes; 82.42% used; 112443637 free inodes.

server1 `/mnt/raid5`: 637715939328 available bytes; 97.07% used; 337408072 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 17932144640 available bytes; 99.00% used; 110367287 free inodes.

server2 `/home`: 17932144640 available bytes; 99.00% used; 110367287 free inodes.

server2 `/tmp`: 17932144640 available bytes; 99.00% used; 110367287 free inodes.

server2 `/var/tmp`: 17932144640 available bytes; 99.00% used; 110367287 free inodes.

server2 `/mnt/raid5`: 593635463168 available bytes; 95.90% used; 444957814 free inodes.
| server3 | True | ['2', '3'] | [] | reference_compatible=True |

server3 `/`: 79508975616 available bytes; 95.56% used; 114068847 free inodes.

server3 `/home`: 79508975616 available bytes; 95.56% used; 114068847 free inodes.

server3 `/data`: 1349113020416 available bytes; 81.35% used; 225825843 free inodes.

server3 `/tmp`: 79508975616 available bytes; 95.56% used; 114068847 free inodes.

server3 `/var/tmp`: 79508975616 available bytes; 95.56% used; 114068847 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105879752704 available bytes; 94.09% used; 114347850 free inodes.

server4 `/home`: 105879752704 available bytes; 94.09% used; 114347850 free inodes.

server4 `/data`: 409567662080 available bytes; 94.34% used; 224823687 free inodes.

server4 `/tmp`: 105879752704 available bytes; 94.09% used; 114347850 free inodes.

server4 `/var/tmp`: 105879752704 available bytes; 94.09% used; 114347850 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
