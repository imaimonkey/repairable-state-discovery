# V2R cluster inventory

2026-09-24T06:20:41.893902+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324513927168 available bytes; 81.90% used; 112491748 free inodes.

server1 `/home`: 324513927168 available bytes; 81.90% used; 112491748 free inodes.

server1 `/tmp`: 324513927168 available bytes; 81.90% used; 112491748 free inodes.

server1 `/var/tmp`: 324513927168 available bytes; 81.90% used; 112491748 free inodes.

server1 `/mnt/raid5`: 517575409664 available bytes; 97.63% used; 337723766 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57885773824 available bytes; 96.77% used; 110431235 free inodes.

server2 `/home`: 57885773824 available bytes; 96.77% used; 110431235 free inodes.

server2 `/tmp`: 57885773824 available bytes; 96.77% used; 110431235 free inodes.

server2 `/var/tmp`: 57885773824 available bytes; 96.77% used; 110431235 free inodes.

server2 `/mnt/raid5`: 520531148800 available bytes; 96.40% used; 445192125 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127167287296 available bytes; 92.90% used; 114196698 free inodes.

server3 `/home`: 127167287296 available bytes; 92.90% used; 114196698 free inodes.

server3 `/data`: 140586455040 available bytes; 98.06% used; 225835943 free inodes.

server3 `/tmp`: 127167287296 available bytes; 92.90% used; 114196698 free inodes.

server3 `/var/tmp`: 127167287296 available bytes; 92.90% used; 114196698 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105805926400 available bytes; 94.10% used; 114349291 free inodes.

server4 `/home`: 105805926400 available bytes; 94.10% used; 114349291 free inodes.

server4 `/data`: 335075627008 available bytes; 95.37% used; 225373559 free inodes.

server4 `/tmp`: 105805926400 available bytes; 94.10% used; 114349291 free inodes.

server4 `/var/tmp`: 105805926400 available bytes; 94.10% used; 114349291 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
