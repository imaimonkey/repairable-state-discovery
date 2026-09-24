# V2R cluster inventory

2026-09-24T15:35:29.165908+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324020404224 available bytes; 81.92% used; 112481440 free inodes.

server1 `/home`: 324020404224 available bytes; 81.92% used; 112481440 free inodes.

server1 `/tmp`: 324020404224 available bytes; 81.92% used; 112481440 free inodes.

server1 `/var/tmp`: 324020404224 available bytes; 81.92% used; 112481440 free inodes.

server1 `/mnt/raid5`: 416749342720 available bytes; 98.09% used; 337660550 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57387716608 available bytes; 96.80% used; 110427447 free inodes.

server2 `/home`: 57387716608 available bytes; 96.80% used; 110427447 free inodes.

server2 `/tmp`: 57387716608 available bytes; 96.80% used; 110427447 free inodes.

server2 `/var/tmp`: 57387716608 available bytes; 96.80% used; 110427447 free inodes.

server2 `/mnt/raid5`: 502078447616 available bytes; 96.53% used; 445165820 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 84473729024 available bytes; 95.29% used; 114157052 free inodes.

server3 `/home`: 84473729024 available bytes; 95.29% used; 114157052 free inodes.

server3 `/data`: 160326000640 available bytes; 97.78% used; 225806458 free inodes.

server3 `/tmp`: 84473729024 available bytes; 95.29% used; 114157052 free inodes.

server3 `/var/tmp`: 84473729024 available bytes; 95.29% used; 114157052 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105716019200 available bytes; 94.10% used; 114348620 free inodes.

server4 `/home`: 105716019200 available bytes; 94.10% used; 114348620 free inodes.

server4 `/data`: 89388494848 available bytes; 98.76% used; 225256708 free inodes.

server4 `/tmp`: 105716019200 available bytes; 94.10% used; 114348620 free inodes.

server4 `/var/tmp`: 105716019200 available bytes; 94.10% used; 114348620 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
