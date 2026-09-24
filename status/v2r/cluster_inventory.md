# V2R cluster inventory

2026-09-24T19:09:13.409525+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323994017792 available bytes; 81.93% used; 112481464 free inodes.

server1 `/home`: 323994017792 available bytes; 81.93% used; 112481464 free inodes.

server1 `/tmp`: 323994017792 available bytes; 81.93% used; 112481464 free inodes.

server1 `/var/tmp`: 323994017792 available bytes; 81.93% used; 112481464 free inodes.

server1 `/mnt/raid5`: 416240807936 available bytes; 98.09% used; 337634826 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 54466097152 available bytes; 96.96% used; 110411923 free inodes.

server2 `/home`: 54466097152 available bytes; 96.96% used; 110411923 free inodes.

server2 `/tmp`: 54466097152 available bytes; 96.96% used; 110411923 free inodes.

server2 `/var/tmp`: 54466097152 available bytes; 96.96% used; 110411923 free inodes.

server2 `/mnt/raid5`: 495518294016 available bytes; 96.58% used; 445159553 free inodes.
| server3 | True | ['1'] | [] |

server3 `/`: 84406145024 available bytes; 95.29% used; 114156135 free inodes.

server3 `/home`: 84406145024 available bytes; 95.29% used; 114156135 free inodes.

server3 `/data`: 152453488640 available bytes; 97.89% used; 225799861 free inodes.

server3 `/tmp`: 84406145024 available bytes; 95.29% used; 114156135 free inodes.

server3 `/var/tmp`: 84406145024 available bytes; 95.29% used; 114156135 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105660743680 available bytes; 94.10% used; 114348475 free inodes.

server4 `/home`: 105660743680 available bytes; 94.10% used; 114348475 free inodes.

server4 `/data`: 89913466880 available bytes; 98.76% used; 225267260 free inodes.

server4 `/tmp`: 105660743680 available bytes; 94.10% used; 114348475 free inodes.

server4 `/var/tmp`: 105660743680 available bytes; 94.10% used; 114348475 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
