# V2R cluster inventory

2026-09-25T08:19:51.017752+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318827532288 available bytes; 82.21% used; 112480360 free inodes.

server1 `/home`: 318827532288 available bytes; 82.21% used; 112480360 free inodes.

server1 `/tmp`: 318827532288 available bytes; 82.21% used; 112480360 free inodes.

server1 `/var/tmp`: 318827532288 available bytes; 82.21% used; 112480360 free inodes.

server1 `/mnt/raid5`: 374376337408 available bytes; 98.28% used; 337557371 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22833852416 available bytes; 98.73% used; 110410480 free inodes.

server2 `/home`: 22833852416 available bytes; 98.73% used; 110410480 free inodes.

server2 `/tmp`: 22833852416 available bytes; 98.73% used; 110410480 free inodes.

server2 `/var/tmp`: 22833852416 available bytes; 98.73% used; 110410480 free inodes.

server2 `/mnt/raid5`: 333601570816 available bytes; 97.69% used; 445094781 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84439003136 available bytes; 95.29% used; 114156051 free inodes.

server3 `/home`: 84439003136 available bytes; 95.29% used; 114156051 free inodes.

server3 `/data`: 142384435200 available bytes; 98.03% used; 225811856 free inodes.

server3 `/tmp`: 84439003136 available bytes; 95.29% used; 114156051 free inodes.

server3 `/var/tmp`: 84439003136 available bytes; 95.29% used; 114156051 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105624956928 available bytes; 94.11% used; 114350334 free inodes.

server4 `/home`: 105624956928 available bytes; 94.11% used; 114350334 free inodes.

server4 `/data`: 247739142144 available bytes; 96.58% used; 225006546 free inodes.

server4 `/tmp`: 105624956928 available bytes; 94.11% used; 114350334 free inodes.

server4 `/var/tmp`: 105624956928 available bytes; 94.11% used; 114350334 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
