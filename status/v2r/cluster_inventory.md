# V2R cluster inventory

2026-09-24T03:04:10.462193+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325371088896 available bytes; 81.85% used; 112498498 free inodes.

server1 `/home`: 325371088896 available bytes; 81.85% used; 112498498 free inodes.

server1 `/tmp`: 325371088896 available bytes; 81.85% used; 112498498 free inodes.

server1 `/var/tmp`: 325371088896 available bytes; 81.85% used; 112498498 free inodes.

server1 `/mnt/raid5`: 499962126336 available bytes; 97.71% used; 337732353 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40860160000 available bytes; 97.72% used; 110431294 free inodes.

server2 `/home`: 40860160000 available bytes; 97.72% used; 110431294 free inodes.

server2 `/tmp`: 40860160000 available bytes; 97.72% used; 110431294 free inodes.

server2 `/var/tmp`: 40860160000 available bytes; 97.72% used; 110431294 free inodes.

server2 `/mnt/raid5`: 527937581056 available bytes; 96.35% used; 445198358 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292689018880 available bytes; 83.67% used; 114211014 free inodes.

server3 `/home`: 292689018880 available bytes; 83.67% used; 114211014 free inodes.

server3 `/data`: 39699623936 available bytes; 99.45% used; 225845287 free inodes.

server3 `/tmp`: 292689018880 available bytes; 83.67% used; 114211014 free inodes.

server3 `/var/tmp`: 292689018880 available bytes; 83.67% used; 114211014 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105988276224 available bytes; 94.09% used; 114349629 free inodes.

server4 `/home`: 105988276224 available bytes; 94.09% used; 114349629 free inodes.

server4 `/data`: 289711861760 available bytes; 96.00% used; 225386867 free inodes.

server4 `/tmp`: 105988276224 available bytes; 94.09% used; 114349629 free inodes.

server4 `/var/tmp`: 105988276224 available bytes; 94.09% used; 114349629 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
