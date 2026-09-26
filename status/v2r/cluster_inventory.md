# V2R cluster inventory

2026-09-26T02:07:24.966028+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318519676928 available bytes; 82.23% used; 112476292 free inodes.

server1 `/home`: 318519676928 available bytes; 82.23% used; 112476292 free inodes.

server1 `/tmp`: 318519676928 available bytes; 82.23% used; 112476292 free inodes.

server1 `/var/tmp`: 318519676928 available bytes; 82.23% used; 112476292 free inodes.

server1 `/mnt/raid5`: 345209905152 available bytes; 98.42% used; 337546267 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22942482432 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22942482432 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22942482432 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22942482432 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 289618313216 available bytes; 98.00% used; 445054738 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84326518784 available bytes; 95.29% used; 114152368 free inodes.

server3 `/home`: 84326518784 available bytes; 95.29% used; 114152368 free inodes.

server3 `/data`: 124792041472 available bytes; 98.28% used; 225817372 free inodes.

server3 `/tmp`: 84326518784 available bytes; 95.29% used; 114152368 free inodes.

server3 `/var/tmp`: 84326518784 available bytes; 95.29% used; 114152368 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105433571328 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105433571328 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130904612864 available bytes; 98.19% used; 224915754 free inodes.

server4 `/tmp`: 105433571328 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105433571328 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
