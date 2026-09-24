# V2R cluster inventory

2026-09-24T01:09:07.962562+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325491920896 available bytes; 81.84% used; 112499971 free inodes.

server1 `/home`: 325491920896 available bytes; 81.84% used; 112499971 free inodes.

server1 `/tmp`: 325491920896 available bytes; 81.84% used; 112499971 free inodes.

server1 `/var/tmp`: 325491920896 available bytes; 81.84% used; 112499971 free inodes.

server1 `/mnt/raid5`: 982678302720 available bytes; 95.49% used; 337734845 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40965357568 available bytes; 97.71% used; 110432145 free inodes.

server2 `/home`: 40965357568 available bytes; 97.71% used; 110432145 free inodes.

server2 `/tmp`: 40965357568 available bytes; 97.71% used; 110432145 free inodes.

server2 `/var/tmp`: 40965357568 available bytes; 97.71% used; 110432145 free inodes.

server2 `/mnt/raid5`: 531572723712 available bytes; 96.33% used; 445202106 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292482359296 available bytes; 83.68% used; 114200415 free inodes.

server3 `/home`: 292482359296 available bytes; 83.68% used; 114200415 free inodes.

server3 `/data`: 82087874560 available bytes; 98.87% used; 225843090 free inodes.

server3 `/tmp`: 292482359296 available bytes; 83.68% used; 114200415 free inodes.

server3 `/var/tmp`: 292482359296 available bytes; 83.68% used; 114200415 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106005446656 available bytes; 94.08% used; 114349296 free inodes.

server4 `/home`: 106005446656 available bytes; 94.08% used; 114349296 free inodes.

server4 `/data`: 292721217536 available bytes; 95.95% used; 225405396 free inodes.

server4 `/tmp`: 106005446656 available bytes; 94.08% used; 114349296 free inodes.

server4 `/var/tmp`: 106005446656 available bytes; 94.08% used; 114349296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
