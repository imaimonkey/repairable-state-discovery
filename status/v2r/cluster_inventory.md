# V2R cluster inventory

2026-09-24T06:59:55.782120+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324484624384 available bytes; 81.90% used; 112491379 free inodes.

server1 `/home`: 324484624384 available bytes; 81.90% used; 112491379 free inodes.

server1 `/tmp`: 324484624384 available bytes; 81.90% used; 112491379 free inodes.

server1 `/var/tmp`: 324484624384 available bytes; 81.90% used; 112491379 free inodes.

server1 `/mnt/raid5`: 517423394816 available bytes; 97.63% used; 337722846 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57863360512 available bytes; 96.77% used; 110431183 free inodes.

server2 `/home`: 57863360512 available bytes; 96.77% used; 110431183 free inodes.

server2 `/tmp`: 57863360512 available bytes; 96.77% used; 110431183 free inodes.

server2 `/var/tmp`: 57863360512 available bytes; 96.77% used; 110431183 free inodes.

server2 `/mnt/raid5`: 519334821888 available bytes; 96.41% used; 445190987 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126757076992 available bytes; 92.93% used; 114175148 free inodes.

server3 `/home`: 126757076992 available bytes; 92.93% used; 114175148 free inodes.

server3 `/data`: 139210850304 available bytes; 98.08% used; 225834770 free inodes.

server3 `/tmp`: 126757076992 available bytes; 92.93% used; 114175148 free inodes.

server3 `/var/tmp`: 126757076992 available bytes; 92.93% used; 114175148 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105798819840 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105798819840 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 303891951616 available bytes; 95.80% used; 225367778 free inodes.

server4 `/tmp`: 105798819840 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105798819840 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
