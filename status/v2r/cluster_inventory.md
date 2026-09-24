# V2R cluster inventory

2026-09-24T02:44:40.413549+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325381537792 available bytes; 81.85% used; 112498724 free inodes.

server1 `/home`: 325381537792 available bytes; 81.85% used; 112498724 free inodes.

server1 `/tmp`: 325381537792 available bytes; 81.85% used; 112498724 free inodes.

server1 `/var/tmp`: 325381537792 available bytes; 81.85% used; 112498724 free inodes.

server1 `/mnt/raid5`: 585395113984 available bytes; 97.31% used; 337733172 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40877015040 available bytes; 97.72% used; 110431434 free inodes.

server2 `/home`: 40877015040 available bytes; 97.72% used; 110431434 free inodes.

server2 `/tmp`: 40877015040 available bytes; 97.72% used; 110431434 free inodes.

server2 `/var/tmp`: 40877015040 available bytes; 97.72% used; 110431434 free inodes.

server2 `/mnt/raid5`: 528552513536 available bytes; 96.35% used; 445198979 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292684013568 available bytes; 83.67% used; 114210223 free inodes.

server3 `/home`: 292684013568 available bytes; 83.67% used; 114210223 free inodes.

server3 `/data`: 39734665216 available bytes; 99.45% used; 225846037 free inodes.

server3 `/tmp`: 292684013568 available bytes; 83.67% used; 114210223 free inodes.

server3 `/var/tmp`: 292684013568 available bytes; 83.67% used; 114210223 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106003021824 available bytes; 94.08% used; 114349830 free inodes.

server4 `/home`: 106003021824 available bytes; 94.08% used; 114349830 free inodes.

server4 `/data`: 289729433600 available bytes; 96.00% used; 225387205 free inodes.

server4 `/tmp`: 106003021824 available bytes; 94.08% used; 114349830 free inodes.

server4 `/var/tmp`: 106003021824 available bytes; 94.08% used; 114349830 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
