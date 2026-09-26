# V2R cluster inventory

2026-09-26T12:25:35.845711+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318179225600 available bytes; 82.25% used; 112474777 free inodes.

server1 `/home`: 318179225600 available bytes; 82.25% used; 112474777 free inodes.

server1 `/tmp`: 318179225600 available bytes; 82.25% used; 112474777 free inodes.

server1 `/var/tmp`: 318179225600 available bytes; 82.25% used; 112474777 free inodes.

server1 `/mnt/raid5`: 218559479808 available bytes; 99.00% used; 337537796 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19782361088 available bytes; 98.90% used; 110383620 free inodes.

server2 `/home`: 19782361088 available bytes; 98.90% used; 110383620 free inodes.

server2 `/tmp`: 19782361088 available bytes; 98.90% used; 110383620 free inodes.

server2 `/var/tmp`: 19782361088 available bytes; 98.90% used; 110383620 free inodes.

server2 `/mnt/raid5`: 240440770560 available bytes; 98.34% used; 444980409 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 82651660288 available bytes; 95.39% used; 114110841 free inodes.

server3 `/home`: 82651660288 available bytes; 95.39% used; 114110841 free inodes.

server3 `/data`: 123417837568 available bytes; 98.29% used; 225824153 free inodes.

server3 `/tmp`: 82651660288 available bytes; 95.39% used; 114110841 free inodes.

server3 `/var/tmp`: 82651660288 available bytes; 95.39% used; 114110841 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899839488 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105899839488 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88564793344 available bytes; 98.78% used; 224879167 free inodes.

server4 `/tmp`: 105899839488 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105899839488 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
