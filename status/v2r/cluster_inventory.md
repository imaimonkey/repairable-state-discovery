# V2R cluster inventory

2026-09-26T00:26:42.311294+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318654713856 available bytes; 82.22% used; 112476283 free inodes.

server1 `/home`: 318654713856 available bytes; 82.22% used; 112476283 free inodes.

server1 `/tmp`: 318654713856 available bytes; 82.22% used; 112476283 free inodes.

server1 `/var/tmp`: 318654713856 available bytes; 82.22% used; 112476283 free inodes.

server1 `/mnt/raid5`: 359402475520 available bytes; 98.35% used; 337546906 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22942547968 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22942547968 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22942547968 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22942547968 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 295201206272 available bytes; 97.96% used; 445057887 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84339208192 available bytes; 95.29% used; 114152441 free inodes.

server3 `/home`: 84339208192 available bytes; 95.29% used; 114152441 free inodes.

server3 `/data`: 124948692992 available bytes; 98.27% used; 225819117 free inodes.

server3 `/tmp`: 84339208192 available bytes; 95.29% used; 114152441 free inodes.

server3 `/var/tmp`: 84339208192 available bytes; 95.29% used; 114152441 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105453285376 available bytes; 94.12% used; 114348369 free inodes.

server4 `/home`: 105453285376 available bytes; 94.12% used; 114348369 free inodes.

server4 `/data`: 177933737984 available bytes; 97.54% used; 224917516 free inodes.

server4 `/tmp`: 105453285376 available bytes; 94.12% used; 114348369 free inodes.

server4 `/var/tmp`: 105453285376 available bytes; 94.12% used; 114348369 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
