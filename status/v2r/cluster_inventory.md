# V2R cluster inventory

2026-09-24T08:40:48.603126+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324392771584 available bytes; 81.90% used; 112490362 free inodes.

server1 `/home`: 324392771584 available bytes; 81.90% used; 112490362 free inodes.

server1 `/tmp`: 324392771584 available bytes; 81.90% used; 112490362 free inodes.

server1 `/var/tmp`: 324392771584 available bytes; 81.90% used; 112490362 free inodes.

server1 `/mnt/raid5`: 506234933248 available bytes; 97.68% used; 337719333 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57798549504 available bytes; 96.78% used; 110430970 free inodes.

server2 `/home`: 57798549504 available bytes; 96.78% used; 110430970 free inodes.

server2 `/tmp`: 57798549504 available bytes; 96.78% used; 110430970 free inodes.

server2 `/var/tmp`: 57798549504 available bytes; 96.78% used; 110430970 free inodes.

server2 `/mnt/raid5`: 515269316608 available bytes; 96.44% used; 445179054 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 85416271872 available bytes; 95.23% used; 114172135 free inodes.

server3 `/home`: 85416271872 available bytes; 95.23% used; 114172135 free inodes.

server3 `/data`: 173664800768 available bytes; 97.60% used; 225822326 free inodes.

server3 `/tmp`: 85416271872 available bytes; 95.23% used; 114172135 free inodes.

server3 `/var/tmp`: 85416271872 available bytes; 95.23% used; 114172135 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105768751104 available bytes; 94.10% used; 114349104 free inodes.

server4 `/home`: 105768751104 available bytes; 94.10% used; 114349104 free inodes.

server4 `/data`: 255371362304 available bytes; 96.47% used; 225288355 free inodes.

server4 `/tmp`: 105768751104 available bytes; 94.10% used; 114349104 free inodes.

server4 `/var/tmp`: 105768751104 available bytes; 94.10% used; 114349104 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
