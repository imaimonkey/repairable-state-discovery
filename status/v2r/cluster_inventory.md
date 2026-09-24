# V2R cluster inventory

2026-09-24T21:17:22.686603+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323962073088 available bytes; 81.93% used; 112481400 free inodes.

server1 `/home`: 323962073088 available bytes; 81.93% used; 112481400 free inodes.

server1 `/tmp`: 323962073088 available bytes; 81.93% used; 112481400 free inodes.

server1 `/var/tmp`: 323962073088 available bytes; 81.93% used; 112481400 free inodes.

server1 `/mnt/raid5`: 415529820160 available bytes; 98.09% used; 337628950 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30136455168 available bytes; 98.32% used; 110411364 free inodes.

server2 `/home`: 30136455168 available bytes; 98.32% used; 110411364 free inodes.

server2 `/tmp`: 30136455168 available bytes; 98.32% used; 110411364 free inodes.

server2 `/var/tmp`: 30136455168 available bytes; 98.32% used; 110411364 free inodes.

server2 `/mnt/raid5`: 490807451648 available bytes; 96.61% used; 445155623 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84383469568 available bytes; 95.29% used; 114156095 free inodes.

server3 `/home`: 84383469568 available bytes; 95.29% used; 114156095 free inodes.

server3 `/data`: 150521614336 available bytes; 97.92% used; 225803412 free inodes.

server3 `/tmp`: 84383469568 available bytes; 95.29% used; 114156095 free inodes.

server3 `/var/tmp`: 84383469568 available bytes; 95.29% used; 114156095 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632518144 available bytes; 94.11% used; 114348350 free inodes.

server4 `/home`: 105632518144 available bytes; 94.11% used; 114348350 free inodes.

server4 `/data`: 71139065856 available bytes; 99.02% used; 225253475 free inodes.

server4 `/tmp`: 105632518144 available bytes; 94.11% used; 114348350 free inodes.

server4 `/var/tmp`: 105632518144 available bytes; 94.11% used; 114348350 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
