# V2R cluster inventory

2026-09-25T02:40:40.036101+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318958944256 available bytes; 82.21% used; 112480424 free inodes.

server1 `/home`: 318958944256 available bytes; 82.21% used; 112480424 free inodes.

server1 `/tmp`: 318958944256 available bytes; 82.21% used; 112480424 free inodes.

server1 `/var/tmp`: 318958944256 available bytes; 82.21% used; 112480424 free inodes.

server1 `/mnt/raid5`: 416195092480 available bytes; 98.09% used; 337604711 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23007268864 available bytes; 98.72% used; 110410439 free inodes.

server2 `/home`: 23007268864 available bytes; 98.72% used; 110410439 free inodes.

server2 `/tmp`: 23007268864 available bytes; 98.72% used; 110410439 free inodes.

server2 `/var/tmp`: 23007268864 available bytes; 98.72% used; 110410439 free inodes.

server2 `/mnt/raid5`: 482250903552 available bytes; 96.67% used; 445113307 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84350844928 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84350844928 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145421750272 available bytes; 97.99% used; 225811059 free inodes.

server3 `/tmp`: 84350844928 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84350844928 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105895563264 available bytes; 94.09% used; 114351001 free inodes.

server4 `/home`: 105895563264 available bytes; 94.09% used; 114351001 free inodes.

server4 `/data`: 0 available bytes; 100.00% used; 224968807 free inodes.

server4 `/tmp`: 105895563264 available bytes; 94.09% used; 114351001 free inodes.

server4 `/var/tmp`: 105895563264 available bytes; 94.09% used; 114351001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
