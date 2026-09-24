# V2R cluster inventory

2026-09-24T03:33:39.277756+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324893868032 available bytes; 81.88% used; 112494763 free inodes.

server1 `/home`: 324893868032 available bytes; 81.88% used; 112494763 free inodes.

server1 `/tmp`: 324893868032 available bytes; 81.88% used; 112494763 free inodes.

server1 `/var/tmp`: 324893868032 available bytes; 81.88% used; 112494763 free inodes.

server1 `/mnt/raid5`: 397485928448 available bytes; 98.18% used; 337734006 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40832512000 available bytes; 97.72% used; 110431080 free inodes.

server2 `/home`: 40832512000 available bytes; 97.72% used; 110431080 free inodes.

server2 `/tmp`: 40832512000 available bytes; 97.72% used; 110431080 free inodes.

server2 `/var/tmp`: 40832512000 available bytes; 97.72% used; 110431080 free inodes.

server2 `/mnt/raid5`: 527116476416 available bytes; 96.36% used; 445197949 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292355805184 available bytes; 83.69% used; 114199420 free inodes.

server3 `/home`: 292355805184 available bytes; 83.69% used; 114199420 free inodes.

server3 `/data`: 36008173568 available bytes; 99.50% used; 225842975 free inodes.

server3 `/tmp`: 292355805184 available bytes; 83.69% used; 114199420 free inodes.

server3 `/var/tmp`: 292355805184 available bytes; 83.69% used; 114199420 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105986932736 available bytes; 94.09% used; 114349605 free inodes.

server4 `/home`: 105986932736 available bytes; 94.09% used; 114349605 free inodes.

server4 `/data`: 281514831872 available bytes; 96.11% used; 225385438 free inodes.

server4 `/tmp`: 105986932736 available bytes; 94.09% used; 114349605 free inodes.

server4 `/var/tmp`: 105986932736 available bytes; 94.09% used; 114349605 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
