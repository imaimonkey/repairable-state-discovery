# V2R cluster inventory

2026-09-26T04:01:55.112657+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318416523264 available bytes; 82.24% used; 112476270 free inodes.

server1 `/home`: 318416523264 available bytes; 82.24% used; 112476270 free inodes.

server1 `/tmp`: 318416523264 available bytes; 82.24% used; 112476270 free inodes.

server1 `/var/tmp`: 318416523264 available bytes; 82.24% used; 112476270 free inodes.

server1 `/mnt/raid5`: 330584907776 available bytes; 98.48% used; 337545607 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22931402752 available bytes; 98.72% used; 110406198 free inodes.

server2 `/home`: 22931402752 available bytes; 98.72% used; 110406198 free inodes.

server2 `/tmp`: 22931402752 available bytes; 98.72% used; 110406198 free inodes.

server2 `/var/tmp`: 22931402752 available bytes; 98.72% used; 110406198 free inodes.

server2 `/mnt/raid5`: 286302720000 available bytes; 98.02% used; 445051562 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84152500224 available bytes; 95.30% used; 114159731 free inodes.

server3 `/home`: 84152500224 available bytes; 95.30% used; 114159731 free inodes.

server3 `/data`: 124587724800 available bytes; 98.28% used; 225820002 free inodes.

server3 `/tmp`: 84152500224 available bytes; 95.30% used; 114159731 free inodes.

server3 `/var/tmp`: 84152500224 available bytes; 95.30% used; 114159731 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106003329024 available bytes; 94.08% used; 114348225 free inodes.

server4 `/home`: 106003329024 available bytes; 94.08% used; 114348225 free inodes.

server4 `/data`: 109757022208 available bytes; 98.48% used; 224929438 free inodes.

server4 `/tmp`: 106003329024 available bytes; 94.08% used; 114348225 free inodes.

server4 `/var/tmp`: 106003329024 available bytes; 94.08% used; 114348225 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
