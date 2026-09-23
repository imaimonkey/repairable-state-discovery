# V2R cluster inventory

2026-09-23T12:58:29.191038+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41331589120 available bytes; 97.69% used; 110436099 free inodes.

server2 `/home`: 41331589120 available bytes; 97.69% used; 110436099 free inodes.

server2 `/tmp`: 41331589120 available bytes; 97.69% used; 110436099 free inodes.

server2 `/var/tmp`: 41331589120 available bytes; 97.69% used; 110436099 free inodes.

server2 `/mnt/raid5`: 556505198592 available bytes; 96.15% used; 445228504 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 378381963264 available bytes; 78.88% used; 114326302 free inodes.

server3 `/home`: 378381963264 available bytes; 78.88% used; 114326302 free inodes.

server3 `/data`: 134929592320 available bytes; 98.14% used; 225862500 free inodes.

server3 `/tmp`: 378381963264 available bytes; 78.88% used; 114326302 free inodes.

server3 `/var/tmp`: 378381963264 available bytes; 78.88% used; 114326302 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111677444096 available bytes; 93.77% used; 114378483 free inodes.

server4 `/home`: 111677444096 available bytes; 93.77% used; 114378483 free inodes.

server4 `/data`: 52298207232 available bytes; 99.28% used; 225403706 free inodes.

server4 `/tmp`: 111677444096 available bytes; 93.77% used; 114378483 free inodes.

server4 `/var/tmp`: 111677444096 available bytes; 93.77% used; 114378483 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
