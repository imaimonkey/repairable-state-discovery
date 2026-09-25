# V2R cluster inventory

2026-09-25T18:54:02.005838+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318740738048 available bytes; 82.22% used; 112476338 free inodes.

server1 `/home`: 318740738048 available bytes; 82.22% used; 112476338 free inodes.

server1 `/tmp`: 318740738048 available bytes; 82.22% used; 112476338 free inodes.

server1 `/var/tmp`: 318740738048 available bytes; 82.22% used; 112476338 free inodes.

server1 `/mnt/raid5`: 371146764288 available bytes; 98.30% used; 337541182 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23097237504 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23097237504 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23097237504 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23097237504 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 313276690432 available bytes; 97.84% used; 445065869 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84383461376 available bytes; 95.29% used; 114152623 free inodes.

server3 `/home`: 84383461376 available bytes; 95.29% used; 114152623 free inodes.

server3 `/data`: 131375480832 available bytes; 98.18% used; 225809248 free inodes.

server3 `/tmp`: 84383461376 available bytes; 95.29% used; 114152623 free inodes.

server3 `/var/tmp`: 84383461376 available bytes; 95.29% used; 114152623 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105606770688 available bytes; 94.11% used; 114349598 free inodes.

server4 `/home`: 105606770688 available bytes; 94.11% used; 114349598 free inodes.

server4 `/data`: 229689368576 available bytes; 96.83% used; 224931408 free inodes.

server4 `/tmp`: 105606770688 available bytes; 94.11% used; 114349598 free inodes.

server4 `/var/tmp`: 105606770688 available bytes; 94.11% used; 114349598 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
