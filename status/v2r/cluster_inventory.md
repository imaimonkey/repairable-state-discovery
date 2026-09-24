# V2R cluster inventory

2026-09-24T08:34:47.807839+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324401037312 available bytes; 81.90% used; 112490416 free inodes.

server1 `/home`: 324401037312 available bytes; 81.90% used; 112490416 free inodes.

server1 `/tmp`: 324401037312 available bytes; 81.90% used; 112490416 free inodes.

server1 `/var/tmp`: 324401037312 available bytes; 81.90% used; 112490416 free inodes.

server1 `/mnt/raid5`: 508636946432 available bytes; 97.67% used; 337720116 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57806974976 available bytes; 96.78% used; 110430984 free inodes.

server2 `/home`: 57806974976 available bytes; 96.78% used; 110430984 free inodes.

server2 `/tmp`: 57806974976 available bytes; 96.78% used; 110430984 free inodes.

server2 `/var/tmp`: 57806974976 available bytes; 96.78% used; 110430984 free inodes.

server2 `/mnt/raid5`: 515992879104 available bytes; 96.43% used; 445179358 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85482430464 available bytes; 95.23% used; 114174924 free inodes.

server3 `/home`: 85482430464 available bytes; 95.23% used; 114174924 free inodes.

server3 `/data`: 174762405888 available bytes; 97.58% used; 225822810 free inodes.

server3 `/tmp`: 85482430464 available bytes; 95.23% used; 114174924 free inodes.

server3 `/var/tmp`: 85482430464 available bytes; 95.23% used; 114174924 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769111552 available bytes; 94.10% used; 114349115 free inodes.

server4 `/home`: 105769111552 available bytes; 94.10% used; 114349115 free inodes.

server4 `/data`: 255375589376 available bytes; 96.47% used; 225288386 free inodes.

server4 `/tmp`: 105769111552 available bytes; 94.10% used; 114349115 free inodes.

server4 `/var/tmp`: 105769111552 available bytes; 94.10% used; 114349115 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
