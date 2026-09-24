# V2R cluster inventory

2026-09-24T11:41:45.142203+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324348583936 available bytes; 81.91% used; 112488832 free inodes.

server1 `/home`: 324348583936 available bytes; 81.91% used; 112488832 free inodes.

server1 `/tmp`: 324348583936 available bytes; 81.91% used; 112488832 free inodes.

server1 `/var/tmp`: 324348583936 available bytes; 81.91% used; 112488832 free inodes.

server1 `/mnt/raid5`: 430696919040 available bytes; 98.02% used; 337688026 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57655037952 available bytes; 96.78% used; 110429888 free inodes.

server2 `/home`: 57655037952 available bytes; 96.78% used; 110429888 free inodes.

server2 `/tmp`: 57655037952 available bytes; 96.78% used; 110429888 free inodes.

server2 `/var/tmp`: 57655037952 available bytes; 96.78% used; 110429888 free inodes.

server2 `/mnt/raid5`: 510293360640 available bytes; 96.47% used; 445173242 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84872343552 available bytes; 95.26% used; 114143667 free inodes.

server3 `/home`: 84872343552 available bytes; 95.26% used; 114143667 free inodes.

server3 `/data`: 163721224192 available bytes; 97.74% used; 225816348 free inodes.

server3 `/tmp`: 84872343552 available bytes; 95.26% used; 114143667 free inodes.

server3 `/var/tmp`: 84872343552 available bytes; 95.26% used; 114143667 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105729789952 available bytes; 94.10% used; 114348863 free inodes.

server4 `/home`: 105729789952 available bytes; 94.10% used; 114348863 free inodes.

server4 `/data`: 115396505600 available bytes; 98.41% used; 225257974 free inodes.

server4 `/tmp`: 105729789952 available bytes; 94.10% used; 114348863 free inodes.

server4 `/var/tmp`: 105729789952 available bytes; 94.10% used; 114348863 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
