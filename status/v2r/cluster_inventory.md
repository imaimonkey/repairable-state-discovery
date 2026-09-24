# V2R cluster inventory

2026-09-24T00:58:15.373443+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325526540288 available bytes; 81.84% used; 112500296 free inodes.

server1 `/home`: 325526540288 available bytes; 81.84% used; 112500296 free inodes.

server1 `/tmp`: 325526540288 available bytes; 81.84% used; 112500296 free inodes.

server1 `/var/tmp`: 325526540288 available bytes; 81.84% used; 112500296 free inodes.

server1 `/mnt/raid5`: 1027554811904 available bytes; 95.29% used; 337734796 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40972271616 available bytes; 97.71% used; 110432224 free inodes.

server2 `/home`: 40972271616 available bytes; 97.71% used; 110432224 free inodes.

server2 `/tmp`: 40972271616 available bytes; 97.71% used; 110432224 free inodes.

server2 `/var/tmp`: 40972271616 available bytes; 97.71% used; 110432224 free inodes.

server2 `/mnt/raid5`: 531918856192 available bytes; 96.32% used; 445202339 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292746014720 available bytes; 83.66% used; 114211815 free inodes.

server3 `/home`: 292746014720 available bytes; 83.66% used; 114211815 free inodes.

server3 `/data`: 82158850048 available bytes; 98.86% used; 225843295 free inodes.

server3 `/tmp`: 292746014720 available bytes; 83.66% used; 114211815 free inodes.

server3 `/var/tmp`: 292746014720 available bytes; 83.66% used; 114211815 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106023587840 available bytes; 94.08% used; 114349593 free inodes.

server4 `/home`: 106023587840 available bytes; 94.08% used; 114349593 free inodes.

server4 `/data`: 292874911744 available bytes; 95.95% used; 225414551 free inodes.

server4 `/tmp`: 106023587840 available bytes; 94.08% used; 114349593 free inodes.

server4 `/var/tmp`: 106023587840 available bytes; 94.08% used; 114349593 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
