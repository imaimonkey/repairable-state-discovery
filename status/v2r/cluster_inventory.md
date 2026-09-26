# V2R cluster inventory

2026-09-26T06:16:18.102462+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318778630144 available bytes; 82.22% used; 112476286 free inodes.

server1 `/home`: 318778630144 available bytes; 82.22% used; 112476286 free inodes.

server1 `/tmp`: 318778630144 available bytes; 82.22% used; 112476286 free inodes.

server1 `/var/tmp`: 318778630144 available bytes; 82.22% used; 112476286 free inodes.

server1 `/mnt/raid5`: 219713859584 available bytes; 98.99% used; 337539876 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22319808512 available bytes; 98.75% used; 110403783 free inodes.

server2 `/home`: 22319808512 available bytes; 98.75% used; 110403783 free inodes.

server2 `/tmp`: 22319808512 available bytes; 98.75% used; 110403783 free inodes.

server2 `/var/tmp`: 22319808512 available bytes; 98.75% used; 110403783 free inodes.

server2 `/mnt/raid5`: 272359055360 available bytes; 98.12% used; 445029069 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82568912896 available bytes; 95.39% used; 114110905 free inodes.

server3 `/home`: 82568912896 available bytes; 95.39% used; 114110905 free inodes.

server3 `/data`: 123990859776 available bytes; 98.29% used; 225822516 free inodes.

server3 `/tmp`: 82568912896 available bytes; 95.39% used; 114110905 free inodes.

server3 `/var/tmp`: 82568912896 available bytes; 95.39% used; 114110905 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105981730816 available bytes; 94.09% used; 114347062 free inodes.

server4 `/home`: 105981730816 available bytes; 94.09% used; 114347062 free inodes.

server4 `/data`: 106605293568 available bytes; 98.53% used; 224923586 free inodes.

server4 `/tmp`: 105981730816 available bytes; 94.09% used; 114347062 free inodes.

server4 `/var/tmp`: 105981730816 available bytes; 94.09% used; 114347062 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
