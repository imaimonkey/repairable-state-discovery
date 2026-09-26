# V2R cluster inventory

2026-09-26T05:35:53.618077+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318792679424 available bytes; 82.22% used; 112476277 free inodes.

server1 `/home`: 318792679424 available bytes; 82.22% used; 112476277 free inodes.

server1 `/tmp`: 318792679424 available bytes; 82.22% used; 112476277 free inodes.

server1 `/var/tmp`: 318792679424 available bytes; 82.22% used; 112476277 free inodes.

server1 `/mnt/raid5`: 251733438464 available bytes; 98.85% used; 337540280 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22928175104 available bytes; 98.72% used; 110406215 free inodes.

server2 `/home`: 22928175104 available bytes; 98.72% used; 110406215 free inodes.

server2 `/tmp`: 22928175104 available bytes; 98.72% used; 110406215 free inodes.

server2 `/var/tmp`: 22928175104 available bytes; 98.72% used; 110406215 free inodes.

server2 `/mnt/raid5`: 276406300672 available bytes; 98.09% used; 445048596 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83195695104 available bytes; 95.36% used; 114149746 free inodes.

server3 `/home`: 83195695104 available bytes; 95.36% used; 114149746 free inodes.

server3 `/data`: 124339392512 available bytes; 98.28% used; 225824158 free inodes.

server3 `/tmp`: 83195695104 available bytes; 95.36% used; 114149746 free inodes.

server3 `/var/tmp`: 83195695104 available bytes; 95.36% used; 114149746 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094776320 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094776320 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 107011919872 available bytes; 98.52% used; 224929216 free inodes.

server4 `/tmp`: 106094776320 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094776320 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
