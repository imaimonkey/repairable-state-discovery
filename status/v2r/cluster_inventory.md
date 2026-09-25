# V2R cluster inventory

2026-09-25T22:53:36.466961+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318694178816 available bytes; 82.22% used; 112476293 free inodes.

server1 `/home`: 318694178816 available bytes; 82.22% used; 112476293 free inodes.

server1 `/tmp`: 318694178816 available bytes; 82.22% used; 112476293 free inodes.

server1 `/var/tmp`: 318694178816 available bytes; 82.22% used; 112476293 free inodes.

server1 `/mnt/raid5`: 360189247488 available bytes; 98.35% used; 337538823 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22946267136 available bytes; 98.72% used; 110406228 free inodes.

server2 `/home`: 22946267136 available bytes; 98.72% used; 110406228 free inodes.

server2 `/tmp`: 22946267136 available bytes; 98.72% used; 110406228 free inodes.

server2 `/var/tmp`: 22946267136 available bytes; 98.72% used; 110406228 free inodes.

server2 `/mnt/raid5`: 298306691072 available bytes; 97.94% used; 445052348 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84350775296 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84350775296 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124821479424 available bytes; 98.27% used; 225805563 free inodes.

server3 `/tmp`: 84350775296 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84350775296 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105235349504 available bytes; 94.13% used; 114346964 free inodes.

server4 `/home`: 105235349504 available bytes; 94.13% used; 114346964 free inodes.

server4 `/data`: 192135725056 available bytes; 97.34% used; 224917678 free inodes.

server4 `/tmp`: 105235349504 available bytes; 94.13% used; 114346964 free inodes.

server4 `/var/tmp`: 105235349504 available bytes; 94.13% used; 114346964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
