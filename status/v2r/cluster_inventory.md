# V2R cluster inventory

2026-09-27T05:25:37.093194+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314756845568 available bytes; 82.44% used; 112442987 free inodes.

server1 `/home`: 314756845568 available bytes; 82.44% used; 112442987 free inodes.

server1 `/tmp`: 314756845568 available bytes; 82.44% used; 112442987 free inodes.

server1 `/var/tmp`: 314756845568 available bytes; 82.44% used; 112442987 free inodes.

server1 `/mnt/raid5`: 634735505408 available bytes; 97.09% used; 337400032 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17627815936 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17627815936 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17627815936 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17627815936 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 575240990720 available bytes; 96.03% used; 444877835 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78575566848 available bytes; 95.62% used; 114062911 free inodes.

server3 `/home`: 78575566848 available bytes; 95.62% used; 114062911 free inodes.

server3 `/data`: 1332915425280 available bytes; 81.58% used; 225757982 free inodes.

server3 `/tmp`: 78575566848 available bytes; 95.62% used; 114062911 free inodes.

server3 `/var/tmp`: 78575566848 available bytes; 95.62% used; 114062911 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 110999781376 available bytes; 93.81% used; 114372905 free inodes.

server4 `/home`: 110999781376 available bytes; 93.81% used; 114372905 free inodes.

server4 `/data`: 375647518720 available bytes; 94.81% used; 224771846 free inodes.

server4 `/tmp`: 110999781376 available bytes; 93.81% used; 114372905 free inodes.

server4 `/var/tmp`: 110999781376 available bytes; 93.81% used; 114372905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
