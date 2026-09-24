# V2R cluster inventory

2026-09-24T03:27:19.058592+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325355282432 available bytes; 81.85% used; 112498185 free inodes.

server1 `/home`: 325355282432 available bytes; 81.85% used; 112498185 free inodes.

server1 `/tmp`: 325355282432 available bytes; 81.85% used; 112498185 free inodes.

server1 `/var/tmp`: 325355282432 available bytes; 81.85% used; 112498185 free inodes.

server1 `/mnt/raid5`: 411908964352 available bytes; 98.11% used; 337733411 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40842190848 available bytes; 97.72% used; 110431122 free inodes.

server2 `/home`: 40842190848 available bytes; 97.72% used; 110431122 free inodes.

server2 `/tmp`: 40842190848 available bytes; 97.72% used; 110431122 free inodes.

server2 `/var/tmp`: 40842190848 available bytes; 97.72% used; 110431122 free inodes.

server2 `/mnt/raid5`: 527326425088 available bytes; 96.36% used; 445198147 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292385873920 available bytes; 83.68% used; 114201276 free inodes.

server3 `/home`: 292385873920 available bytes; 83.68% used; 114201276 free inodes.

server3 `/data`: 36718931968 available bytes; 99.49% used; 225843112 free inodes.

server3 `/tmp`: 292385873920 available bytes; 83.68% used; 114201276 free inodes.

server3 `/var/tmp`: 292385873920 available bytes; 83.68% used; 114201276 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105987174400 available bytes; 94.09% used; 114349606 free inodes.

server4 `/home`: 105987174400 available bytes; 94.09% used; 114349606 free inodes.

server4 `/data`: 284326113280 available bytes; 96.07% used; 225385695 free inodes.

server4 `/tmp`: 105987174400 available bytes; 94.09% used; 114349606 free inodes.

server4 `/var/tmp`: 105987174400 available bytes; 94.09% used; 114349606 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
