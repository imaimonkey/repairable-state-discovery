# V2R cluster inventory

2026-09-24T01:22:00.842927+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325469347840 available bytes; 81.84% used; 112499783 free inodes.

server1 `/home`: 325469347840 available bytes; 81.84% used; 112499783 free inodes.

server1 `/tmp`: 325469347840 available bytes; 81.84% used; 112499783 free inodes.

server1 `/var/tmp`: 325469347840 available bytes; 81.84% used; 112499783 free inodes.

server1 `/mnt/raid5`: 929868173312 available bytes; 95.73% used; 337734032 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40953290752 available bytes; 97.72% used; 110432061 free inodes.

server2 `/home`: 40953290752 available bytes; 97.72% used; 110432061 free inodes.

server2 `/tmp`: 40953290752 available bytes; 97.72% used; 110432061 free inodes.

server2 `/var/tmp`: 40953290752 available bytes; 97.72% used; 110432061 free inodes.

server2 `/mnt/raid5`: 531210661888 available bytes; 96.33% used; 445201982 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292347211776 available bytes; 83.69% used; 114187465 free inodes.

server3 `/home`: 292347211776 available bytes; 83.69% used; 114187465 free inodes.

server3 `/data`: 82050461696 available bytes; 98.87% used; 225842428 free inodes.

server3 `/tmp`: 292347211776 available bytes; 83.69% used; 114187465 free inodes.

server3 `/var/tmp`: 292347211776 available bytes; 83.69% used; 114187465 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105976201216 available bytes; 94.09% used; 114348968 free inodes.

server4 `/home`: 105976201216 available bytes; 94.09% used; 114348968 free inodes.

server4 `/data`: 290827833344 available bytes; 95.98% used; 225396988 free inodes.

server4 `/tmp`: 105976201216 available bytes; 94.09% used; 114348968 free inodes.

server4 `/var/tmp`: 105976201216 available bytes; 94.09% used; 114348968 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
