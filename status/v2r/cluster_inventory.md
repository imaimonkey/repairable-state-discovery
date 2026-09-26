# V2R cluster inventory

2026-09-26T21:49:46.642774+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315480952832 available bytes; 82.40% used; 112445679 free inodes.

server1 `/home`: 315480952832 available bytes; 82.40% used; 112445679 free inodes.

server1 `/tmp`: 315480952832 available bytes; 82.40% used; 112445679 free inodes.

server1 `/var/tmp`: 315480952832 available bytes; 82.40% used; 112445679 free inodes.

server1 `/mnt/raid5`: 645855481856 available bytes; 97.04% used; 337467239 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17942044672 available bytes; 99.00% used; 110367511 free inodes.

server2 `/home`: 17942044672 available bytes; 99.00% used; 110367511 free inodes.

server2 `/tmp`: 17942044672 available bytes; 99.00% used; 110367511 free inodes.

server2 `/var/tmp`: 17942044672 available bytes; 99.00% used; 110367511 free inodes.

server2 `/mnt/raid5`: 598223511552 available bytes; 95.87% used; 444962602 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81082134528 available bytes; 95.48% used; 114069853 free inodes.

server3 `/home`: 81082134528 available bytes; 95.48% used; 114069853 free inodes.

server3 `/data`: 1349618896896 available bytes; 81.35% used; 225827492 free inodes.

server3 `/tmp`: 81082134528 available bytes; 95.48% used; 114069853 free inodes.

server3 `/var/tmp`: 81082134528 available bytes; 95.48% used; 114069853 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105900236800 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105900236800 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409665523712 available bytes; 94.34% used; 224823823 free inodes.

server4 `/tmp`: 105900236800 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105900236800 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
