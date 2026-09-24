# V2R cluster inventory

2026-09-24T11:04:01.686448+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324373966848 available bytes; 81.90% used; 112489010 free inodes.

server1 `/home`: 324373966848 available bytes; 81.90% used; 112489010 free inodes.

server1 `/tmp`: 324373966848 available bytes; 81.90% used; 112489010 free inodes.

server1 `/var/tmp`: 324373966848 available bytes; 81.90% used; 112489010 free inodes.

server1 `/mnt/raid5`: 484013207552 available bytes; 97.78% used; 337692965 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57694756864 available bytes; 96.78% used; 110430253 free inodes.

server2 `/home`: 57694756864 available bytes; 96.78% used; 110430253 free inodes.

server2 `/tmp`: 57694756864 available bytes; 96.78% used; 110430253 free inodes.

server2 `/var/tmp`: 57694756864 available bytes; 96.78% used; 110430253 free inodes.

server2 `/mnt/raid5`: 511721951232 available bytes; 96.46% used; 445174314 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85348253696 available bytes; 95.24% used; 114171386 free inodes.

server3 `/home`: 85348253696 available bytes; 95.24% used; 114171386 free inodes.

server3 `/data`: 163993796608 available bytes; 97.73% used; 225817526 free inodes.

server3 `/tmp`: 85348253696 available bytes; 95.24% used; 114171386 free inodes.

server3 `/var/tmp`: 85348253696 available bytes; 95.24% used; 114171386 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105733828608 available bytes; 94.10% used; 114348923 free inodes.

server4 `/home`: 105733828608 available bytes; 94.10% used; 114348923 free inodes.

server4 `/data`: 115745894400 available bytes; 98.40% used; 225258216 free inodes.

server4 `/tmp`: 105733828608 available bytes; 94.10% used; 114348923 free inodes.

server4 `/var/tmp`: 105733828608 available bytes; 94.10% used; 114348923 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
