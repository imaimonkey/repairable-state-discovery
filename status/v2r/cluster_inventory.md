# V2R cluster inventory

2026-09-26T00:12:58.473281+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318670307328 available bytes; 82.22% used; 112476310 free inodes.

server1 `/home`: 318670307328 available bytes; 82.22% used; 112476310 free inodes.

server1 `/tmp`: 318670307328 available bytes; 82.22% used; 112476310 free inodes.

server1 `/var/tmp`: 318670307328 available bytes; 82.22% used; 112476310 free inodes.

server1 `/mnt/raid5`: 359572340736 available bytes; 98.35% used; 337547067 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22948954112 available bytes; 98.72% used; 110406226 free inodes.

server2 `/home`: 22948954112 available bytes; 98.72% used; 110406226 free inodes.

server2 `/tmp`: 22948954112 available bytes; 98.72% used; 110406226 free inodes.

server2 `/var/tmp`: 22948954112 available bytes; 98.72% used; 110406226 free inodes.

server2 `/mnt/raid5`: 295554400256 available bytes; 97.96% used; 445058034 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84342079488 available bytes; 95.29% used; 114152433 free inodes.

server3 `/home`: 84342079488 available bytes; 95.29% used; 114152433 free inodes.

server3 `/data`: 124948373504 available bytes; 98.27% used; 225819344 free inodes.

server3 `/tmp`: 84342079488 available bytes; 95.29% used; 114152433 free inodes.

server3 `/var/tmp`: 84342079488 available bytes; 95.29% used; 114152433 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105453772800 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105453772800 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178051379200 available bytes; 97.54% used; 224917554 free inodes.

server4 `/tmp`: 105453772800 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105453772800 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
