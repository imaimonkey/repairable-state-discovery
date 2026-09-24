# V2R cluster inventory

2026-09-24T07:12:28.546046+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324454920192 available bytes; 81.90% used; 112491244 free inodes.

server1 `/home`: 324454920192 available bytes; 81.90% used; 112491244 free inodes.

server1 `/tmp`: 324454920192 available bytes; 81.90% used; 112491244 free inodes.

server1 `/var/tmp`: 324454920192 available bytes; 81.90% used; 112491244 free inodes.

server1 `/mnt/raid5`: 517427040256 available bytes; 97.63% used; 337722824 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57855086592 available bytes; 96.77% used; 110431145 free inodes.

server2 `/home`: 57855086592 available bytes; 96.77% used; 110431145 free inodes.

server2 `/tmp`: 57855086592 available bytes; 96.77% used; 110431145 free inodes.

server2 `/var/tmp`: 57855086592 available bytes; 96.77% used; 110431145 free inodes.

server2 `/mnt/raid5`: 518808711168 available bytes; 96.42% used; 445181511 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127145902080 available bytes; 92.90% used; 114199321 free inodes.

server3 `/home`: 127145902080 available bytes; 92.90% used; 114199321 free inodes.

server3 `/data`: 139105509376 available bytes; 98.08% used; 225834490 free inodes.

server3 `/tmp`: 127145902080 available bytes; 92.90% used; 114199321 free inodes.

server3 `/var/tmp`: 127145902080 available bytes; 92.90% used; 114199321 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105789972480 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105789972480 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 295271583744 available bytes; 95.92% used; 225367329 free inodes.

server4 `/tmp`: 105789972480 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105789972480 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
