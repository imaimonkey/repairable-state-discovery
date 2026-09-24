# V2R cluster inventory

2026-09-24T02:10:14.541727+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325446234112 available bytes; 81.84% used; 112499231 free inodes.

server1 `/home`: 325446234112 available bytes; 81.84% used; 112499231 free inodes.

server1 `/tmp`: 325446234112 available bytes; 81.84% used; 112499231 free inodes.

server1 `/var/tmp`: 325446234112 available bytes; 81.84% used; 112499231 free inodes.

server1 `/mnt/raid5`: 731904339968 available bytes; 96.64% used; 337733521 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40907579392 available bytes; 97.72% used; 110431678 free inodes.

server2 `/home`: 40907579392 available bytes; 97.72% used; 110431678 free inodes.

server2 `/tmp`: 40907579392 available bytes; 97.72% used; 110431678 free inodes.

server2 `/var/tmp`: 40907579392 available bytes; 97.72% used; 110431678 free inodes.

server2 `/mnt/raid5`: 516099821568 available bytes; 96.43% used; 445200126 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292685344768 available bytes; 83.67% used; 114210523 free inodes.

server3 `/home`: 292685344768 available bytes; 83.67% used; 114210523 free inodes.

server3 `/data`: 28449521664 available bytes; 99.61% used; 225841407 free inodes.

server3 `/tmp`: 292685344768 available bytes; 83.67% used; 114210523 free inodes.

server3 `/var/tmp`: 292685344768 available bytes; 83.67% used; 114210523 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105932423168 available bytes; 94.09% used; 114348266 free inodes.

server4 `/home`: 105932423168 available bytes; 94.09% used; 114348266 free inodes.

server4 `/data`: 289762828288 available bytes; 96.00% used; 225388464 free inodes.

server4 `/tmp`: 105932423168 available bytes; 94.09% used; 114348266 free inodes.

server4 `/var/tmp`: 105932423168 available bytes; 94.09% used; 114348266 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
