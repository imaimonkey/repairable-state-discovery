# V2R cluster inventory

2026-09-27T00:29:50.481932+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315155296256 available bytes; 82.42% used; 112443463 free inodes.

server1 `/home`: 315155296256 available bytes; 82.42% used; 112443463 free inodes.

server1 `/tmp`: 315155296256 available bytes; 82.42% used; 112443463 free inodes.

server1 `/var/tmp`: 315155296256 available bytes; 82.42% used; 112443463 free inodes.

server1 `/mnt/raid5`: 637687492608 available bytes; 97.07% used; 337407695 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17632686080 available bytes; 99.02% used; 110365019 free inodes.

server2 `/home`: 17632686080 available bytes; 99.02% used; 110365019 free inodes.

server2 `/tmp`: 17632686080 available bytes; 99.02% used; 110365019 free inodes.

server2 `/var/tmp`: 17632686080 available bytes; 99.02% used; 110365019 free inodes.

server2 `/mnt/raid5`: 592698204160 available bytes; 95.90% used; 444957281 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 77837889536 available bytes; 95.66% used; 114068608 free inodes.

server3 `/home`: 77837889536 available bytes; 95.66% used; 114068608 free inodes.

server3 `/data`: 1349105102848 available bytes; 81.35% used; 225825567 free inodes.

server3 `/tmp`: 77837889536 available bytes; 95.66% used; 114068608 free inodes.

server3 `/var/tmp`: 77837889536 available bytes; 95.66% used; 114068608 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105879355392 available bytes; 94.09% used; 114347844 free inodes.

server4 `/home`: 105879355392 available bytes; 94.09% used; 114347844 free inodes.

server4 `/data`: 409234010112 available bytes; 94.34% used; 224820677 free inodes.

server4 `/tmp`: 105879355392 available bytes; 94.09% used; 114347844 free inodes.

server4 `/var/tmp`: 105879355392 available bytes; 94.09% used; 114347844 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
