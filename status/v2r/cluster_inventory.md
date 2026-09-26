# V2R cluster inventory

2026-09-26T22:23:18.630381+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315471970304 available bytes; 82.40% used; 112445698 free inodes.

server1 `/home`: 315471970304 available bytes; 82.40% used; 112445698 free inodes.

server1 `/tmp`: 315471970304 available bytes; 82.40% used; 112445698 free inodes.

server1 `/var/tmp`: 315471970304 available bytes; 82.40% used; 112445698 free inodes.

server1 `/mnt/raid5`: 645853028352 available bytes; 97.04% used; 337467238 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17941745664 available bytes; 99.00% used; 110367509 free inodes.

server2 `/home`: 17941745664 available bytes; 99.00% used; 110367509 free inodes.

server2 `/tmp`: 17941745664 available bytes; 99.00% used; 110367509 free inodes.

server2 `/var/tmp`: 17941745664 available bytes; 99.00% used; 110367509 free inodes.

server2 `/mnt/raid5`: 597266624512 available bytes; 95.87% used; 444961419 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81083768832 available bytes; 95.48% used; 114069871 free inodes.

server3 `/home`: 81083768832 available bytes; 95.48% used; 114069871 free inodes.

server3 `/data`: 1349252399104 available bytes; 81.35% used; 225827116 free inodes.

server3 `/tmp`: 81083768832 available bytes; 95.48% used; 114069871 free inodes.

server3 `/var/tmp`: 81083768832 available bytes; 95.48% used; 114069871 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105899376640 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105899376640 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409643540480 available bytes; 94.34% used; 224823833 free inodes.

server4 `/tmp`: 105899376640 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105899376640 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
