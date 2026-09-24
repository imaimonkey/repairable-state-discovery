# V2R cluster inventory

2026-09-24T09:05:57.361962+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324376625152 available bytes; 81.90% used; 112490101 free inodes.

server1 `/home`: 324376625152 available bytes; 81.90% used; 112490101 free inodes.

server1 `/tmp`: 324376625152 available bytes; 81.90% used; 112490101 free inodes.

server1 `/var/tmp`: 324376625152 available bytes; 81.90% used; 112490101 free inodes.

server1 `/mnt/raid5`: 503732097024 available bytes; 97.69% used; 337716254 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57785856000 available bytes; 96.78% used; 110430945 free inodes.

server2 `/home`: 57785856000 available bytes; 96.78% used; 110430945 free inodes.

server2 `/tmp`: 57785856000 available bytes; 96.78% used; 110430945 free inodes.

server2 `/var/tmp`: 57785856000 available bytes; 96.78% used; 110430945 free inodes.

server2 `/mnt/raid5`: 514814001152 available bytes; 96.44% used; 445178529 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85882920960 available bytes; 95.21% used; 114198831 free inodes.

server3 `/home`: 85882920960 available bytes; 95.21% used; 114198831 free inodes.

server3 `/data`: 167022022656 available bytes; 97.69% used; 225821746 free inodes.

server3 `/tmp`: 85882920960 available bytes; 95.21% used; 114198831 free inodes.

server3 `/var/tmp`: 85882920960 available bytes; 95.21% used; 114198831 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105758904320 available bytes; 94.10% used; 114349076 free inodes.

server4 `/home`: 105758904320 available bytes; 94.10% used; 114349076 free inodes.

server4 `/data`: 319627812864 available bytes; 95.58% used; 225273401 free inodes.

server4 `/tmp`: 105758904320 available bytes; 94.10% used; 114349076 free inodes.

server4 `/var/tmp`: 105758904320 available bytes; 94.10% used; 114349076 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
