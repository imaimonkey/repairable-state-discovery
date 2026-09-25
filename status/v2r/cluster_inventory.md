# V2R cluster inventory

2026-09-25T23:28:42.411030+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318675718144 available bytes; 82.22% used; 112476316 free inodes.

server1 `/home`: 318675718144 available bytes; 82.22% used; 112476316 free inodes.

server1 `/tmp`: 318675718144 available bytes; 82.22% used; 112476316 free inodes.

server1 `/var/tmp`: 318675718144 available bytes; 82.22% used; 112476316 free inodes.

server1 `/mnt/raid5`: 360123011072 available bytes; 98.35% used; 337538666 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22945841152 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22945841152 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22945841152 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22945841152 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 296808886272 available bytes; 97.95% used; 445051060 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84348272640 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84348272640 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124821692416 available bytes; 98.27% used; 225811684 free inodes.

server3 `/tmp`: 84348272640 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84348272640 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105125158912 available bytes; 94.13% used; 114346703 free inodes.

server4 `/home`: 105125158912 available bytes; 94.13% used; 114346703 free inodes.

server4 `/data`: 181679149056 available bytes; 97.49% used; 224917614 free inodes.

server4 `/tmp`: 105125158912 available bytes; 94.13% used; 114346703 free inodes.

server4 `/var/tmp`: 105125158912 available bytes; 94.13% used; 114346703 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
