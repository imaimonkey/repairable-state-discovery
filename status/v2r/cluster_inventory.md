# V2R cluster inventory

2026-09-26T03:50:27.801603+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318415859712 available bytes; 82.24% used; 112476261 free inodes.

server1 `/home`: 318415859712 available bytes; 82.24% used; 112476261 free inodes.

server1 `/tmp`: 318415859712 available bytes; 82.24% used; 112476261 free inodes.

server1 `/var/tmp`: 318415859712 available bytes; 82.24% used; 112476261 free inodes.

server1 `/mnt/raid5`: 310333734912 available bytes; 98.58% used; 337545714 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22940733440 available bytes; 98.72% used; 110406194 free inodes.

server2 `/home`: 22940733440 available bytes; 98.72% used; 110406194 free inodes.

server2 `/tmp`: 22940733440 available bytes; 98.72% used; 110406194 free inodes.

server2 `/var/tmp`: 22940733440 available bytes; 98.72% used; 110406194 free inodes.

server2 `/mnt/raid5`: 286648823808 available bytes; 98.02% used; 445051800 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84161015808 available bytes; 95.30% used; 114152333 free inodes.

server3 `/home`: 84161015808 available bytes; 95.30% used; 114152333 free inodes.

server3 `/data`: 125022109696 available bytes; 98.27% used; 225820914 free inodes.

server3 `/tmp`: 84161015808 available bytes; 95.30% used; 114152333 free inodes.

server3 `/var/tmp`: 84161015808 available bytes; 95.30% used; 114152333 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105732481024 available bytes; 94.10% used; 114346692 free inodes.

server4 `/home`: 105732481024 available bytes; 94.10% used; 114346692 free inodes.

server4 `/data`: 109839564800 available bytes; 98.48% used; 224929559 free inodes.

server4 `/tmp`: 105732481024 available bytes; 94.10% used; 114346692 free inodes.

server4 `/var/tmp`: 105732481024 available bytes; 94.10% used; 114346692 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
