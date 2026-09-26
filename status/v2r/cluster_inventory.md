# V2R cluster inventory

2026-09-26T11:48:51.001183+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318197686272 available bytes; 82.25% used; 112474779 free inodes.

server1 `/home`: 318197686272 available bytes; 82.25% used; 112474779 free inodes.

server1 `/tmp`: 318197686272 available bytes; 82.25% used; 112474779 free inodes.

server1 `/var/tmp`: 318197686272 available bytes; 82.25% used; 112474779 free inodes.

server1 `/mnt/raid5`: 218649972736 available bytes; 99.00% used; 337537980 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19787329536 available bytes; 98.90% used; 110383637 free inodes.

server2 `/home`: 19787329536 available bytes; 98.90% used; 110383637 free inodes.

server2 `/tmp`: 19787329536 available bytes; 98.90% used; 110383637 free inodes.

server2 `/var/tmp`: 19787329536 available bytes; 98.90% used; 110383637 free inodes.

server2 `/mnt/raid5`: 240327335936 available bytes; 98.34% used; 444977292 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82648948736 available bytes; 95.39% used; 114110823 free inodes.

server3 `/home`: 82648948736 available bytes; 95.39% used; 114110823 free inodes.

server3 `/data`: 123435376640 available bytes; 98.29% used; 225825199 free inodes.

server3 `/tmp`: 82648948736 available bytes; 95.39% used; 114110823 free inodes.

server3 `/var/tmp`: 82648948736 available bytes; 95.39% used; 114110823 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105900765184 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105900765184 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88606449664 available bytes; 98.78% used; 224879304 free inodes.

server4 `/tmp`: 105900765184 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105900765184 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
