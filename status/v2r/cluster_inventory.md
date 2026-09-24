# V2R cluster inventory

2026-09-24T09:46:20.992963+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324449689600 available bytes; 81.90% used; 112489662 free inodes.

server1 `/home`: 324449689600 available bytes; 81.90% used; 112489662 free inodes.

server1 `/tmp`: 324449689600 available bytes; 81.90% used; 112489662 free inodes.

server1 `/var/tmp`: 324449689600 available bytes; 81.90% used; 112489662 free inodes.

server1 `/mnt/raid5`: 500755099648 available bytes; 97.70% used; 337703028 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57756622848 available bytes; 96.78% used; 110430775 free inodes.

server2 `/home`: 57756622848 available bytes; 96.78% used; 110430775 free inodes.

server2 `/tmp`: 57756622848 available bytes; 96.78% used; 110430775 free inodes.

server2 `/var/tmp`: 57756622848 available bytes; 96.78% used; 110430775 free inodes.

server2 `/mnt/raid5`: 513558003712 available bytes; 96.45% used; 445176900 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85830602752 available bytes; 95.21% used; 114199406 free inodes.

server3 `/home`: 85830602752 available bytes; 95.21% used; 114199406 free inodes.

server3 `/data`: 165665247232 available bytes; 97.71% used; 225819871 free inodes.

server3 `/tmp`: 85830602752 available bytes; 95.21% used; 114199406 free inodes.

server3 `/var/tmp`: 85830602752 available bytes; 95.21% used; 114199406 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748598784 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748598784 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154561662976 available bytes; 97.86% used; 225273218 free inodes.

server4 `/tmp`: 105748598784 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748598784 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
