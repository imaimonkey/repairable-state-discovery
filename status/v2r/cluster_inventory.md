# V2R cluster inventory

2026-09-24T00:10:21.564091+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325573779456 available bytes; 81.84% used; 112500808 free inodes.

server1 `/home`: 325573779456 available bytes; 81.84% used; 112500808 free inodes.

server1 `/tmp`: 325573779456 available bytes; 81.84% used; 112500808 free inodes.

server1 `/var/tmp`: 325573779456 available bytes; 81.84% used; 112500808 free inodes.

server1 `/mnt/raid5`: 1224424345600 available bytes; 94.38% used; 337735325 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41007747072 available bytes; 97.71% used; 110432407 free inodes.

server2 `/home`: 41007747072 available bytes; 97.71% used; 110432407 free inodes.

server2 `/tmp`: 41007747072 available bytes; 97.71% used; 110432407 free inodes.

server2 `/var/tmp`: 41007747072 available bytes; 97.71% used; 110432407 free inodes.

server2 `/mnt/raid5`: 532753940480 available bytes; 96.32% used; 445203794 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292600516608 available bytes; 83.67% used; 114209235 free inodes.

server3 `/home`: 292600516608 available bytes; 83.67% used; 114209235 free inodes.

server3 `/data`: 82260045824 available bytes; 98.86% used; 225844580 free inodes.

server3 `/tmp`: 292600516608 available bytes; 83.67% used; 114209235 free inodes.

server3 `/var/tmp`: 292600516608 available bytes; 83.67% used; 114209235 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106115813376 available bytes; 94.08% used; 114350911 free inodes.

server4 `/home`: 106115813376 available bytes; 94.08% used; 114350911 free inodes.

server4 `/data`: 292911624192 available bytes; 95.95% used; 225414568 free inodes.

server4 `/tmp`: 106115813376 available bytes; 94.08% used; 114350911 free inodes.

server4 `/var/tmp`: 106115813376 available bytes; 94.08% used; 114350911 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
