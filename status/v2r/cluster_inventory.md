# V2R cluster inventory

2026-09-26T01:22:12.330747+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318649503744 available bytes; 82.22% used; 112476296 free inodes.

server1 `/home`: 318649503744 available bytes; 82.22% used; 112476296 free inodes.

server1 `/tmp`: 318649503744 available bytes; 82.22% used; 112476296 free inodes.

server1 `/var/tmp`: 318649503744 available bytes; 82.22% used; 112476296 free inodes.

server1 `/mnt/raid5`: 345516785664 available bytes; 98.41% used; 337546592 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22930145280 available bytes; 98.72% used; 110406204 free inodes.

server2 `/home`: 22930145280 available bytes; 98.72% used; 110406204 free inodes.

server2 `/tmp`: 22930145280 available bytes; 98.72% used; 110406204 free inodes.

server2 `/var/tmp`: 22930145280 available bytes; 98.72% used; 110406204 free inodes.

server2 `/mnt/raid5`: 290960646144 available bytes; 97.99% used; 445056240 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339826688 available bytes; 95.29% used; 114152428 free inodes.

server3 `/home`: 84339826688 available bytes; 95.29% used; 114152428 free inodes.

server3 `/data`: 124871716864 available bytes; 98.27% used; 225818155 free inodes.

server3 `/tmp`: 84339826688 available bytes; 95.29% used; 114152428 free inodes.

server3 `/var/tmp`: 84339826688 available bytes; 95.29% used; 114152428 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105264345088 available bytes; 94.13% used; 114347079 free inodes.

server4 `/home`: 105264345088 available bytes; 94.13% used; 114347079 free inodes.

server4 `/data`: 141693005824 available bytes; 98.04% used; 224917305 free inodes.

server4 `/tmp`: 105264345088 available bytes; 94.13% used; 114347079 free inodes.

server4 `/var/tmp`: 105264345088 available bytes; 94.13% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
