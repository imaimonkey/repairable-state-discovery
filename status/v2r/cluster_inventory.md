# V2R cluster inventory

2026-09-26T01:49:05.552477+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318526390272 available bytes; 82.23% used; 112476285 free inodes.

server1 `/home`: 318526390272 available bytes; 82.23% used; 112476285 free inodes.

server1 `/tmp`: 318526390272 available bytes; 82.23% used; 112476285 free inodes.

server1 `/var/tmp`: 318526390272 available bytes; 82.23% used; 112476285 free inodes.

server1 `/mnt/raid5`: 345248821248 available bytes; 98.42% used; 337546347 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22937985024 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22937985024 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22937985024 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22937985024 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 290172952576 available bytes; 97.99% used; 445055550 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84325879808 available bytes; 95.29% used; 114152368 free inodes.

server3 `/home`: 84325879808 available bytes; 95.29% used; 114152368 free inodes.

server3 `/data`: 124794429440 available bytes; 98.28% used; 225817694 free inodes.

server3 `/tmp`: 84325879808 available bytes; 95.29% used; 114152368 free inodes.

server3 `/var/tmp`: 84325879808 available bytes; 95.29% used; 114152368 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105434083328 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105434083328 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130908536832 available bytes; 98.19% used; 224915776 free inodes.

server4 `/tmp`: 105434083328 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105434083328 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
