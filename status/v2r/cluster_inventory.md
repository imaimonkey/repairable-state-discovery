# V2R cluster inventory

2026-09-26T00:31:16.918326+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318652690432 available bytes; 82.22% used; 112476291 free inodes.

server1 `/home`: 318652690432 available bytes; 82.22% used; 112476291 free inodes.

server1 `/tmp`: 318652690432 available bytes; 82.22% used; 112476291 free inodes.

server1 `/var/tmp`: 318652690432 available bytes; 82.22% used; 112476291 free inodes.

server1 `/mnt/raid5`: 318103814144 available bytes; 98.54% used; 337546851 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940676096 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22940676096 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22940676096 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22940676096 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 295048482816 available bytes; 97.96% used; 445057865 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340527104 available bytes; 95.29% used; 114152443 free inodes.

server3 `/home`: 84340527104 available bytes; 95.29% used; 114152443 free inodes.

server3 `/data`: 124945268736 available bytes; 98.27% used; 225819046 free inodes.

server3 `/tmp`: 84340527104 available bytes; 95.29% used; 114152443 free inodes.

server3 `/var/tmp`: 84340527104 available bytes; 95.29% used; 114152443 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105453137920 available bytes; 94.12% used; 114348369 free inodes.

server4 `/home`: 105453137920 available bytes; 94.12% used; 114348369 free inodes.

server4 `/data`: 176288137216 available bytes; 97.56% used; 224917472 free inodes.

server4 `/tmp`: 105453137920 available bytes; 94.12% used; 114348369 free inodes.

server4 `/var/tmp`: 105453137920 available bytes; 94.12% used; 114348369 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
