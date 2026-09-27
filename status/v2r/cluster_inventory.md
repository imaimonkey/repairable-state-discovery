# V2R cluster inventory

2026-09-27T05:19:31.213236+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314755375104 available bytes; 82.44% used; 112442998 free inodes.

server1 `/home`: 314755375104 available bytes; 82.44% used; 112442998 free inodes.

server1 `/tmp`: 314755375104 available bytes; 82.44% used; 112442998 free inodes.

server1 `/var/tmp`: 314755375104 available bytes; 82.44% used; 112442998 free inodes.

server1 `/mnt/raid5`: 634730606592 available bytes; 97.09% used; 337400246 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17628291072 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17628291072 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17628291072 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17628291072 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 575410028544 available bytes; 96.02% used; 444878001 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78579769344 available bytes; 95.61% used; 114062911 free inodes.

server3 `/home`: 78579769344 available bytes; 95.61% used; 114062911 free inodes.

server3 `/data`: 1332933009408 available bytes; 81.58% used; 225758108 free inodes.

server3 `/tmp`: 78579769344 available bytes; 95.61% used; 114062911 free inodes.

server3 `/var/tmp`: 78579769344 available bytes; 95.61% used; 114062911 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 110999953408 available bytes; 93.81% used; 114372909 free inodes.

server4 `/home`: 110999953408 available bytes; 93.81% used; 114372909 free inodes.

server4 `/data`: 380114702336 available bytes; 94.75% used; 224776186 free inodes.

server4 `/tmp`: 110999953408 available bytes; 93.81% used; 114372909 free inodes.

server4 `/var/tmp`: 110999953408 available bytes; 93.81% used; 114372909 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
