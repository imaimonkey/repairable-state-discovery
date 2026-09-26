# V2R cluster inventory

2026-09-26T00:41:57.858992+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318650667008 available bytes; 82.22% used; 112476302 free inodes.

server1 `/home`: 318650667008 available bytes; 82.22% used; 112476302 free inodes.

server1 `/tmp`: 318650667008 available bytes; 82.22% used; 112476302 free inodes.

server1 `/var/tmp`: 318650667008 available bytes; 82.22% used; 112476302 free inodes.

server1 `/mnt/raid5`: 345607782400 available bytes; 98.41% used; 337546786 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22941126656 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22941126656 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22941126656 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22941126656 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 294746013696 available bytes; 97.96% used; 445057421 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84342923264 available bytes; 95.29% used; 114152441 free inodes.

server3 `/home`: 84342923264 available bytes; 95.29% used; 114152441 free inodes.

server3 `/data`: 124944666624 available bytes; 98.27% used; 225818848 free inodes.

server3 `/tmp`: 84342923264 available bytes; 95.29% used; 114152441 free inodes.

server3 `/var/tmp`: 84342923264 available bytes; 95.29% used; 114152441 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105349443584 available bytes; 94.12% used; 114347249 free inodes.

server4 `/home`: 105349443584 available bytes; 94.12% used; 114347249 free inodes.

server4 `/data`: 148675039232 available bytes; 97.95% used; 224917387 free inodes.

server4 `/tmp`: 105349443584 available bytes; 94.12% used; 114347249 free inodes.

server4 `/var/tmp`: 105349443584 available bytes; 94.12% used; 114347249 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
