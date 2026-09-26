# V2R cluster inventory

2026-09-26T19:33:41.188282+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315541676032 available bytes; 82.40% used; 112445150 free inodes.

server1 `/home`: 315541676032 available bytes; 82.40% used; 112445150 free inodes.

server1 `/tmp`: 315541676032 available bytes; 82.40% used; 112445150 free inodes.

server1 `/var/tmp`: 315541676032 available bytes; 82.40% used; 112445150 free inodes.

server1 `/mnt/raid5`: 645854572544 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18022895616 available bytes; 98.99% used; 110367537 free inodes.

server2 `/home`: 18022895616 available bytes; 98.99% used; 110367537 free inodes.

server2 `/tmp`: 18022895616 available bytes; 98.99% used; 110367537 free inodes.

server2 `/var/tmp`: 18022895616 available bytes; 98.99% used; 110367537 free inodes.

server2 `/mnt/raid5`: 602287448064 available bytes; 95.84% used; 444966476 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81268076544 available bytes; 95.46% used; 114065305 free inodes.

server3 `/home`: 81268076544 available bytes; 95.46% used; 114065305 free inodes.

server3 `/data`: 1349019267072 available bytes; 81.36% used; 225833779 free inodes.

server3 `/tmp`: 81268076544 available bytes; 95.46% used; 114065305 free inodes.

server3 `/var/tmp`: 81268076544 available bytes; 95.46% used; 114065305 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105920389120 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105920389120 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410304163840 available bytes; 94.33% used; 224824173 free inodes.

server4 `/tmp`: 105920389120 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105920389120 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
