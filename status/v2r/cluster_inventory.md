# V2R cluster inventory

2026-09-26T09:37:45.014974+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318626807808 available bytes; 82.22% used; 112475085 free inodes.

server1 `/home`: 318626807808 available bytes; 82.22% used; 112475085 free inodes.

server1 `/tmp`: 318626807808 available bytes; 82.22% used; 112475085 free inodes.

server1 `/var/tmp`: 318626807808 available bytes; 82.22% used; 112475085 free inodes.

server1 `/mnt/raid5`: 218950889472 available bytes; 99.00% used; 337538603 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22314852352 available bytes; 98.76% used; 110403894 free inodes.

server2 `/home`: 22314852352 available bytes; 98.76% used; 110403894 free inodes.

server2 `/tmp`: 22314852352 available bytes; 98.76% used; 110403894 free inodes.

server2 `/var/tmp`: 22314852352 available bytes; 98.76% used; 110403894 free inodes.

server2 `/mnt/raid5`: 253976657920 available bytes; 98.25% used; 445022676 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82656354304 available bytes; 95.39% used; 114110791 free inodes.

server3 `/home`: 82656354304 available bytes; 95.39% used; 114110791 free inodes.

server3 `/data`: 123653066752 available bytes; 98.29% used; 225827677 free inodes.

server3 `/tmp`: 82656354304 available bytes; 95.39% used; 114110791 free inodes.

server3 `/var/tmp`: 82656354304 available bytes; 95.39% used; 114110791 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105942630400 available bytes; 94.09% used; 114348051 free inodes.

server4 `/home`: 105942630400 available bytes; 94.09% used; 114348051 free inodes.

server4 `/data`: 89283555328 available bytes; 98.77% used; 224882693 free inodes.

server4 `/tmp`: 105942630400 available bytes; 94.09% used; 114348051 free inodes.

server4 `/var/tmp`: 105942630400 available bytes; 94.09% used; 114348051 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
