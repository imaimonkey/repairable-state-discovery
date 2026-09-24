# V2R cluster inventory

2026-09-24T02:47:47.625698+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325388255232 available bytes; 81.85% used; 112498682 free inodes.

server1 `/home`: 325388255232 available bytes; 81.85% used; 112498682 free inodes.

server1 `/tmp`: 325388255232 available bytes; 81.85% used; 112498682 free inodes.

server1 `/var/tmp`: 325388255232 available bytes; 81.85% used; 112498682 free inodes.

server1 `/mnt/raid5`: 571701530624 available bytes; 97.38% used; 337733149 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40876490752 available bytes; 97.72% used; 110431414 free inodes.

server2 `/home`: 40876490752 available bytes; 97.72% used; 110431414 free inodes.

server2 `/tmp`: 40876490752 available bytes; 97.72% used; 110431414 free inodes.

server2 `/var/tmp`: 40876490752 available bytes; 97.72% used; 110431414 free inodes.

server2 `/mnt/raid5`: 528464891904 available bytes; 96.35% used; 445198966 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292670066688 available bytes; 83.67% used; 114208134 free inodes.

server3 `/home`: 292670066688 available bytes; 83.67% used; 114208134 free inodes.

server3 `/data`: 39730749440 available bytes; 99.45% used; 225845977 free inodes.

server3 `/tmp`: 292670066688 available bytes; 83.67% used; 114208134 free inodes.

server3 `/var/tmp`: 292670066688 available bytes; 83.67% used; 114208134 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002849792 available bytes; 94.08% used; 114349825 free inodes.

server4 `/home`: 106002849792 available bytes; 94.08% used; 114349825 free inodes.

server4 `/data`: 289726275584 available bytes; 96.00% used; 225387139 free inodes.

server4 `/tmp`: 106002849792 available bytes; 94.08% used; 114349825 free inodes.

server4 `/var/tmp`: 106002849792 available bytes; 94.08% used; 114349825 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
