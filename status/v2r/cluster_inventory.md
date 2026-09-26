# V2R cluster inventory

2026-09-26T00:02:17.543813+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318672216064 available bytes; 82.22% used; 112476310 free inodes.

server1 `/home`: 318672216064 available bytes; 82.22% used; 112476310 free inodes.

server1 `/tmp`: 318672216064 available bytes; 82.22% used; 112476310 free inodes.

server1 `/var/tmp`: 318672216064 available bytes; 82.22% used; 112476310 free inodes.

server1 `/mnt/raid5`: 359440756736 available bytes; 98.35% used; 337538421 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22944575488 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22944575488 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22944575488 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22944575488 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 296151990272 available bytes; 97.95% used; 445049880 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84347600896 available bytes; 95.29% used; 114152430 free inodes.

server3 `/home`: 84347600896 available bytes; 95.29% used; 114152430 free inodes.

server3 `/data`: 124800176128 available bytes; 98.28% used; 225810860 free inodes.

server3 `/tmp`: 84347600896 available bytes; 95.29% used; 114152430 free inodes.

server3 `/var/tmp`: 84347600896 available bytes; 95.29% used; 114152430 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105454071808 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105454071808 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178052956160 available bytes; 97.54% used; 224917568 free inodes.

server4 `/tmp`: 105454071808 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105454071808 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
