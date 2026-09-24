# V2R cluster inventory

2026-09-24T00:01:32.878511+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325581312000 available bytes; 81.84% used; 112500895 free inodes.

server1 `/home`: 325581312000 available bytes; 81.84% used; 112500895 free inodes.

server1 `/tmp`: 325581312000 available bytes; 81.84% used; 112500895 free inodes.

server1 `/var/tmp`: 325581312000 available bytes; 81.84% used; 112500895 free inodes.

server1 `/mnt/raid5`: 1250183077888 available bytes; 94.26% used; 337735411 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41017782272 available bytes; 97.71% used; 110432439 free inodes.

server2 `/home`: 41017782272 available bytes; 97.71% used; 110432439 free inodes.

server2 `/tmp`: 41017782272 available bytes; 97.71% used; 110432439 free inodes.

server2 `/var/tmp`: 41017782272 available bytes; 97.71% used; 110432439 free inodes.

server2 `/mnt/raid5`: 512913768448 available bytes; 96.46% used; 445204290 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292803309568 available bytes; 83.66% used; 114213631 free inodes.

server3 `/home`: 292803309568 available bytes; 83.66% used; 114213631 free inodes.

server3 `/data`: 82268200960 available bytes; 98.86% used; 225844819 free inodes.

server3 `/tmp`: 292803309568 available bytes; 83.66% used; 114213631 free inodes.

server3 `/var/tmp`: 292803309568 available bytes; 83.66% used; 114213631 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106136117248 available bytes; 94.08% used; 114351223 free inodes.

server4 `/home`: 106136117248 available bytes; 94.08% used; 114351223 free inodes.

server4 `/data`: 292928806912 available bytes; 95.95% used; 225414699 free inodes.

server4 `/tmp`: 106136117248 available bytes; 94.08% used; 114351223 free inodes.

server4 `/var/tmp`: 106136117248 available bytes; 94.08% used; 114351223 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
