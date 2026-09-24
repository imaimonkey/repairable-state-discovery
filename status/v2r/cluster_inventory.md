# V2R cluster inventory

2026-09-24T01:18:25.050412+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325473656832 available bytes; 81.84% used; 112499837 free inodes.

server1 `/home`: 325473656832 available bytes; 81.84% used; 112499837 free inodes.

server1 `/tmp`: 325473656832 available bytes; 81.84% used; 112499837 free inodes.

server1 `/var/tmp`: 325473656832 available bytes; 81.84% used; 112499837 free inodes.

server1 `/mnt/raid5`: 944602972160 available bytes; 95.67% used; 337734078 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40953548800 available bytes; 97.72% used; 110432083 free inodes.

server2 `/home`: 40953548800 available bytes; 97.72% used; 110432083 free inodes.

server2 `/tmp`: 40953548800 available bytes; 97.72% used; 110432083 free inodes.

server2 `/var/tmp`: 40953548800 available bytes; 97.72% used; 110432083 free inodes.

server2 `/mnt/raid5`: 531317051392 available bytes; 96.33% used; 445202105 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292347940864 available bytes; 83.69% used; 114187477 free inodes.

server3 `/home`: 292347940864 available bytes; 83.69% used; 114187477 free inodes.

server3 `/data`: 82067505152 available bytes; 98.87% used; 225842568 free inodes.

server3 `/tmp`: 292347940864 available bytes; 83.69% used; 114187477 free inodes.

server3 `/var/tmp`: 292347940864 available bytes; 83.69% used; 114187477 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105989345280 available bytes; 94.09% used; 114349047 free inodes.

server4 `/home`: 105989345280 available bytes; 94.09% used; 114349047 free inodes.

server4 `/data`: 290839560192 available bytes; 95.98% used; 225397015 free inodes.

server4 `/tmp`: 105989345280 available bytes; 94.09% used; 114349047 free inodes.

server4 `/var/tmp`: 105989345280 available bytes; 94.09% used; 114349047 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
