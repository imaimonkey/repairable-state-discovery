# V2R cluster inventory

2026-09-24T02:18:02.843017+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325409628160 available bytes; 81.85% used; 112499009 free inodes.

server1 `/home`: 325409628160 available bytes; 81.85% used; 112499009 free inodes.

server1 `/tmp`: 325409628160 available bytes; 81.85% used; 112499009 free inodes.

server1 `/var/tmp`: 325409628160 available bytes; 81.85% used; 112499009 free inodes.

server1 `/mnt/raid5`: 698531328000 available bytes; 96.80% used; 337733345 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40903839744 available bytes; 97.72% used; 110431622 free inodes.

server2 `/home`: 40903839744 available bytes; 97.72% used; 110431622 free inodes.

server2 `/tmp`: 40903839744 available bytes; 97.72% used; 110431622 free inodes.

server2 `/var/tmp`: 40903839744 available bytes; 97.72% used; 110431622 free inodes.

server2 `/mnt/raid5`: 529392025600 available bytes; 96.34% used; 445199760 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292326666240 available bytes; 83.69% used; 114195870 free inodes.

server3 `/home`: 292326666240 available bytes; 83.69% used; 114195870 free inodes.

server3 `/data`: 18121400320 available bytes; 99.75% used; 225847064 free inodes.

server3 `/tmp`: 292326666240 available bytes; 83.69% used; 114195870 free inodes.

server3 `/var/tmp`: 292326666240 available bytes; 83.69% used; 114195870 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105934917632 available bytes; 94.09% used; 114348467 free inodes.

server4 `/home`: 105934917632 available bytes; 94.09% used; 114348467 free inodes.

server4 `/data`: 289740869632 available bytes; 96.00% used; 225387792 free inodes.

server4 `/tmp`: 105934917632 available bytes; 94.09% used; 114348467 free inodes.

server4 `/var/tmp`: 105934917632 available bytes; 94.09% used; 114348467 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
