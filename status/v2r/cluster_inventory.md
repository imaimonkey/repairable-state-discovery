# V2R cluster inventory

2026-09-23T22:50:08.873700+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325743927296 available bytes; 81.83% used; 112501727 free inodes.

server1 `/home`: 325743927296 available bytes; 81.83% used; 112501727 free inodes.

server1 `/tmp`: 325743927296 available bytes; 81.83% used; 112501727 free inodes.

server1 `/var/tmp`: 325743927296 available bytes; 81.83% used; 112501727 free inodes.

server1 `/mnt/raid5`: 1367465242624 available bytes; 93.73% used; 337739955 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41071054848 available bytes; 97.71% used; 110432621 free inodes.

server2 `/home`: 41071054848 available bytes; 97.71% used; 110432621 free inodes.

server2 `/tmp`: 41071054848 available bytes; 97.71% used; 110432621 free inodes.

server2 `/var/tmp`: 41071054848 available bytes; 97.71% used; 110432621 free inodes.

server2 `/mnt/raid5`: 535530926080 available bytes; 96.30% used; 445206163 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292536918016 available bytes; 83.68% used; 114192874 free inodes.

server3 `/home`: 292536918016 available bytes; 83.68% used; 114192874 free inodes.

server3 `/data`: 82363740160 available bytes; 98.86% used; 225846833 free inodes.

server3 `/tmp`: 292536918016 available bytes; 83.68% used; 114192874 free inodes.

server3 `/var/tmp`: 292536918016 available bytes; 83.68% used; 114192874 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106319822848 available bytes; 94.07% used; 114353815 free inodes.

server4 `/home`: 106319822848 available bytes; 94.07% used; 114353815 free inodes.

server4 `/data`: 300100558848 available bytes; 95.85% used; 225433971 free inodes.

server4 `/tmp`: 106319822848 available bytes; 94.07% used; 114353815 free inodes.

server4 `/var/tmp`: 106319822848 available bytes; 94.07% used; 114353815 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
