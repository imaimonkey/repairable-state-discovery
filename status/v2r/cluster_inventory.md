# V2R cluster inventory

2026-09-26T07:03:38.547325+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318770069504 available bytes; 82.22% used; 112476291 free inodes.

server1 `/home`: 318770069504 available bytes; 82.22% used; 112476291 free inodes.

server1 `/tmp`: 318770069504 available bytes; 82.22% used; 112476291 free inodes.

server1 `/var/tmp`: 318770069504 available bytes; 82.22% used; 112476291 free inodes.

server1 `/mnt/raid5`: 219292504064 available bytes; 98.99% used; 337539373 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22316011520 available bytes; 98.76% used; 110403878 free inodes.

server2 `/home`: 22316011520 available bytes; 98.76% used; 110403878 free inodes.

server2 `/tmp`: 22316011520 available bytes; 98.76% used; 110403878 free inodes.

server2 `/var/tmp`: 22316011520 available bytes; 98.76% used; 110403878 free inodes.

server2 `/mnt/raid5`: 272018579456 available bytes; 98.12% used; 445027817 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82689105920 available bytes; 95.39% used; 114110895 free inodes.

server3 `/home`: 82689105920 available bytes; 95.39% used; 114110895 free inodes.

server3 `/data`: 123985039360 available bytes; 98.29% used; 225821545 free inodes.

server3 `/tmp`: 82689105920 available bytes; 95.39% used; 114110895 free inodes.

server3 `/var/tmp`: 82689105920 available bytes; 95.39% used; 114110895 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106075242496 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106075242496 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105882681344 available bytes; 98.54% used; 224922799 free inodes.

server4 `/tmp`: 106075242496 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106075242496 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
