# V2R cluster inventory

2026-09-23T15:49:32.463482+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['2', '3', '4', '5', '7'] | [] | reference_compatible=False |

server2 `/`: 41420451840 available bytes; 97.69% used; 110435187 free inodes.

server2 `/home`: 41420451840 available bytes; 97.69% used; 110435187 free inodes.

server2 `/tmp`: 41420451840 available bytes; 97.69% used; 110435187 free inodes.

server2 `/var/tmp`: 41420451840 available bytes; 97.69% used; 110435187 free inodes.

server2 `/mnt/raid5`: 550356295680 available bytes; 96.20% used; 445223427 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 376858439680 available bytes; 78.97% used; 114285317 free inodes.

server3 `/home`: 376858439680 available bytes; 78.97% used; 114285317 free inodes.

server3 `/data`: 125338001408 available bytes; 98.27% used; 225854790 free inodes.

server3 `/tmp`: 376858439680 available bytes; 78.97% used; 114285317 free inodes.

server3 `/var/tmp`: 376858439680 available bytes; 78.97% used; 114285317 free inodes.
| server4 | True | ['1', '2', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499321344 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499321344 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 38654996480 available bytes; 99.47% used; 225494939 free inodes.

server4 `/tmp`: 111499321344 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499321344 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
