# V2R cluster inventory

2026-09-25T09:25:51.934311+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318837501952 available bytes; 82.21% used; 112480386 free inodes.

server1 `/home`: 318837501952 available bytes; 82.21% used; 112480386 free inodes.

server1 `/tmp`: 318837501952 available bytes; 82.21% used; 112480386 free inodes.

server1 `/var/tmp`: 318837501952 available bytes; 82.21% used; 112480386 free inodes.

server1 `/mnt/raid5`: 350389387264 available bytes; 98.39% used; 337556910 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22829834240 available bytes; 98.73% used; 110410486 free inodes.

server2 `/home`: 22829834240 available bytes; 98.73% used; 110410486 free inodes.

server2 `/tmp`: 22829834240 available bytes; 98.73% used; 110410486 free inodes.

server2 `/var/tmp`: 22829834240 available bytes; 98.73% used; 110410486 free inodes.

server2 `/mnt/raid5`: 331815546880 available bytes; 97.71% used; 445092916 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 84419072000 available bytes; 95.29% used; 114156055 free inodes.

server3 `/home`: 84419072000 available bytes; 95.29% used; 114156055 free inodes.

server3 `/data`: 142299828224 available bytes; 98.03% used; 225810727 free inodes.

server3 `/tmp`: 84419072000 available bytes; 95.29% used; 114156055 free inodes.

server3 `/var/tmp`: 84419072000 available bytes; 95.29% used; 114156055 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632272384 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105632272384 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 241738502144 available bytes; 96.66% used; 224996144 free inodes.

server4 `/tmp`: 105632272384 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105632272384 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
