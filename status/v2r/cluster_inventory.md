# V2R cluster inventory

2026-09-26T02:22:40.680051+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318418018304 available bytes; 82.24% used; 112476283 free inodes.

server1 `/home`: 318418018304 available bytes; 82.24% used; 112476283 free inodes.

server1 `/tmp`: 318418018304 available bytes; 82.24% used; 112476283 free inodes.

server1 `/var/tmp`: 318418018304 available bytes; 82.24% used; 112476283 free inodes.

server1 `/mnt/raid5`: 344985972736 available bytes; 98.42% used; 337546189 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22936461312 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22936461312 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22936461312 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22936461312 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 289211940864 available bytes; 98.00% used; 445054843 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84317454336 available bytes; 95.29% used; 114152370 free inodes.

server3 `/home`: 84317454336 available bytes; 95.29% used; 114152370 free inodes.

server3 `/data`: 124790165504 available bytes; 98.28% used; 225817126 free inodes.

server3 `/tmp`: 84317454336 available bytes; 95.29% used; 114152370 free inodes.

server3 `/var/tmp`: 84317454336 available bytes; 95.29% used; 114152370 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106126876672 available bytes; 94.08% used; 114349423 free inodes.

server4 `/home`: 106126876672 available bytes; 94.08% used; 114349423 free inodes.

server4 `/data`: 130902835200 available bytes; 98.19% used; 224915756 free inodes.

server4 `/tmp`: 106126876672 available bytes; 94.08% used; 114349423 free inodes.

server4 `/var/tmp`: 106126876672 available bytes; 94.08% used; 114349423 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
