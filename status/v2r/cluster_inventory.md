# V2R cluster inventory

2026-09-24T01:29:46.433771+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325461553152 available bytes; 81.84% used; 112499666 free inodes.

server1 `/home`: 325461553152 available bytes; 81.84% used; 112499666 free inodes.

server1 `/tmp`: 325461553152 available bytes; 81.84% used; 112499666 free inodes.

server1 `/var/tmp`: 325461553152 available bytes; 81.84% used; 112499666 free inodes.

server1 `/mnt/raid5`: 898458120192 available bytes; 95.88% used; 337733991 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40943423488 available bytes; 97.72% used; 110431993 free inodes.

server2 `/home`: 40943423488 available bytes; 97.72% used; 110431993 free inodes.

server2 `/tmp`: 40943423488 available bytes; 97.72% used; 110431993 free inodes.

server2 `/var/tmp`: 40943423488 available bytes; 97.72% used; 110431993 free inodes.

server2 `/mnt/raid5`: 530970411008 available bytes; 96.33% used; 445201614 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292699844608 available bytes; 83.67% used; 114210375 free inodes.

server3 `/home`: 292699844608 available bytes; 83.67% used; 114210375 free inodes.

server3 `/data`: 82041114624 available bytes; 98.87% used; 225842268 free inodes.

server3 `/tmp`: 292699844608 available bytes; 83.67% used; 114210375 free inodes.

server3 `/var/tmp`: 292699844608 available bytes; 83.67% used; 114210375 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105967349760 available bytes; 94.09% used; 114348832 free inodes.

server4 `/home`: 105967349760 available bytes; 94.09% used; 114348832 free inodes.

server4 `/data`: 290807459840 available bytes; 95.98% used; 225396963 free inodes.

server4 `/tmp`: 105967349760 available bytes; 94.09% used; 114348832 free inodes.

server4 `/var/tmp`: 105967349760 available bytes; 94.09% used; 114348832 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
