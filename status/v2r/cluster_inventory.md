# V2R cluster inventory

2026-09-24T04:03:34.727059+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324720144384 available bytes; 81.89% used; 112493501 free inodes.

server1 `/home`: 324720144384 available bytes; 81.89% used; 112493501 free inodes.

server1 `/tmp`: 324720144384 available bytes; 81.89% used; 112493501 free inodes.

server1 `/var/tmp`: 324720144384 available bytes; 81.89% used; 112493501 free inodes.

server1 `/mnt/raid5`: 416632651776 available bytes; 98.09% used; 337724774 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40804589568 available bytes; 97.72% used; 110430852 free inodes.

server2 `/home`: 40804589568 available bytes; 97.72% used; 110430852 free inodes.

server2 `/tmp`: 40804589568 available bytes; 97.72% used; 110430852 free inodes.

server2 `/var/tmp`: 40804589568 available bytes; 97.72% used; 110430852 free inodes.

server2 `/mnt/raid5`: 525645676544 available bytes; 96.37% used; 445196767 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 291919745024 available bytes; 83.71% used; 114174670 free inodes.

server3 `/home`: 291919745024 available bytes; 83.71% used; 114174670 free inodes.

server3 `/data`: 31743250432 available bytes; 99.56% used; 225841988 free inodes.

server3 `/tmp`: 291919745024 available bytes; 83.71% used; 114174670 free inodes.

server3 `/var/tmp`: 291919745024 available bytes; 83.71% used; 114174670 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105791201280 available bytes; 94.10% used; 114349500 free inodes.

server4 `/home`: 105791201280 available bytes; 94.10% used; 114349500 free inodes.

server4 `/data`: 256728195072 available bytes; 96.45% used; 225381892 free inodes.

server4 `/tmp`: 105791201280 available bytes; 94.10% used; 114349500 free inodes.

server4 `/var/tmp`: 105791201280 available bytes; 94.10% used; 114349500 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
