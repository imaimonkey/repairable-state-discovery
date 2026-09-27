# V2R cluster inventory

2026-09-27T04:53:35.886429+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314888654848 available bytes; 82.43% used; 112443032 free inodes.

server1 `/home`: 314888654848 available bytes; 82.43% used; 112443032 free inodes.

server1 `/tmp`: 314888654848 available bytes; 82.43% used; 112443032 free inodes.

server1 `/var/tmp`: 314888654848 available bytes; 82.43% used; 112443032 free inodes.

server1 `/mnt/raid5`: 636059394048 available bytes; 97.08% used; 337400301 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17621970944 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17621970944 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17621970944 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17621970944 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 576152891392 available bytes; 96.02% used; 444878715 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78695440384 available bytes; 95.61% used; 114062916 free inodes.

server3 `/home`: 78695440384 available bytes; 95.61% used; 114062916 free inodes.

server3 `/data`: 1333985280000 available bytes; 81.56% used; 225758848 free inodes.

server3 `/tmp`: 78695440384 available bytes; 95.61% used; 114062916 free inodes.

server3 `/var/tmp`: 78695440384 available bytes; 95.61% used; 114062916 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111000760320 available bytes; 93.81% used; 114372935 free inodes.

server4 `/home`: 111000760320 available bytes; 93.81% used; 114372935 free inodes.

server4 `/data`: 382107729920 available bytes; 94.72% used; 224780548 free inodes.

server4 `/tmp`: 111000760320 available bytes; 93.81% used; 114372935 free inodes.

server4 `/var/tmp`: 111000760320 available bytes; 93.81% used; 114372935 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
