# V2R cluster inventory

2026-09-24T07:09:22.309222+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324476731392 available bytes; 81.90% used; 112491290 free inodes.

server1 `/home`: 324476731392 available bytes; 81.90% used; 112491290 free inodes.

server1 `/tmp`: 324476731392 available bytes; 81.90% used; 112491290 free inodes.

server1 `/var/tmp`: 324476731392 available bytes; 81.90% used; 112491290 free inodes.

server1 `/mnt/raid5`: 517429202944 available bytes; 97.63% used; 337722833 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57861935104 available bytes; 96.77% used; 110431157 free inodes.

server2 `/home`: 57861935104 available bytes; 96.77% used; 110431157 free inodes.

server2 `/tmp`: 57861935104 available bytes; 96.77% used; 110431157 free inodes.

server2 `/var/tmp`: 57861935104 available bytes; 96.77% used; 110431157 free inodes.

server2 `/mnt/raid5`: 518924406784 available bytes; 96.41% used; 445181842 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127188623360 available bytes; 92.90% used; 114199224 free inodes.

server3 `/home`: 127188623360 available bytes; 92.90% used; 114199224 free inodes.

server3 `/data`: 139130683392 available bytes; 98.08% used; 225834555 free inodes.

server3 `/tmp`: 127188623360 available bytes; 92.90% used; 114199224 free inodes.

server3 `/var/tmp`: 127188623360 available bytes; 92.90% used; 114199224 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105790111744 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105790111744 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 297396080640 available bytes; 95.89% used; 225367440 free inodes.

server4 `/tmp`: 105790111744 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105790111744 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
