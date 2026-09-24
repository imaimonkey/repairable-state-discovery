# V2R cluster inventory

2026-09-24T00:32:29.471128+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325549461504 available bytes; 81.84% used; 112500568 free inodes.

server1 `/home`: 325549461504 available bytes; 81.84% used; 112500568 free inodes.

server1 `/tmp`: 325549461504 available bytes; 81.84% used; 112500568 free inodes.

server1 `/var/tmp`: 325549461504 available bytes; 81.84% used; 112500568 free inodes.

server1 `/mnt/raid5`: 1115398963200 available bytes; 94.88% used; 337735110 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40994127872 available bytes; 97.71% used; 110432332 free inodes.

server2 `/home`: 40994127872 available bytes; 97.71% used; 110432332 free inodes.

server2 `/tmp`: 40994127872 available bytes; 97.71% used; 110432332 free inodes.

server2 `/var/tmp`: 40994127872 available bytes; 97.71% used; 110432332 free inodes.

server2 `/mnt/raid5`: 532697440256 available bytes; 96.32% used; 445203271 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292195627008 available bytes; 83.69% used; 114186372 free inodes.

server3 `/home`: 292195627008 available bytes; 83.69% used; 114186372 free inodes.

server3 `/data`: 82238259200 available bytes; 98.86% used; 225844196 free inodes.

server3 `/tmp`: 292195627008 available bytes; 83.69% used; 114186372 free inodes.

server3 `/var/tmp`: 292195627008 available bytes; 83.69% used; 114186372 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106075795456 available bytes; 94.08% used; 114350283 free inodes.

server4 `/home`: 106075795456 available bytes; 94.08% used; 114350283 free inodes.

server4 `/data`: 292919582720 available bytes; 95.95% used; 225414581 free inodes.

server4 `/tmp`: 106075795456 available bytes; 94.08% used; 114350283 free inodes.

server4 `/var/tmp`: 106075795456 available bytes; 94.08% used; 114350283 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
