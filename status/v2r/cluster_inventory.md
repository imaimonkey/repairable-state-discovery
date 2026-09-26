# V2R cluster inventory

2026-09-26T00:24:10.062061+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318655598592 available bytes; 82.22% used; 112476279 free inodes.

server1 `/home`: 318655598592 available bytes; 82.22% used; 112476279 free inodes.

server1 `/tmp`: 318655598592 available bytes; 82.22% used; 112476279 free inodes.

server1 `/var/tmp`: 318655598592 available bytes; 82.22% used; 112476279 free inodes.

server1 `/mnt/raid5`: 359508680704 available bytes; 98.35% used; 337546977 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22949072896 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22949072896 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22949072896 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22949072896 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 295269601280 available bytes; 97.96% used; 445057979 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339634176 available bytes; 95.29% used; 114152433 free inodes.

server3 `/home`: 84339634176 available bytes; 95.29% used; 114152433 free inodes.

server3 `/data`: 124948271104 available bytes; 98.27% used; 225819151 free inodes.

server3 `/tmp`: 84339634176 available bytes; 95.29% used; 114152433 free inodes.

server3 `/var/tmp`: 84339634176 available bytes; 95.29% used; 114152433 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453416448 available bytes; 94.12% used; 114348386 free inodes.

server4 `/home`: 105453416448 available bytes; 94.12% used; 114348386 free inodes.

server4 `/data`: 178008866816 available bytes; 97.54% used; 224917529 free inodes.

server4 `/tmp`: 105453416448 available bytes; 94.12% used; 114348386 free inodes.

server4 `/var/tmp`: 105453416448 available bytes; 94.12% used; 114348386 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
