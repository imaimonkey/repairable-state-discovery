# V2R cluster inventory

2026-09-24T03:54:03.281459+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324736094208 available bytes; 81.88% used; 112493642 free inodes.

server1 `/home`: 324736094208 available bytes; 81.88% used; 112493642 free inodes.

server1 `/tmp`: 324736094208 available bytes; 81.88% used; 112493642 free inodes.

server1 `/var/tmp`: 324736094208 available bytes; 81.88% used; 112493642 free inodes.

server1 `/mnt/raid5`: 411803754496 available bytes; 98.11% used; 337724793 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40816586752 available bytes; 97.72% used; 110430924 free inodes.

server2 `/home`: 40816586752 available bytes; 97.72% used; 110430924 free inodes.

server2 `/tmp`: 40816586752 available bytes; 97.72% used; 110430924 free inodes.

server2 `/var/tmp`: 40816586752 available bytes; 97.72% used; 110430924 free inodes.

server2 `/mnt/raid5`: 526484205568 available bytes; 96.36% used; 445196951 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292380078080 available bytes; 83.68% used; 114200341 free inodes.

server3 `/home`: 292380078080 available bytes; 83.68% used; 114200341 free inodes.

server3 `/data`: 33870270464 available bytes; 99.53% used; 225842508 free inodes.

server3 `/tmp`: 292380078080 available bytes; 83.68% used; 114200341 free inodes.

server3 `/var/tmp`: 292380078080 available bytes; 83.68% used; 114200341 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105791737856 available bytes; 94.10% used; 114349524 free inodes.

server4 `/home`: 105791737856 available bytes; 94.10% used; 114349524 free inodes.

server4 `/data`: 271551131648 available bytes; 96.25% used; 225383820 free inodes.

server4 `/tmp`: 105791737856 available bytes; 94.10% used; 114349524 free inodes.

server4 `/var/tmp`: 105791737856 available bytes; 94.10% used; 114349524 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
