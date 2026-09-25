# V2R cluster inventory

2026-09-25T08:32:11.029871+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318825537536 available bytes; 82.21% used; 112480369 free inodes.

server1 `/home`: 318825537536 available bytes; 82.21% used; 112480369 free inodes.

server1 `/tmp`: 318825537536 available bytes; 82.21% used; 112480369 free inodes.

server1 `/var/tmp`: 318825537536 available bytes; 82.21% used; 112480369 free inodes.

server1 `/mnt/raid5`: 364226826240 available bytes; 98.33% used; 337557087 free inodes.
| server2 | True | ['5', '6'] | [] |

server2 `/`: 22843019264 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22843019264 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22843019264 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22843019264 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 333176672256 available bytes; 97.70% used; 445094139 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436447232 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84436447232 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142380765184 available bytes; 98.03% used; 225811645 free inodes.

server3 `/tmp`: 84436447232 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84436447232 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105634091008 available bytes; 94.11% used; 114350326 free inodes.

server4 `/home`: 105634091008 available bytes; 94.11% used; 114350326 free inodes.

server4 `/data`: 246707236864 available bytes; 96.59% used; 225003949 free inodes.

server4 `/tmp`: 105634091008 available bytes; 94.11% used; 114350326 free inodes.

server4 `/var/tmp`: 105634091008 available bytes; 94.11% used; 114350326 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
