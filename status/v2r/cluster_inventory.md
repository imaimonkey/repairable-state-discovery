# V2R cluster inventory

2026-09-24T05:31:05.664629+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324548894720 available bytes; 81.89% used; 112492353 free inodes.

server1 `/home`: 324548894720 available bytes; 81.89% used; 112492353 free inodes.

server1 `/tmp`: 324548894720 available bytes; 81.89% used; 112492353 free inodes.

server1 `/var/tmp`: 324548894720 available bytes; 81.89% used; 112492353 free inodes.

server1 `/mnt/raid5`: 513757081600 available bytes; 97.64% used; 337724231 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57918824448 available bytes; 96.77% used; 110431368 free inodes.

server2 `/home`: 57918824448 available bytes; 96.77% used; 110431368 free inodes.

server2 `/tmp`: 57918824448 available bytes; 96.77% used; 110431368 free inodes.

server2 `/var/tmp`: 57918824448 available bytes; 96.77% used; 110431368 free inodes.

server2 `/mnt/raid5`: 522333237248 available bytes; 96.39% used; 445193577 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127198904320 available bytes; 92.90% used; 114197411 free inodes.

server3 `/home`: 127198904320 available bytes; 92.90% used; 114197411 free inodes.

server3 `/data`: 185274056704 available bytes; 97.44% used; 225839595 free inodes.

server3 `/tmp`: 127198904320 available bytes; 92.90% used; 114197411 free inodes.

server3 `/var/tmp`: 127198904320 available bytes; 92.90% used; 114197411 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816997888 available bytes; 94.10% used; 114349363 free inodes.

server4 `/home`: 105816997888 available bytes; 94.10% used; 114349363 free inodes.

server4 `/data`: 251531251712 available bytes; 96.52% used; 225358120 free inodes.

server4 `/tmp`: 105816997888 available bytes; 94.10% used; 114349363 free inodes.

server4 `/var/tmp`: 105816997888 available bytes; 94.10% used; 114349363 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
