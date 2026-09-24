# V2R cluster inventory

2026-09-24T10:18:59.018623+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324418719744 available bytes; 81.90% used; 112489361 free inodes.

server1 `/home`: 324418719744 available bytes; 81.90% used; 112489361 free inodes.

server1 `/tmp`: 324418719744 available bytes; 81.90% used; 112489361 free inodes.

server1 `/var/tmp`: 324418719744 available bytes; 81.90% used; 112489361 free inodes.

server1 `/mnt/raid5`: 500635316224 available bytes; 97.70% used; 337699142 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57737191424 available bytes; 96.78% used; 110430689 free inodes.

server2 `/home`: 57737191424 available bytes; 96.78% used; 110430689 free inodes.

server2 `/tmp`: 57737191424 available bytes; 96.78% used; 110430689 free inodes.

server2 `/var/tmp`: 57737191424 available bytes; 96.78% used; 110430689 free inodes.

server2 `/mnt/raid5`: 513066131456 available bytes; 96.45% used; 445175653 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85830520832 available bytes; 95.21% used; 114199511 free inodes.

server3 `/home`: 85830520832 available bytes; 95.21% used; 114199511 free inodes.

server3 `/data`: 164380696576 available bytes; 97.73% used; 225818840 free inodes.

server3 `/tmp`: 85830520832 available bytes; 95.21% used; 114199511 free inodes.

server3 `/var/tmp`: 85830520832 available bytes; 95.21% used; 114199511 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747091456 available bytes; 94.10% used; 114348988 free inodes.

server4 `/home`: 105747091456 available bytes; 94.10% used; 114348988 free inodes.

server4 `/data`: 153484804096 available bytes; 97.88% used; 225258419 free inodes.

server4 `/tmp`: 105747091456 available bytes; 94.10% used; 114348988 free inodes.

server4 `/var/tmp`: 105747091456 available bytes; 94.10% used; 114348988 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
