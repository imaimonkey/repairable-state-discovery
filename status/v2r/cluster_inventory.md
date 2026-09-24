# V2R cluster inventory

2026-09-24T07:04:16.867439+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324481482752 available bytes; 81.90% used; 112491342 free inodes.

server1 `/home`: 324481482752 available bytes; 81.90% used; 112491342 free inodes.

server1 `/tmp`: 324481482752 available bytes; 81.90% used; 112491342 free inodes.

server1 `/var/tmp`: 324481482752 available bytes; 81.90% used; 112491342 free inodes.

server1 `/mnt/raid5`: 517429018624 available bytes; 97.63% used; 337722837 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57861562368 available bytes; 96.77% used; 110431169 free inodes.

server2 `/home`: 57861562368 available bytes; 96.77% used; 110431169 free inodes.

server2 `/tmp`: 57861562368 available bytes; 96.77% used; 110431169 free inodes.

server2 `/var/tmp`: 57861562368 available bytes; 96.77% used; 110431169 free inodes.

server2 `/mnt/raid5`: 519181201408 available bytes; 96.41% used; 445190769 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127168147456 available bytes; 92.90% used; 114199241 free inodes.

server3 `/home`: 127168147456 available bytes; 92.90% used; 114199241 free inodes.

server3 `/data`: 139170775040 available bytes; 98.08% used; 225834690 free inodes.

server3 `/tmp`: 127168147456 available bytes; 92.90% used; 114199241 free inodes.

server3 `/var/tmp`: 127168147456 available bytes; 92.90% used; 114199241 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105790291968 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105790291968 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 300886966272 available bytes; 95.84% used; 225367626 free inodes.

server4 `/tmp`: 105790291968 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105790291968 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
