# V2R cluster inventory

2026-09-24T23:03:56.729777+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 321173962752 available bytes; 82.08% used; 112480870 free inodes.

server1 `/home`: 321173962752 available bytes; 82.08% used; 112480870 free inodes.

server1 `/tmp`: 321173962752 available bytes; 82.08% used; 112480870 free inodes.

server1 `/var/tmp`: 321173962752 available bytes; 82.08% used; 112480870 free inodes.

server1 `/mnt/raid5`: 415290454016 available bytes; 98.09% used; 337616282 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23130357760 available bytes; 98.71% used; 110410802 free inodes.

server2 `/home`: 23130357760 available bytes; 98.71% used; 110410802 free inodes.

server2 `/tmp`: 23130357760 available bytes; 98.71% used; 110410802 free inodes.

server2 `/var/tmp`: 23130357760 available bytes; 98.71% used; 110410802 free inodes.

server2 `/mnt/raid5`: 487478378496 available bytes; 96.63% used; 445152117 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84370575360 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84370575360 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 148718067712 available bytes; 97.94% used; 225801415 free inodes.

server3 `/tmp`: 84370575360 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84370575360 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800704000 available bytes; 94.10% used; 114348311 free inodes.

server4 `/home`: 105800704000 available bytes; 94.10% used; 114348311 free inodes.

server4 `/data`: 61938089984 available bytes; 99.14% used; 225185770 free inodes.

server4 `/tmp`: 105800704000 available bytes; 94.10% used; 114348311 free inodes.

server4 `/var/tmp`: 105800704000 available bytes; 94.10% used; 114348311 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
