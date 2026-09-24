# V2R cluster inventory

2026-09-24T01:15:19.639843+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325477351424 available bytes; 81.84% used; 112499877 free inodes.

server1 `/home`: 325477351424 available bytes; 81.84% used; 112499877 free inodes.

server1 `/tmp`: 325477351424 available bytes; 81.84% used; 112499877 free inodes.

server1 `/var/tmp`: 325477351424 available bytes; 81.84% used; 112499877 free inodes.

server1 `/mnt/raid5`: 956798476288 available bytes; 95.61% used; 337734138 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40955609088 available bytes; 97.72% used; 110432107 free inodes.

server2 `/home`: 40955609088 available bytes; 97.72% used; 110432107 free inodes.

server2 `/tmp`: 40955609088 available bytes; 97.72% used; 110432107 free inodes.

server2 `/var/tmp`: 40955609088 available bytes; 97.72% used; 110432107 free inodes.

server2 `/mnt/raid5`: 531394166784 available bytes; 96.33% used; 445201658 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292360089600 available bytes; 83.69% used; 114188200 free inodes.

server3 `/home`: 292360089600 available bytes; 83.69% used; 114188200 free inodes.

server3 `/data`: 82068332544 available bytes; 98.87% used; 225842674 free inodes.

server3 `/tmp`: 292360089600 available bytes; 83.69% used; 114188200 free inodes.

server3 `/var/tmp`: 292360089600 available bytes; 83.69% used; 114188200 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105994506240 available bytes; 94.09% used; 114349119 free inodes.

server4 `/home`: 105994506240 available bytes; 94.09% used; 114349119 free inodes.

server4 `/data`: 290834784256 available bytes; 95.98% used; 225397034 free inodes.

server4 `/tmp`: 105994506240 available bytes; 94.09% used; 114349119 free inodes.

server4 `/var/tmp`: 105994506240 available bytes; 94.09% used; 114349119 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
