# V2R cluster inventory

2026-09-24T10:40:42.178041+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324405174272 available bytes; 81.90% used; 112489190 free inodes.

server1 `/home`: 324405174272 available bytes; 81.90% used; 112489190 free inodes.

server1 `/tmp`: 324405174272 available bytes; 81.90% used; 112489190 free inodes.

server1 `/var/tmp`: 324405174272 available bytes; 81.90% used; 112489190 free inodes.

server1 `/mnt/raid5`: 499881005056 available bytes; 97.71% used; 337696559 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57719144448 available bytes; 96.78% used; 110430501 free inodes.

server2 `/home`: 57719144448 available bytes; 96.78% used; 110430501 free inodes.

server2 `/tmp`: 57719144448 available bytes; 96.78% used; 110430501 free inodes.

server2 `/var/tmp`: 57719144448 available bytes; 96.78% used; 110430501 free inodes.

server2 `/mnt/raid5`: 512464162816 available bytes; 96.46% used; 445175026 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85817253888 available bytes; 95.21% used; 114199468 free inodes.

server3 `/home`: 85817253888 available bytes; 95.21% used; 114199468 free inodes.

server3 `/data`: 164155092992 available bytes; 97.73% used; 225818013 free inodes.

server3 `/tmp`: 85817253888 available bytes; 95.21% used; 114199468 free inodes.

server3 `/var/tmp`: 85817253888 available bytes; 95.21% used; 114199468 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744101376 available bytes; 94.10% used; 114348964 free inodes.

server4 `/home`: 105744101376 available bytes; 94.10% used; 114348964 free inodes.

server4 `/data`: 153468887040 available bytes; 97.88% used; 225258358 free inodes.

server4 `/tmp`: 105744101376 available bytes; 94.10% used; 114348964 free inodes.

server4 `/var/tmp`: 105744101376 available bytes; 94.10% used; 114348964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
