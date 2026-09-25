# V2R cluster inventory

2026-09-25T21:28:25.722716+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318701703168 available bytes; 82.22% used; 112476322 free inodes.

server1 `/home`: 318701703168 available bytes; 82.22% used; 112476322 free inodes.

server1 `/tmp`: 318701703168 available bytes; 82.22% used; 112476322 free inodes.

server1 `/var/tmp`: 318701703168 available bytes; 82.22% used; 112476322 free inodes.

server1 `/mnt/raid5`: 346769661952 available bytes; 98.41% used; 337539318 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22905520128 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22905520128 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22905520128 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22905520128 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 301318307840 available bytes; 97.92% used; 445054965 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84363382784 available bytes; 95.29% used; 114152618 free inodes.

server3 `/home`: 84363382784 available bytes; 95.29% used; 114152618 free inodes.

server3 `/data`: 125899296768 available bytes; 98.26% used; 225807029 free inodes.

server3 `/tmp`: 84363382784 available bytes; 95.29% used; 114152618 free inodes.

server3 `/var/tmp`: 84363382784 available bytes; 95.29% used; 114152618 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389080576 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389080576 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217453936640 available bytes; 96.99% used; 224920127 free inodes.

server4 `/tmp`: 105389080576 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389080576 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
