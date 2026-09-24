# V2R cluster inventory

2026-09-24T06:10:15.690236+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324523868160 available bytes; 81.90% used; 112491840 free inodes.

server1 `/home`: 324523868160 available bytes; 81.90% used; 112491840 free inodes.

server1 `/tmp`: 324523868160 available bytes; 81.90% used; 112491840 free inodes.

server1 `/var/tmp`: 324523868160 available bytes; 81.90% used; 112491840 free inodes.

server1 `/mnt/raid5`: 517602131968 available bytes; 97.63% used; 337723796 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57895673856 available bytes; 96.77% used; 110431272 free inodes.

server2 `/home`: 57895673856 available bytes; 96.77% used; 110431272 free inodes.

server2 `/tmp`: 57895673856 available bytes; 96.77% used; 110431272 free inodes.

server2 `/var/tmp`: 57895673856 available bytes; 96.77% used; 110431272 free inodes.

server2 `/mnt/raid5`: 520858042368 available bytes; 96.40% used; 445192661 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126844059648 available bytes; 92.92% used; 114180345 free inodes.

server3 `/home`: 126844059648 available bytes; 92.92% used; 114180345 free inodes.

server3 `/data`: 161312292864 available bytes; 97.77% used; 225836130 free inodes.

server3 `/tmp`: 126844059648 available bytes; 92.92% used; 114180345 free inodes.

server3 `/var/tmp`: 126844059648 available bytes; 92.92% used; 114180345 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105814953984 available bytes; 94.10% used; 114349319 free inodes.

server4 `/home`: 105814953984 available bytes; 94.10% used; 114349319 free inodes.

server4 `/data`: 339782025216 available bytes; 95.30% used; 225374146 free inodes.

server4 `/tmp`: 105814953984 available bytes; 94.10% used; 114349319 free inodes.

server4 `/var/tmp`: 105814953984 available bytes; 94.10% used; 114349319 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
