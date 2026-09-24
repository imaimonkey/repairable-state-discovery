# V2R cluster inventory

2026-09-24T12:28:37.934028+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324055175168 available bytes; 81.92% used; 112481554 free inodes.

server1 `/home`: 324055175168 available bytes; 81.92% used; 112481554 free inodes.

server1 `/tmp`: 324055175168 available bytes; 81.92% used; 112481554 free inodes.

server1 `/var/tmp`: 324055175168 available bytes; 81.92% used; 112481554 free inodes.

server1 `/mnt/raid5`: 405189718016 available bytes; 98.14% used; 337682554 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57597022208 available bytes; 96.79% used; 110429417 free inodes.

server2 `/home`: 57597022208 available bytes; 96.79% used; 110429417 free inodes.

server2 `/tmp`: 57597022208 available bytes; 96.79% used; 110429417 free inodes.

server2 `/var/tmp`: 57597022208 available bytes; 96.79% used; 110429417 free inodes.

server2 `/mnt/raid5`: 508554543104 available bytes; 96.49% used; 445171637 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85719785472 available bytes; 95.22% used; 114197773 free inodes.

server3 `/home`: 85719785472 available bytes; 95.22% used; 114197773 free inodes.

server3 `/data`: 163348578304 available bytes; 97.74% used; 225814783 free inodes.

server3 `/tmp`: 85719785472 available bytes; 95.22% used; 114197773 free inodes.

server3 `/var/tmp`: 85719785472 available bytes; 95.22% used; 114197773 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105780662272 available bytes; 94.10% used; 114348793 free inodes.

server4 `/home`: 105780662272 available bytes; 94.10% used; 114348793 free inodes.

server4 `/data`: 90073993216 available bytes; 98.76% used; 225257250 free inodes.

server4 `/tmp`: 105780662272 available bytes; 94.10% used; 114348793 free inodes.

server4 `/var/tmp`: 105780662272 available bytes; 94.10% used; 114348793 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
