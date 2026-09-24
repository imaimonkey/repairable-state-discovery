# V2R cluster inventory

2026-09-24T10:32:56.755416+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324408082432 available bytes; 81.90% used; 112489248 free inodes.

server1 `/home`: 324408082432 available bytes; 81.90% used; 112489248 free inodes.

server1 `/tmp`: 324408082432 available bytes; 81.90% used; 112489248 free inodes.

server1 `/var/tmp`: 324408082432 available bytes; 81.90% used; 112489248 free inodes.

server1 `/mnt/raid5`: 500150755328 available bytes; 97.71% used; 337697502 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57730961408 available bytes; 96.78% used; 110430583 free inodes.

server2 `/home`: 57730961408 available bytes; 96.78% used; 110430583 free inodes.

server2 `/tmp`: 57730961408 available bytes; 96.78% used; 110430583 free inodes.

server2 `/var/tmp`: 57730961408 available bytes; 96.78% used; 110430583 free inodes.

server2 `/mnt/raid5`: 512702578688 available bytes; 96.46% used; 445175257 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85261127680 available bytes; 95.24% used; 114169482 free inodes.

server3 `/home`: 85261127680 available bytes; 95.24% used; 114169482 free inodes.

server3 `/data`: 164275736576 available bytes; 97.73% used; 225818179 free inodes.

server3 `/tmp`: 85261127680 available bytes; 95.24% used; 114169482 free inodes.

server3 `/var/tmp`: 85261127680 available bytes; 95.24% used; 114169482 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744384000 available bytes; 94.10% used; 114348961 free inodes.

server4 `/home`: 105744384000 available bytes; 94.10% used; 114348961 free inodes.

server4 `/data`: 153482842112 available bytes; 97.88% used; 225258403 free inodes.

server4 `/tmp`: 105744384000 available bytes; 94.10% used; 114348961 free inodes.

server4 `/var/tmp`: 105744384000 available bytes; 94.10% used; 114348961 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
