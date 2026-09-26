# V2R cluster inventory

2026-09-26T03:55:02.850019+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318415069184 available bytes; 82.24% used; 112476261 free inodes.

server1 `/home`: 318415069184 available bytes; 82.24% used; 112476261 free inodes.

server1 `/tmp`: 318415069184 available bytes; 82.24% used; 112476261 free inodes.

server1 `/var/tmp`: 318415069184 available bytes; 82.24% used; 112476261 free inodes.

server1 `/mnt/raid5`: 330965598208 available bytes; 98.48% used; 337545691 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22932271104 available bytes; 98.72% used; 110406194 free inodes.

server2 `/home`: 22932271104 available bytes; 98.72% used; 110406194 free inodes.

server2 `/tmp`: 22932271104 available bytes; 98.72% used; 110406194 free inodes.

server2 `/var/tmp`: 22932271104 available bytes; 98.72% used; 110406194 free inodes.

server2 `/mnt/raid5`: 286523224064 available bytes; 98.02% used; 445051521 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84673380352 available bytes; 95.27% used; 114177893 free inodes.

server3 `/home`: 84673380352 available bytes; 95.27% used; 114177893 free inodes.

server3 `/data`: 124608786432 available bytes; 98.28% used; 225820512 free inodes.

server3 `/tmp`: 84673380352 available bytes; 95.27% used; 114177893 free inodes.

server3 `/var/tmp`: 84673380352 available bytes; 95.27% used; 114177893 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105698766848 available bytes; 94.10% used; 114346608 free inodes.

server4 `/home`: 105698766848 available bytes; 94.10% used; 114346608 free inodes.

server4 `/data`: 109795389440 available bytes; 98.48% used; 224929553 free inodes.

server4 `/tmp`: 105698766848 available bytes; 94.10% used; 114346608 free inodes.

server4 `/var/tmp`: 105698766848 available bytes; 94.10% used; 114346608 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
