# V2R cluster inventory

2026-09-26T10:50:59.485099+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318213566464 available bytes; 82.25% used; 112474817 free inodes.

server1 `/home`: 318213566464 available bytes; 82.25% used; 112474817 free inodes.

server1 `/tmp`: 318213566464 available bytes; 82.25% used; 112474817 free inodes.

server1 `/var/tmp`: 318213566464 available bytes; 82.25% used; 112474817 free inodes.

server1 `/mnt/raid5`: 218784587776 available bytes; 99.00% used; 337538261 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19845238784 available bytes; 98.89% used; 110384887 free inodes.

server2 `/home`: 19845238784 available bytes; 98.89% used; 110384887 free inodes.

server2 `/tmp`: 19845238784 available bytes; 98.89% used; 110384887 free inodes.

server2 `/var/tmp`: 19845238784 available bytes; 98.89% used; 110384887 free inodes.

server2 `/mnt/raid5`: 242574581760 available bytes; 98.32% used; 444978736 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82658254848 available bytes; 95.39% used; 114110823 free inodes.

server3 `/home`: 82658254848 available bytes; 95.39% used; 114110823 free inodes.

server3 `/data`: 123571499008 available bytes; 98.29% used; 225826181 free inodes.

server3 `/tmp`: 82658254848 available bytes; 95.39% used; 114110823 free inodes.

server3 `/var/tmp`: 82658254848 available bytes; 95.39% used; 114110823 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105926942720 available bytes; 94.09% used; 114347976 free inodes.

server4 `/home`: 105926942720 available bytes; 94.09% used; 114347976 free inodes.

server4 `/data`: 89060687872 available bytes; 98.77% used; 224880605 free inodes.

server4 `/tmp`: 105926942720 available bytes; 94.09% used; 114347976 free inodes.

server4 `/var/tmp`: 105926942720 available bytes; 94.09% used; 114347976 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
