# V2R cluster inventory

2026-09-24T10:29:50.603376+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324410167296 available bytes; 81.90% used; 112489269 free inodes.

server1 `/home`: 324410167296 available bytes; 81.90% used; 112489269 free inodes.

server1 `/tmp`: 324410167296 available bytes; 81.90% used; 112489269 free inodes.

server1 `/var/tmp`: 324410167296 available bytes; 81.90% used; 112489269 free inodes.

server1 `/mnt/raid5`: 500159295488 available bytes; 97.71% used; 337697857 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57733955584 available bytes; 96.78% used; 110430640 free inodes.

server2 `/home`: 57733955584 available bytes; 96.78% used; 110430640 free inodes.

server2 `/tmp`: 57733955584 available bytes; 96.78% used; 110430640 free inodes.

server2 `/var/tmp`: 57733955584 available bytes; 96.78% used; 110430640 free inodes.

server2 `/mnt/raid5`: 512287862784 available bytes; 96.46% used; 445175576 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85364604928 available bytes; 95.24% used; 114173277 free inodes.

server3 `/home`: 85364604928 available bytes; 95.24% used; 114173277 free inodes.

server3 `/data`: 164310851584 available bytes; 97.73% used; 225818572 free inodes.

server3 `/tmp`: 85364604928 available bytes; 95.24% used; 114173277 free inodes.

server3 `/var/tmp`: 85364604928 available bytes; 95.24% used; 114173277 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744584704 available bytes; 94.10% used; 114348968 free inodes.

server4 `/home`: 105744584704 available bytes; 94.10% used; 114348968 free inodes.

server4 `/data`: 153475354624 available bytes; 97.88% used; 225258403 free inodes.

server4 `/tmp`: 105744584704 available bytes; 94.10% used; 114348968 free inodes.

server4 `/var/tmp`: 105744584704 available bytes; 94.10% used; 114348968 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
