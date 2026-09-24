# V2R cluster inventory

2026-09-24T04:32:12.122709+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324633006080 available bytes; 81.89% used; 112493021 free inodes.

server1 `/home`: 324633006080 available bytes; 81.89% used; 112493021 free inodes.

server1 `/tmp`: 324633006080 available bytes; 81.89% used; 112493021 free inodes.

server1 `/var/tmp`: 324633006080 available bytes; 81.89% used; 112493021 free inodes.

server1 `/mnt/raid5`: 450476670976 available bytes; 97.93% used; 337724665 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40781414400 available bytes; 97.72% used; 110430528 free inodes.

server2 `/home`: 40781414400 available bytes; 97.72% used; 110430528 free inodes.

server2 `/tmp`: 40781414400 available bytes; 97.72% used; 110430528 free inodes.

server2 `/var/tmp`: 40781414400 available bytes; 97.72% used; 110430528 free inodes.

server2 `/mnt/raid5`: 524747841536 available bytes; 96.37% used; 445195905 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292003893248 available bytes; 83.71% used; 114176148 free inodes.

server3 `/home`: 292003893248 available bytes; 83.71% used; 114176148 free inodes.

server3 `/data`: 25410809856 available bytes; 99.65% used; 225840911 free inodes.

server3 `/tmp`: 292003893248 available bytes; 83.71% used; 114176148 free inodes.

server3 `/var/tmp`: 292003893248 available bytes; 83.71% used; 114176148 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105844420608 available bytes; 94.09% used; 114349421 free inodes.

server4 `/home`: 105844420608 available bytes; 94.09% used; 114349421 free inodes.

server4 `/data`: 253408235520 available bytes; 96.50% used; 225366893 free inodes.

server4 `/tmp`: 105844420608 available bytes; 94.09% used; 114349421 free inodes.

server4 `/var/tmp`: 105844420608 available bytes; 94.09% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
