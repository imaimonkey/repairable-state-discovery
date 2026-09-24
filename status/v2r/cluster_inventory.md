# V2R cluster inventory

2026-09-24T11:16:38.692109+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324363497472 available bytes; 81.90% used; 112488945 free inodes.

server1 `/home`: 324363497472 available bytes; 81.90% used; 112488945 free inodes.

server1 `/tmp`: 324363497472 available bytes; 81.90% used; 112488945 free inodes.

server1 `/var/tmp`: 324363497472 available bytes; 81.90% used; 112488945 free inodes.

server1 `/mnt/raid5`: 464187613184 available bytes; 97.87% used; 337690938 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57678106624 available bytes; 96.78% used; 110430130 free inodes.

server2 `/home`: 57678106624 available bytes; 96.78% used; 110430130 free inodes.

server2 `/tmp`: 57678106624 available bytes; 96.78% used; 110430130 free inodes.

server2 `/var/tmp`: 57678106624 available bytes; 96.78% used; 110430130 free inodes.

server2 `/mnt/raid5`: 511047831552 available bytes; 96.47% used; 445173801 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85753466880 available bytes; 95.21% used; 114198665 free inodes.

server3 `/home`: 85753466880 available bytes; 95.21% used; 114198665 free inodes.

server3 `/data`: 163902132224 available bytes; 97.73% used; 225816912 free inodes.

server3 `/tmp`: 85753466880 available bytes; 95.21% used; 114198665 free inodes.

server3 `/var/tmp`: 85753466880 available bytes; 95.21% used; 114198665 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105731563520 available bytes; 94.10% used; 114348889 free inodes.

server4 `/home`: 105731563520 available bytes; 94.10% used; 114348889 free inodes.

server4 `/data`: 115648806912 available bytes; 98.40% used; 225258134 free inodes.

server4 `/tmp`: 105731563520 available bytes; 94.10% used; 114348889 free inodes.

server4 `/var/tmp`: 105731563520 available bytes; 94.10% used; 114348889 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
