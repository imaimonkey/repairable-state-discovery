# V2R cluster inventory

2026-09-24T03:12:02.036284+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325369274368 available bytes; 81.85% used; 112498418 free inodes.

server1 `/home`: 325369274368 available bytes; 81.85% used; 112498418 free inodes.

server1 `/tmp`: 325369274368 available bytes; 81.85% used; 112498418 free inodes.

server1 `/var/tmp`: 325369274368 available bytes; 81.85% used; 112498418 free inodes.

server1 `/mnt/raid5`: 468654280704 available bytes; 97.85% used; 337732343 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40856494080 available bytes; 97.72% used; 110431234 free inodes.

server2 `/home`: 40856494080 available bytes; 97.72% used; 110431234 free inodes.

server2 `/tmp`: 40856494080 available bytes; 97.72% used; 110431234 free inodes.

server2 `/var/tmp`: 40856494080 available bytes; 97.72% used; 110431234 free inodes.

server2 `/mnt/raid5`: 527708835840 available bytes; 96.35% used; 445198146 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292293910528 available bytes; 83.69% used; 114187091 free inodes.

server3 `/home`: 292293910528 available bytes; 83.69% used; 114187091 free inodes.

server3 `/data`: 39678857216 available bytes; 99.45% used; 225844753 free inodes.

server3 `/tmp`: 292293910528 available bytes; 83.69% used; 114187091 free inodes.

server3 `/var/tmp`: 292293910528 available bytes; 83.69% used; 114187091 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105987940352 available bytes; 94.09% used; 114349625 free inodes.

server4 `/home`: 105987940352 available bytes; 94.09% used; 114349625 free inodes.

server4 `/data`: 289700007936 available bytes; 96.00% used; 225386846 free inodes.

server4 `/tmp`: 105987940352 available bytes; 94.09% used; 114349625 free inodes.

server4 `/var/tmp`: 105987940352 available bytes; 94.09% used; 114349625 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
