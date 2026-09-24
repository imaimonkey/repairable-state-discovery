# V2R cluster inventory

2026-09-24T23:13:00.474167+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319573753856 available bytes; 82.17% used; 112480827 free inodes.

server1 `/home`: 319573753856 available bytes; 82.17% used; 112480827 free inodes.

server1 `/tmp`: 319573753856 available bytes; 82.17% used; 112480827 free inodes.

server1 `/var/tmp`: 319573753856 available bytes; 82.17% used; 112480827 free inodes.

server1 `/mnt/raid5`: 415272001536 available bytes; 98.10% used; 337615206 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23120908288 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23120908288 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23120908288 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23120908288 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 487215529984 available bytes; 96.63% used; 445151897 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84371767296 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84371767296 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 148575473664 available bytes; 97.95% used; 225801250 free inodes.

server3 `/tmp`: 84371767296 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84371767296 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105800212480 available bytes; 94.10% used; 114348308 free inodes.

server4 `/home`: 105800212480 available bytes; 94.10% used; 114348308 free inodes.

server4 `/data`: 61771427840 available bytes; 99.15% used; 225172265 free inodes.

server4 `/tmp`: 105800212480 available bytes; 94.10% used; 114348308 free inodes.

server4 `/var/tmp`: 105800212480 available bytes; 94.10% used; 114348308 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
