# V2R cluster inventory

2026-09-25T23:43:57.758635+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318674051072 available bytes; 82.22% used; 112476312 free inodes.

server1 `/home`: 318674051072 available bytes; 82.22% used; 112476312 free inodes.

server1 `/tmp`: 318674051072 available bytes; 82.22% used; 112476312 free inodes.

server1 `/var/tmp`: 318674051072 available bytes; 82.22% used; 112476312 free inodes.

server1 `/mnt/raid5`: 360084422656 available bytes; 98.35% used; 337538588 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22950195200 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22950195200 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22950195200 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22950195200 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 296620376064 available bytes; 97.95% used; 445050708 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84351270912 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84351270912 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124803514368 available bytes; 98.28% used; 225811255 free inodes.

server3 `/tmp`: 84351270912 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84351270912 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105082716160 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082716160 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178219192320 available bytes; 97.54% used; 224917591 free inodes.

server4 `/tmp`: 105082716160 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082716160 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
