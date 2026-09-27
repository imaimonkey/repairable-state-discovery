# V2R cluster inventory

2026-09-27T15:26:49.405671+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304745582592 available bytes; 83.00% used; 112401390 free inodes.

server1 `/home`: 304745582592 available bytes; 83.00% used; 112401390 free inodes.

server1 `/tmp`: 304745582592 available bytes; 83.00% used; 112401390 free inodes.

server1 `/var/tmp`: 304745582592 available bytes; 83.00% used; 112401390 free inodes.

server1 `/mnt/raid5`: 626090811392 available bytes; 97.13% used; 337423995 free inodes.
| server2 | True | ['5', '6', '7'] | [] |

server2 `/`: 13396500480 available bytes; 99.25% used; 110351756 free inodes.

server2 `/home`: 13396500480 available bytes; 99.25% used; 110351756 free inodes.

server2 `/tmp`: 13396500480 available bytes; 99.25% used; 110351756 free inodes.

server2 `/var/tmp`: 13396500480 available bytes; 99.25% used; 110351756 free inodes.

server2 `/mnt/raid5`: 524009734144 available bytes; 96.38% used; 444720764 free inodes.
| server3 | True | ['0', '1', '2'] | [] |

server3 `/`: 78559137792 available bytes; 95.62% used; 114062768 free inodes.

server3 `/home`: 78559137792 available bytes; 95.62% used; 114062768 free inodes.

server3 `/data`: 1326819106816 available bytes; 81.66% used; 225762654 free inodes.

server3 `/tmp`: 78559137792 available bytes; 95.62% used; 114062768 free inodes.

server3 `/var/tmp`: 78559137792 available bytes; 95.62% used; 114062768 free inodes.
| server4 | True | ['1', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 108536446976 available bytes; 93.94% used; 114372705 free inodes.

server4 `/home`: 108536446976 available bytes; 93.94% used; 114372705 free inodes.

server4 `/data`: 350347636736 available bytes; 95.16% used; 224727086 free inodes.

server4 `/tmp`: 108536446976 available bytes; 93.94% used; 114372705 free inodes.

server4 `/var/tmp`: 108536446976 available bytes; 93.94% used; 114372705 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
