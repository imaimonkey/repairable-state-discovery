# V2R cluster inventory

2026-09-24T01:18:55.053859+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325473017856 available bytes; 81.84% used; 112499829 free inodes.

server1 `/home`: 325473017856 available bytes; 81.84% used; 112499829 free inodes.

server1 `/tmp`: 325473017856 available bytes; 81.84% used; 112499829 free inodes.

server1 `/var/tmp`: 325473017856 available bytes; 81.84% used; 112499829 free inodes.

server1 `/mnt/raid5`: 942887776256 available bytes; 95.67% used; 337734081 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40953339904 available bytes; 97.72% used; 110432083 free inodes.

server2 `/home`: 40953339904 available bytes; 97.72% used; 110432083 free inodes.

server2 `/tmp`: 40953339904 available bytes; 97.72% used; 110432083 free inodes.

server2 `/var/tmp`: 40953339904 available bytes; 97.72% used; 110432083 free inodes.

server2 `/mnt/raid5`: 530771066880 available bytes; 96.33% used; 445202091 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292347764736 available bytes; 83.69% used; 114187477 free inodes.

server3 `/home`: 292347764736 available bytes; 83.69% used; 114187477 free inodes.

server3 `/data`: 82067714048 available bytes; 98.87% used; 225842551 free inodes.

server3 `/tmp`: 292347764736 available bytes; 83.69% used; 114187477 free inodes.

server3 `/var/tmp`: 292347764736 available bytes; 83.69% used; 114187477 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105988575232 available bytes; 94.09% used; 114349035 free inodes.

server4 `/home`: 105988575232 available bytes; 94.09% used; 114349035 free inodes.

server4 `/data`: 290842226688 available bytes; 95.98% used; 225397013 free inodes.

server4 `/tmp`: 105988575232 available bytes; 94.09% used; 114349035 free inodes.

server4 `/var/tmp`: 105988575232 available bytes; 94.09% used; 114349035 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
