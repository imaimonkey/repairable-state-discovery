# V2R cluster inventory

2026-09-24T05:46:49.501731+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324525158400 available bytes; 81.90% used; 112492088 free inodes.

server1 `/home`: 324525158400 available bytes; 81.90% used; 112492088 free inodes.

server1 `/tmp`: 324525158400 available bytes; 81.90% used; 112492088 free inodes.

server1 `/var/tmp`: 324525158400 available bytes; 81.90% used; 112492088 free inodes.

server1 `/mnt/raid5`: 517613015040 available bytes; 97.63% used; 337723919 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57908006912 available bytes; 96.77% used; 110431326 free inodes.

server2 `/home`: 57908006912 available bytes; 96.77% used; 110431326 free inodes.

server2 `/tmp`: 57908006912 available bytes; 96.77% used; 110431326 free inodes.

server2 `/var/tmp`: 57908006912 available bytes; 96.77% used; 110431326 free inodes.

server2 `/mnt/raid5`: 521861722112 available bytes; 96.39% used; 445193373 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126604365824 available bytes; 92.94% used; 114167649 free inodes.

server3 `/home`: 126604365824 available bytes; 92.94% used; 114167649 free inodes.

server3 `/data`: 185221189632 available bytes; 97.44% used; 225838690 free inodes.

server3 `/tmp`: 126604365824 available bytes; 92.94% used; 114167649 free inodes.

server3 `/var/tmp`: 126604365824 available bytes; 92.94% used; 114167649 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816133632 available bytes; 94.10% used; 114349347 free inodes.

server4 `/home`: 105816133632 available bytes; 94.10% used; 114349347 free inodes.

server4 `/data`: 251479957504 available bytes; 96.52% used; 225358005 free inodes.

server4 `/tmp`: 105816133632 available bytes; 94.10% used; 114349347 free inodes.

server4 `/var/tmp`: 105816133632 available bytes; 94.10% used; 114349347 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
