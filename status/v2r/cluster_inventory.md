# V2R cluster inventory

2026-09-24T07:54:24.129901+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324417785856 available bytes; 81.90% used; 112490819 free inodes.

server1 `/home`: 324417785856 available bytes; 81.90% used; 112490819 free inodes.

server1 `/tmp`: 324417785856 available bytes; 81.90% used; 112490819 free inodes.

server1 `/var/tmp`: 324417785856 available bytes; 81.90% used; 112490819 free inodes.

server1 `/mnt/raid5`: 509483700224 available bytes; 97.66% used; 337722392 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57829654528 available bytes; 96.77% used; 110431088 free inodes.

server2 `/home`: 57829654528 available bytes; 96.77% used; 110431088 free inodes.

server2 `/tmp`: 57829654528 available bytes; 96.77% used; 110431088 free inodes.

server2 `/var/tmp`: 57829654528 available bytes; 96.77% used; 110431088 free inodes.

server2 `/mnt/raid5`: 517549424640 available bytes; 96.42% used; 445180744 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85547675648 available bytes; 95.23% used; 114184933 free inodes.

server3 `/home`: 85547675648 available bytes; 95.23% used; 114184933 free inodes.

server3 `/data`: 177882497024 available bytes; 97.54% used; 225839091 free inodes.

server3 `/tmp`: 85547675648 available bytes; 95.23% used; 114184933 free inodes.

server3 `/var/tmp`: 85547675648 available bytes; 95.23% used; 114184933 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779609600 available bytes; 94.10% used; 114349171 free inodes.

server4 `/home`: 105779609600 available bytes; 94.10% used; 114349171 free inodes.

server4 `/data`: 284238876672 available bytes; 96.07% used; 225366086 free inodes.

server4 `/tmp`: 105779609600 available bytes; 94.10% used; 114349171 free inodes.

server4 `/var/tmp`: 105779609600 available bytes; 94.10% used; 114349171 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
