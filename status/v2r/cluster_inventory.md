# V2R cluster inventory

2026-09-27T07:45:54.081336+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314470977536 available bytes; 82.46% used; 112440796 free inodes.

server1 `/home`: 314470977536 available bytes; 82.46% used; 112440796 free inodes.

server1 `/tmp`: 314470977536 available bytes; 82.46% used; 112440796 free inodes.

server1 `/var/tmp`: 314470977536 available bytes; 82.46% used; 112440796 free inodes.

server1 `/mnt/raid5`: 634656137216 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 17608597504 available bytes; 99.02% used; 110365017 free inodes.

server2 `/home`: 17608597504 available bytes; 99.02% used; 110365017 free inodes.

server2 `/tmp`: 17608597504 available bytes; 99.02% used; 110365017 free inodes.

server2 `/var/tmp`: 17608597504 available bytes; 99.02% used; 110365017 free inodes.

server2 `/mnt/raid5`: 570923597824 available bytes; 96.06% used; 444873787 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 78571749376 available bytes; 95.62% used; 114062876 free inodes.

server3 `/home`: 78571749376 available bytes; 95.62% used; 114062876 free inodes.

server3 `/data`: 1333015552000 available bytes; 81.58% used; 225763924 free inodes.

server3 `/tmp`: 78571749376 available bytes; 95.62% used; 114062876 free inodes.

server3 `/var/tmp`: 78571749376 available bytes; 95.62% used; 114062876 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111070089216 available bytes; 93.80% used; 114372883 free inodes.

server4 `/home`: 111070089216 available bytes; 93.80% used; 114372883 free inodes.

server4 `/data`: 374289903616 available bytes; 94.83% used; 224770986 free inodes.

server4 `/tmp`: 111070089216 available bytes; 93.80% used; 114372883 free inodes.

server4 `/var/tmp`: 111070089216 available bytes; 93.80% used; 114372883 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
