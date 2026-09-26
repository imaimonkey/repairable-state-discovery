# V2R cluster inventory

2026-09-26T11:06:15.052749+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318213414912 available bytes; 82.25% used; 112474835 free inodes.

server1 `/home`: 318213414912 available bytes; 82.25% used; 112474835 free inodes.

server1 `/tmp`: 318213414912 available bytes; 82.25% used; 112474835 free inodes.

server1 `/var/tmp`: 318213414912 available bytes; 82.25% used; 112474835 free inodes.

server1 `/mnt/raid5`: 218749218816 available bytes; 99.00% used; 337538189 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19848855552 available bytes; 98.89% used; 110384895 free inodes.

server2 `/home`: 19848855552 available bytes; 98.89% used; 110384895 free inodes.

server2 `/tmp`: 19848855552 available bytes; 98.89% used; 110384895 free inodes.

server2 `/var/tmp`: 19848855552 available bytes; 98.89% used; 110384895 free inodes.

server2 `/mnt/raid5`: 242137223168 available bytes; 98.33% used; 444978883 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82649927680 available bytes; 95.39% used; 114110823 free inodes.

server3 `/home`: 82649927680 available bytes; 95.39% used; 114110823 free inodes.

server3 `/data`: 123563802624 available bytes; 98.29% used; 225825913 free inodes.

server3 `/tmp`: 82649927680 available bytes; 95.39% used; 114110823 free inodes.

server3 `/var/tmp`: 82649927680 available bytes; 95.39% used; 114110823 free inodes.
| server4 | True | ['3', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105926463488 available bytes; 94.09% used; 114347959 free inodes.

server4 `/home`: 105926463488 available bytes; 94.09% used; 114347959 free inodes.

server4 `/data`: 88883179520 available bytes; 98.77% used; 224880520 free inodes.

server4 `/tmp`: 105926463488 available bytes; 94.09% used; 114347959 free inodes.

server4 `/var/tmp`: 105926463488 available bytes; 94.09% used; 114347959 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
