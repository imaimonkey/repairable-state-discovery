# V2R cluster inventory

2026-09-27T01:01:51.705987+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315157913600 available bytes; 82.42% used; 112443451 free inodes.

server1 `/home`: 315157913600 available bytes; 82.42% used; 112443451 free inodes.

server1 `/tmp`: 315157913600 available bytes; 82.42% used; 112443451 free inodes.

server1 `/var/tmp`: 315157913600 available bytes; 82.42% used; 112443451 free inodes.

server1 `/mnt/raid5`: 637561606144 available bytes; 97.08% used; 337405783 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17631051776 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17631051776 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17631051776 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17631051776 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 584062636032 available bytes; 95.96% used; 444887501 free inodes.
| server3 | True | ['0', '3'] | [] |

server3 `/`: 79498616832 available bytes; 95.56% used; 114068702 free inodes.

server3 `/home`: 79498616832 available bytes; 95.56% used; 114068702 free inodes.

server3 `/data`: 1342479413248 available bytes; 81.45% used; 225764008 free inodes.

server3 `/tmp`: 79498616832 available bytes; 95.56% used; 114068702 free inodes.

server3 `/var/tmp`: 79498616832 available bytes; 95.56% used; 114068702 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105878499328 available bytes; 94.09% used; 114347835 free inodes.

server4 `/home`: 105878499328 available bytes; 94.09% used; 114347835 free inodes.

server4 `/data`: 406587338752 available bytes; 94.38% used; 224782990 free inodes.

server4 `/tmp`: 105878499328 available bytes; 94.09% used; 114347835 free inodes.

server4 `/var/tmp`: 105878499328 available bytes; 94.09% used; 114347835 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
