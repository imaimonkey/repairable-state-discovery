# V2R cluster inventory

2026-09-26T01:25:15.634142+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318648975360 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318648975360 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318648975360 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318648975360 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 345508945920 available bytes; 98.42% used; 337546580 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22929539072 available bytes; 98.72% used; 110406204 free inodes.

server2 `/home`: 22929539072 available bytes; 98.72% used; 110406204 free inodes.

server2 `/tmp`: 22929539072 available bytes; 98.72% used; 110406204 free inodes.

server2 `/var/tmp`: 22929539072 available bytes; 98.72% used; 110406204 free inodes.

server2 `/mnt/raid5`: 290876526592 available bytes; 97.99% used; 445056258 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339056640 available bytes; 95.29% used; 114152428 free inodes.

server3 `/home`: 84339056640 available bytes; 95.29% used; 114152428 free inodes.

server3 `/data`: 124868448256 available bytes; 98.27% used; 225818106 free inodes.

server3 `/tmp`: 84339056640 available bytes; 95.29% used; 114152428 free inodes.

server3 `/var/tmp`: 84339056640 available bytes; 95.29% used; 114152428 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105264267264 available bytes; 94.13% used; 114347079 free inodes.

server4 `/home`: 105264267264 available bytes; 94.13% used; 114347079 free inodes.

server4 `/data`: 141688655872 available bytes; 98.04% used; 224917303 free inodes.

server4 `/tmp`: 105264267264 available bytes; 94.13% used; 114347079 free inodes.

server4 `/var/tmp`: 105264267264 available bytes; 94.13% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
