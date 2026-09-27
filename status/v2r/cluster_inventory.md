# V2R cluster inventory

2026-09-27T07:39:48.414006+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314471845888 available bytes; 82.46% used; 112440796 free inodes.

server1 `/home`: 314471845888 available bytes; 82.46% used; 112440796 free inodes.

server1 `/tmp`: 314471845888 available bytes; 82.46% used; 112440796 free inodes.

server1 `/var/tmp`: 314471845888 available bytes; 82.46% used; 112440796 free inodes.

server1 `/mnt/raid5`: 634658582528 available bytes; 97.09% used; 337400008 free inodes.
| server2 | True | ['0', '1'] | [] |

server2 `/`: 17613254656 available bytes; 99.02% used; 110365014 free inodes.

server2 `/home`: 17613254656 available bytes; 99.02% used; 110365014 free inodes.

server2 `/tmp`: 17613254656 available bytes; 99.02% used; 110365014 free inodes.

server2 `/var/tmp`: 17613254656 available bytes; 99.02% used; 110365014 free inodes.

server2 `/mnt/raid5`: 571095678976 available bytes; 96.05% used; 444873695 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 78572617728 available bytes; 95.62% used; 114062876 free inodes.

server3 `/home`: 78572617728 available bytes; 95.62% used; 114062876 free inodes.

server3 `/data`: 1333023219712 available bytes; 81.58% used; 225763987 free inodes.

server3 `/tmp`: 78572617728 available bytes; 95.62% used; 114062876 free inodes.

server3 `/var/tmp`: 78572617728 available bytes; 95.62% used; 114062876 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111070281728 available bytes; 93.80% used; 114372888 free inodes.

server4 `/home`: 111070281728 available bytes; 93.80% used; 114372888 free inodes.

server4 `/data`: 374300237824 available bytes; 94.83% used; 224770988 free inodes.

server4 `/tmp`: 111070281728 available bytes; 93.80% used; 114372888 free inodes.

server4 `/var/tmp`: 111070281728 available bytes; 93.80% used; 114372888 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
