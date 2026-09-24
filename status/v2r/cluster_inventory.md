# V2R cluster inventory

2026-09-24T01:20:28.038256+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325471326208 available bytes; 81.84% used; 112499805 free inodes.

server1 `/home`: 325471326208 available bytes; 81.84% used; 112499805 free inodes.

server1 `/tmp`: 325471326208 available bytes; 81.84% used; 112499805 free inodes.

server1 `/var/tmp`: 325471326208 available bytes; 81.84% used; 112499805 free inodes.

server1 `/mnt/raid5`: 937041842176 available bytes; 95.70% used; 337734060 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40952262656 available bytes; 97.72% used; 110432067 free inodes.

server2 `/home`: 40952262656 available bytes; 97.72% used; 110432067 free inodes.

server2 `/tmp`: 40952262656 available bytes; 97.72% used; 110432067 free inodes.

server2 `/var/tmp`: 40952262656 available bytes; 97.72% used; 110432067 free inodes.

server2 `/mnt/raid5`: 531255844864 available bytes; 96.33% used; 445201946 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292347662336 available bytes; 83.69% used; 114187477 free inodes.

server3 `/home`: 292347662336 available bytes; 83.69% used; 114187477 free inodes.

server3 `/data`: 82065805312 available bytes; 98.87% used; 225842536 free inodes.

server3 `/tmp`: 292347662336 available bytes; 83.69% used; 114187477 free inodes.

server3 `/var/tmp`: 292347662336 available bytes; 83.69% used; 114187477 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105986666496 available bytes; 94.09% used; 114349000 free inodes.

server4 `/home`: 105986666496 available bytes; 94.09% used; 114349000 free inodes.

server4 `/data`: 290842918912 available bytes; 95.98% used; 225397012 free inodes.

server4 `/tmp`: 105986666496 available bytes; 94.09% used; 114349000 free inodes.

server4 `/var/tmp`: 105986666496 available bytes; 94.09% used; 114349000 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
