# V2R cluster inventory

2026-09-27T06:35:45.065102+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314499072000 available bytes; 82.46% used; 112440814 free inodes.

server1 `/home`: 314499072000 available bytes; 82.46% used; 112440814 free inodes.

server1 `/tmp`: 314499072000 available bytes; 82.46% used; 112440814 free inodes.

server1 `/var/tmp`: 314499072000 available bytes; 82.46% used; 112440814 free inodes.

server1 `/mnt/raid5`: 634680360960 available bytes; 97.09% used; 337400006 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17620013056 available bytes; 99.02% used; 110365003 free inodes.

server2 `/home`: 17620013056 available bytes; 99.02% used; 110365003 free inodes.

server2 `/tmp`: 17620013056 available bytes; 99.02% used; 110365003 free inodes.

server2 `/var/tmp`: 17620013056 available bytes; 99.02% used; 110365003 free inodes.

server2 `/mnt/raid5`: 572936216576 available bytes; 96.04% used; 444875586 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78575661056 available bytes; 95.62% used; 114062896 free inodes.

server3 `/home`: 78575661056 available bytes; 95.62% used; 114062896 free inodes.

server3 `/data`: 1333173043200 available bytes; 81.58% used; 225765004 free inodes.

server3 `/tmp`: 78575661056 available bytes; 95.62% used; 114062896 free inodes.

server3 `/var/tmp`: 78575661056 available bytes; 95.62% used; 114062896 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 110998003712 available bytes; 93.81% used; 114372899 free inodes.

server4 `/home`: 110998003712 available bytes; 93.81% used; 114372899 free inodes.

server4 `/data`: 374460764160 available bytes; 94.82% used; 224771173 free inodes.

server4 `/tmp`: 110998003712 available bytes; 93.81% used; 114372899 free inodes.

server4 `/var/tmp`: 110998003712 available bytes; 93.81% used; 114372899 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
