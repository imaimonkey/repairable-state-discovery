# V2R cluster inventory

2026-09-23T23:56:27.139079+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325582741504 available bytes; 81.84% used; 112500949 free inodes.

server1 `/home`: 325582741504 available bytes; 81.84% used; 112500949 free inodes.

server1 `/tmp`: 325582741504 available bytes; 81.84% used; 112500949 free inodes.

server1 `/var/tmp`: 325582741504 available bytes; 81.84% used; 112500949 free inodes.

server1 `/mnt/raid5`: 1282183651328 available bytes; 94.12% used; 337735446 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41020964864 available bytes; 97.71% used; 110432461 free inodes.

server2 `/home`: 41020964864 available bytes; 97.71% used; 110432461 free inodes.

server2 `/tmp`: 41020964864 available bytes; 97.71% used; 110432461 free inodes.

server2 `/var/tmp`: 41020964864 available bytes; 97.71% used; 110432461 free inodes.

server2 `/mnt/raid5`: 533641646080 available bytes; 96.31% used; 445204302 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292781244416 available bytes; 83.66% used; 114205970 free inodes.

server3 `/home`: 292781244416 available bytes; 83.66% used; 114205970 free inodes.

server3 `/data`: 82274889728 available bytes; 98.86% used; 225844910 free inodes.

server3 `/tmp`: 292781244416 available bytes; 83.66% used; 114205970 free inodes.

server3 `/var/tmp`: 292781244416 available bytes; 83.66% used; 114205970 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106146816000 available bytes; 94.08% used; 114351403 free inodes.

server4 `/home`: 106146816000 available bytes; 94.08% used; 114351403 free inodes.

server4 `/data`: 292946264064 available bytes; 95.95% used; 225416130 free inodes.

server4 `/tmp`: 106146816000 available bytes; 94.08% used; 114351403 free inodes.

server4 `/var/tmp`: 106146816000 available bytes; 94.08% used; 114351403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
