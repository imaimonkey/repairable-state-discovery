# V2R cluster inventory

2026-09-24T10:15:52.588368+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324421500928 available bytes; 81.90% used; 112489393 free inodes.

server1 `/home`: 324421500928 available bytes; 81.90% used; 112489393 free inodes.

server1 `/tmp`: 324421500928 available bytes; 81.90% used; 112489393 free inodes.

server1 `/var/tmp`: 324421500928 available bytes; 81.90% used; 112489393 free inodes.

server1 `/mnt/raid5`: 500648554496 available bytes; 97.70% used; 337699510 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57742950400 available bytes; 96.78% used; 110430697 free inodes.

server2 `/home`: 57742950400 available bytes; 96.78% used; 110430697 free inodes.

server2 `/tmp`: 57742950400 available bytes; 96.78% used; 110430697 free inodes.

server2 `/var/tmp`: 57742950400 available bytes; 96.78% used; 110430697 free inodes.

server2 `/mnt/raid5`: 513168478208 available bytes; 96.45% used; 445175867 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85385363456 available bytes; 95.24% used; 114173791 free inodes.

server3 `/home`: 85385363456 available bytes; 95.24% used; 114173791 free inodes.

server3 `/data`: 164403138560 available bytes; 97.73% used; 225818939 free inodes.

server3 `/tmp`: 85385363456 available bytes; 95.24% used; 114173791 free inodes.

server3 `/var/tmp`: 85385363456 available bytes; 95.24% used; 114173791 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747181568 available bytes; 94.10% used; 114348988 free inodes.

server4 `/home`: 105747181568 available bytes; 94.10% used; 114348988 free inodes.

server4 `/data`: 153488080896 available bytes; 97.88% used; 225258423 free inodes.

server4 `/tmp`: 105747181568 available bytes; 94.10% used; 114348988 free inodes.

server4 `/var/tmp`: 105747181568 available bytes; 94.10% used; 114348988 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
