# V2R cluster inventory

2026-09-23T19:07:44.049307+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325755564032 available bytes; 81.83% used; 112501849 free inodes.

server1 `/home`: 325755564032 available bytes; 81.83% used; 112501849 free inodes.

server1 `/tmp`: 325755564032 available bytes; 81.83% used; 112501849 free inodes.

server1 `/var/tmp`: 325755564032 available bytes; 81.83% used; 112501849 free inodes.

server1 `/mnt/raid5`: 1372418543616 available bytes; 93.70% used; 337741420 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41338220544 available bytes; 97.69% used; 110435436 free inodes.

server2 `/home`: 41338220544 available bytes; 97.69% used; 110435436 free inodes.

server2 `/tmp`: 41338220544 available bytes; 97.69% used; 110435436 free inodes.

server2 `/var/tmp`: 41338220544 available bytes; 97.69% used; 110435436 free inodes.

server2 `/mnt/raid5`: 543814234112 available bytes; 96.24% used; 445213191 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293625253888 available bytes; 83.61% used; 114236832 free inodes.

server3 `/home`: 293625253888 available bytes; 83.61% used; 114236832 free inodes.

server3 `/data`: 52777377792 available bytes; 99.27% used; 225845929 free inodes.

server3 `/tmp`: 293625253888 available bytes; 83.61% used; 114236832 free inodes.

server3 `/var/tmp`: 293625253888 available bytes; 83.61% used; 114236832 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106475376640 available bytes; 94.06% used; 114356232 free inodes.

server4 `/home`: 106475376640 available bytes; 94.06% used; 114356232 free inodes.

server4 `/data`: 13242368 available bytes; 100.00% used; 225457663 free inodes.

server4 `/tmp`: 106475376640 available bytes; 94.06% used; 114356232 free inodes.

server4 `/var/tmp`: 106475376640 available bytes; 94.06% used; 114356232 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
