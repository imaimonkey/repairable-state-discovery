# V2R cluster inventory

2026-09-27T00:37:27.985416+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315153498112 available bytes; 82.42% used; 112443467 free inodes.

server1 `/home`: 315153498112 available bytes; 82.42% used; 112443467 free inodes.

server1 `/tmp`: 315153498112 available bytes; 82.42% used; 112443467 free inodes.

server1 `/var/tmp`: 315153498112 available bytes; 82.42% used; 112443467 free inodes.

server1 `/mnt/raid5`: 637680205824 available bytes; 97.07% used; 337407670 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17624440832 available bytes; 99.02% used; 110365008 free inodes.

server2 `/home`: 17624440832 available bytes; 99.02% used; 110365008 free inodes.

server2 `/tmp`: 17624440832 available bytes; 99.02% used; 110365008 free inodes.

server2 `/var/tmp`: 17624440832 available bytes; 99.02% used; 110365008 free inodes.

server2 `/mnt/raid5`: 592999702528 available bytes; 95.90% used; 444956935 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 78491332608 available bytes; 95.62% used; 114068611 free inodes.

server3 `/home`: 78491332608 available bytes; 95.62% used; 114068611 free inodes.

server3 `/data`: 1349108318208 available bytes; 81.35% used; 225825489 free inodes.

server3 `/tmp`: 78491332608 available bytes; 95.62% used; 114068611 free inodes.

server3 `/var/tmp`: 78491332608 available bytes; 95.62% used; 114068611 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105879142400 available bytes; 94.09% used; 114347836 free inodes.

server4 `/home`: 105879142400 available bytes; 94.09% used; 114347836 free inodes.

server4 `/data`: 409208483840 available bytes; 94.34% used; 224820613 free inodes.

server4 `/tmp`: 105879142400 available bytes; 94.09% used; 114347836 free inodes.

server4 `/var/tmp`: 105879142400 available bytes; 94.09% used; 114347836 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
