# V2R cluster inventory

2026-09-26T09:31:38.676719+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318626938880 available bytes; 82.22% used; 112475099 free inodes.

server1 `/home`: 318626938880 available bytes; 82.22% used; 112475099 free inodes.

server1 `/tmp`: 318626938880 available bytes; 82.22% used; 112475099 free inodes.

server1 `/var/tmp`: 318626938880 available bytes; 82.22% used; 112475099 free inodes.

server1 `/mnt/raid5`: 218965499904 available bytes; 99.00% used; 337538645 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22320496640 available bytes; 98.75% used; 110403910 free inodes.

server2 `/home`: 22320496640 available bytes; 98.75% used; 110403910 free inodes.

server2 `/tmp`: 22320496640 available bytes; 98.75% used; 110403910 free inodes.

server2 `/var/tmp`: 22320496640 available bytes; 98.75% used; 110403910 free inodes.

server2 `/mnt/raid5`: 254147891200 available bytes; 98.24% used; 445022737 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82661109760 available bytes; 95.39% used; 114110805 free inodes.

server3 `/home`: 82661109760 available bytes; 95.39% used; 114110805 free inodes.

server3 `/data`: 123657039872 available bytes; 98.29% used; 225827823 free inodes.

server3 `/tmp`: 82661109760 available bytes; 95.39% used; 114110805 free inodes.

server3 `/var/tmp`: 82661109760 available bytes; 95.39% used; 114110805 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105942802432 available bytes; 94.09% used; 114348053 free inodes.

server4 `/home`: 105942802432 available bytes; 94.09% used; 114348053 free inodes.

server4 `/data`: 89296482304 available bytes; 98.77% used; 224882762 free inodes.

server4 `/tmp`: 105942802432 available bytes; 94.09% used; 114348053 free inodes.

server4 `/var/tmp`: 105942802432 available bytes; 94.09% used; 114348053 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
