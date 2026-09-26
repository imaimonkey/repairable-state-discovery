# V2R cluster inventory

2026-09-26T22:49:13.890498+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315469201408 available bytes; 82.40% used; 112445698 free inodes.

server1 `/home`: 315469201408 available bytes; 82.40% used; 112445698 free inodes.

server1 `/tmp`: 315469201408 available bytes; 82.40% used; 112445698 free inodes.

server1 `/var/tmp`: 315469201408 available bytes; 82.40% used; 112445698 free inodes.

server1 `/mnt/raid5`: 645835472896 available bytes; 97.04% used; 337467223 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17948053504 available bytes; 99.00% used; 110367507 free inodes.

server2 `/home`: 17948053504 available bytes; 99.00% used; 110367507 free inodes.

server2 `/tmp`: 17948053504 available bytes; 99.00% used; 110367507 free inodes.

server2 `/var/tmp`: 17948053504 available bytes; 99.00% used; 110367507 free inodes.

server2 `/mnt/raid5`: 596522655744 available bytes; 95.88% used; 444960708 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 81083858944 available bytes; 95.48% used; 114069879 free inodes.

server3 `/home`: 81083858944 available bytes; 95.48% used; 114069879 free inodes.

server3 `/data`: 1349240287232 available bytes; 81.35% used; 225826828 free inodes.

server3 `/tmp`: 81083858944 available bytes; 95.48% used; 114069879 free inodes.

server3 `/var/tmp`: 81083858944 available bytes; 95.48% used; 114069879 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898725376 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105898725376 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409623261184 available bytes; 94.34% used; 224823835 free inodes.

server4 `/tmp`: 105898725376 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105898725376 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
