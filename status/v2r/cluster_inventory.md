# V2R cluster inventory

2026-09-24T10:17:25.873651+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324420292608 available bytes; 81.90% used; 112489377 free inodes.

server1 `/home`: 324420292608 available bytes; 81.90% used; 112489377 free inodes.

server1 `/tmp`: 324420292608 available bytes; 81.90% used; 112489377 free inodes.

server1 `/var/tmp`: 324420292608 available bytes; 81.90% used; 112489377 free inodes.

server1 `/mnt/raid5`: 500638191616 available bytes; 97.70% used; 337699319 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57742475264 available bytes; 96.78% used; 110430693 free inodes.

server2 `/home`: 57742475264 available bytes; 96.78% used; 110430693 free inodes.

server2 `/tmp`: 57742475264 available bytes; 96.78% used; 110430693 free inodes.

server2 `/var/tmp`: 57742475264 available bytes; 96.78% used; 110430693 free inodes.

server2 `/mnt/raid5`: 513131110400 available bytes; 96.45% used; 445175829 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85832126464 available bytes; 95.21% used; 114199525 free inodes.

server3 `/home`: 85832126464 available bytes; 95.21% used; 114199525 free inodes.

server3 `/data`: 164390338560 available bytes; 97.73% used; 225818875 free inodes.

server3 `/tmp`: 85832126464 available bytes; 95.21% used; 114199525 free inodes.

server3 `/var/tmp`: 85832126464 available bytes; 95.21% used; 114199525 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747132416 available bytes; 94.10% used; 114348988 free inodes.

server4 `/home`: 105747132416 available bytes; 94.10% used; 114348988 free inodes.

server4 `/data`: 153486942208 available bytes; 97.88% used; 225258423 free inodes.

server4 `/tmp`: 105747132416 available bytes; 94.10% used; 114348988 free inodes.

server4 `/var/tmp`: 105747132416 available bytes; 94.10% used; 114348988 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
