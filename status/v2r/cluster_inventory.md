# V2R cluster inventory

2026-09-27T12:37:19.785775+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304683286528 available bytes; 83.00% used; 112401392 free inodes.

server1 `/home`: 304683286528 available bytes; 83.00% used; 112401392 free inodes.

server1 `/tmp`: 304683286528 available bytes; 83.00% used; 112401392 free inodes.

server1 `/var/tmp`: 304683286528 available bytes; 83.00% used; 112401392 free inodes.

server1 `/mnt/raid5`: 634590236672 available bytes; 97.09% used; 337424227 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13429796864 available bytes; 99.25% used; 110352378 free inodes.

server2 `/home`: 13429796864 available bytes; 99.25% used; 110352378 free inodes.

server2 `/tmp`: 13429796864 available bytes; 99.25% used; 110352378 free inodes.

server2 `/var/tmp`: 13429796864 available bytes; 99.25% used; 110352378 free inodes.

server2 `/mnt/raid5`: 557942575104 available bytes; 96.14% used; 444735219 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78542913536 available bytes; 95.62% used; 114062860 free inodes.

server3 `/home`: 78542913536 available bytes; 95.62% used; 114062860 free inodes.

server3 `/data`: 1331759017984 available bytes; 81.59% used; 225758202 free inodes.

server3 `/tmp`: 78542913536 available bytes; 95.62% used; 114062860 free inodes.

server3 `/var/tmp`: 78542913536 available bytes; 95.62% used; 114062860 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111020093440 available bytes; 93.80% used; 114372805 free inodes.

server4 `/home`: 111020093440 available bytes; 93.80% used; 114372805 free inodes.

server4 `/data`: 352172695552 available bytes; 95.13% used; 224727853 free inodes.

server4 `/tmp`: 111020093440 available bytes; 93.80% used; 114372805 free inodes.

server4 `/var/tmp`: 111020093440 available bytes; 93.80% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
