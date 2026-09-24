# V2R cluster inventory

2026-09-24T01:12:43.789377+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325477937152 available bytes; 81.84% used; 112499909 free inodes.

server1 `/home`: 325477937152 available bytes; 81.84% used; 112499909 free inodes.

server1 `/tmp`: 325477937152 available bytes; 81.84% used; 112499909 free inodes.

server1 `/var/tmp`: 325477937152 available bytes; 81.84% used; 112499909 free inodes.

server1 `/mnt/raid5`: 967483322368 available bytes; 95.56% used; 337734132 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40958152704 available bytes; 97.72% used; 110432123 free inodes.

server2 `/home`: 40958152704 available bytes; 97.72% used; 110432123 free inodes.

server2 `/tmp`: 40958152704 available bytes; 97.72% used; 110432123 free inodes.

server2 `/var/tmp`: 40958152704 available bytes; 97.72% used; 110432123 free inodes.

server2 `/mnt/raid5`: 531461017600 available bytes; 96.33% used; 445201784 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292397162496 available bytes; 83.68% used; 114189811 free inodes.

server3 `/home`: 292397162496 available bytes; 83.68% used; 114189811 free inodes.

server3 `/data`: 82079150080 available bytes; 98.87% used; 225843018 free inodes.

server3 `/tmp`: 292397162496 available bytes; 83.68% used; 114189811 free inodes.

server3 `/var/tmp`: 292397162496 available bytes; 83.68% used; 114189811 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105999163392 available bytes; 94.08% used; 114349199 free inodes.

server4 `/home`: 105999163392 available bytes; 94.08% used; 114349199 free inodes.

server4 `/data`: 291866275840 available bytes; 95.97% used; 225405354 free inodes.

server4 `/tmp`: 105999163392 available bytes; 94.08% used; 114349199 free inodes.

server4 `/var/tmp`: 105999163392 available bytes; 94.08% used; 114349199 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
