# V2R cluster inventory

2026-09-25T02:11:29.180861+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318969397248 available bytes; 82.21% used; 112480527 free inodes.

server1 `/home`: 318969397248 available bytes; 82.21% used; 112480527 free inodes.

server1 `/tmp`: 318969397248 available bytes; 82.21% used; 112480527 free inodes.

server1 `/var/tmp`: 318969397248 available bytes; 82.21% used; 112480527 free inodes.

server1 `/mnt/raid5`: 416249778176 available bytes; 98.09% used; 337608100 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23023210496 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 23023210496 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 23023210496 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 23023210496 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 483974443008 available bytes; 96.66% used; 445114308 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84351266816 available bytes; 95.29% used; 114156074 free inodes.

server3 `/home`: 84351266816 available bytes; 95.29% used; 114156074 free inodes.

server3 `/data`: 145919991808 available bytes; 97.98% used; 225811517 free inodes.

server3 `/tmp`: 84351266816 available bytes; 95.29% used; 114156074 free inodes.

server3 `/var/tmp`: 84351266816 available bytes; 95.29% used; 114156074 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105752403968 available bytes; 94.10% used; 114348239 free inodes.

server4 `/home`: 105752403968 available bytes; 94.10% used; 114348239 free inodes.

server4 `/data`: 37813858304 available bytes; 99.48% used; 224978246 free inodes.

server4 `/tmp`: 105752403968 available bytes; 94.10% used; 114348239 free inodes.

server4 `/var/tmp`: 105752403968 available bytes; 94.10% used; 114348239 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
