# V2R cluster inventory

2026-09-24T03:10:25.810031+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325370781696 available bytes; 81.85% used; 112498434 free inodes.

server1 `/home`: 325370781696 available bytes; 81.85% used; 112498434 free inodes.

server1 `/tmp`: 325370781696 available bytes; 81.85% used; 112498434 free inodes.

server1 `/var/tmp`: 325370781696 available bytes; 81.85% used; 112498434 free inodes.

server1 `/mnt/raid5`: 475413897216 available bytes; 97.82% used; 337732226 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40857714688 available bytes; 97.72% used; 110431250 free inodes.

server2 `/home`: 40857714688 available bytes; 97.72% used; 110431250 free inodes.

server2 `/tmp`: 40857714688 available bytes; 97.72% used; 110431250 free inodes.

server2 `/var/tmp`: 40857714688 available bytes; 97.72% used; 110431250 free inodes.

server2 `/mnt/raid5`: 527757840384 available bytes; 96.35% used; 445198284 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292294266880 available bytes; 83.69% used; 114187093 free inodes.

server3 `/home`: 292294266880 available bytes; 83.69% used; 114187093 free inodes.

server3 `/data`: 39687114752 available bytes; 99.45% used; 225844789 free inodes.

server3 `/tmp`: 292294266880 available bytes; 83.69% used; 114187093 free inodes.

server3 `/var/tmp`: 292294266880 available bytes; 83.69% used; 114187093 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105987993600 available bytes; 94.09% used; 114349625 free inodes.

server4 `/home`: 105987993600 available bytes; 94.09% used; 114349625 free inodes.

server4 `/data`: 289701175296 available bytes; 96.00% used; 225386846 free inodes.

server4 `/tmp`: 105987993600 available bytes; 94.09% used; 114349625 free inodes.

server4 `/var/tmp`: 105987993600 available bytes; 94.09% used; 114349625 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
