# V2R cluster inventory

2026-09-26T01:03:52.577841+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318659305472 available bytes; 82.22% used; 112476292 free inodes.

server1 `/home`: 318659305472 available bytes; 82.22% used; 112476292 free inodes.

server1 `/tmp`: 318659305472 available bytes; 82.22% used; 112476292 free inodes.

server1 `/var/tmp`: 318659305472 available bytes; 82.22% used; 112476292 free inodes.

server1 `/mnt/raid5`: 345559785472 available bytes; 98.41% used; 337546687 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939848704 available bytes; 98.72% used; 110406200 free inodes.

server2 `/home`: 22939848704 available bytes; 98.72% used; 110406200 free inodes.

server2 `/tmp`: 22939848704 available bytes; 98.72% used; 110406200 free inodes.

server2 `/var/tmp`: 22939848704 available bytes; 98.72% used; 110406200 free inodes.

server2 `/mnt/raid5`: 293030866944 available bytes; 97.98% used; 445056759 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84338728960 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84338728960 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124936048640 available bytes; 98.27% used; 225818457 free inodes.

server3 `/tmp`: 84338728960 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84338728960 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105281654784 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281654784 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141768052736 available bytes; 98.04% used; 224917336 free inodes.

server4 `/tmp`: 105281654784 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281654784 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
