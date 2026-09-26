# V2R cluster inventory

2026-09-26T00:05:20.755365+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318671495168 available bytes; 82.22% used; 112476309 free inodes.

server1 `/home`: 318671495168 available bytes; 82.22% used; 112476309 free inodes.

server1 `/tmp`: 318671495168 available bytes; 82.22% used; 112476309 free inodes.

server1 `/var/tmp`: 318671495168 available bytes; 82.22% used; 112476309 free inodes.

server1 `/mnt/raid5`: 359430803456 available bytes; 98.35% used; 337538401 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22943436800 available bytes; 98.72% used; 110406226 free inodes.

server2 `/home`: 22943436800 available bytes; 98.72% used; 110406226 free inodes.

server2 `/tmp`: 22943436800 available bytes; 98.72% used; 110406226 free inodes.

server2 `/var/tmp`: 22943436800 available bytes; 98.72% used; 110406226 free inodes.

server2 `/mnt/raid5`: 296069169152 available bytes; 97.95% used; 445049897 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84348121088 available bytes; 95.29% used; 114152438 free inodes.

server3 `/home`: 84348121088 available bytes; 95.29% used; 114152438 free inodes.

server3 `/data`: 124798722048 available bytes; 98.28% used; 225810803 free inodes.

server3 `/tmp`: 84348121088 available bytes; 95.29% used; 114152438 free inodes.

server3 `/var/tmp`: 84348121088 available bytes; 95.29% used; 114152438 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105453998080 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105453998080 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178050699264 available bytes; 97.54% used; 224917554 free inodes.

server4 `/tmp`: 105453998080 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105453998080 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
