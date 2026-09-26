# V2R cluster inventory

2026-09-26T03:53:31.234085+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318415339520 available bytes; 82.24% used; 112476261 free inodes.

server1 `/home`: 318415339520 available bytes; 82.24% used; 112476261 free inodes.

server1 `/tmp`: 318415339520 available bytes; 82.24% used; 112476261 free inodes.

server1 `/var/tmp`: 318415339520 available bytes; 82.24% used; 112476261 free inodes.

server1 `/mnt/raid5`: 330968334336 available bytes; 98.48% used; 337545693 free inodes.
| server2 | True | ['1'] | [] |

server2 `/`: 22932729856 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22932729856 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22932729856 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22932729856 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 286563377152 available bytes; 98.02% used; 445051689 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84307673088 available bytes; 95.30% used; 114152336 free inodes.

server3 `/home`: 84307673088 available bytes; 95.30% used; 114152336 free inodes.

server3 `/data`: 124612653056 available bytes; 98.28% used; 225820527 free inodes.

server3 `/tmp`: 84307673088 available bytes; 95.30% used; 114152336 free inodes.

server3 `/var/tmp`: 84307673088 available bytes; 95.30% used; 114152336 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105698803712 available bytes; 94.10% used; 114346605 free inodes.

server4 `/home`: 105698803712 available bytes; 94.10% used; 114346605 free inodes.

server4 `/data`: 109797257216 available bytes; 98.48% used; 224929556 free inodes.

server4 `/tmp`: 105698803712 available bytes; 94.10% used; 114346605 free inodes.

server4 `/var/tmp`: 105698803712 available bytes; 94.10% used; 114346605 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
