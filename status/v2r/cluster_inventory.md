# V2R cluster inventory

2026-09-27T12:55:38.132389+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304680198144 available bytes; 83.00% used; 112401392 free inodes.

server1 `/home`: 304680198144 available bytes; 83.00% used; 112401392 free inodes.

server1 `/tmp`: 304680198144 available bytes; 83.00% used; 112401392 free inodes.

server1 `/var/tmp`: 304680198144 available bytes; 83.00% used; 112401392 free inodes.

server1 `/mnt/raid5`: 634595414016 available bytes; 97.09% used; 337424232 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13413179392 available bytes; 99.25% used; 110351843 free inodes.

server2 `/home`: 13413179392 available bytes; 99.25% used; 110351843 free inodes.

server2 `/tmp`: 13413179392 available bytes; 99.25% used; 110351843 free inodes.

server2 `/var/tmp`: 13413179392 available bytes; 99.25% used; 110351843 free inodes.

server2 `/mnt/raid5`: 538910777344 available bytes; 96.28% used; 444734323 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78579077120 available bytes; 95.61% used; 114062858 free inodes.

server3 `/home`: 78579077120 available bytes; 95.61% used; 114062858 free inodes.

server3 `/data`: 1331516858368 available bytes; 81.60% used; 225757960 free inodes.

server3 `/tmp`: 78579077120 available bytes; 95.61% used; 114062858 free inodes.

server3 `/var/tmp`: 78579077120 available bytes; 95.61% used; 114062858 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111011270656 available bytes; 93.81% used; 114372802 free inodes.

server4 `/home`: 111011270656 available bytes; 93.81% used; 114372802 free inodes.

server4 `/data`: 351848316928 available bytes; 95.14% used; 224727830 free inodes.

server4 `/tmp`: 111011270656 available bytes; 93.81% used; 114372802 free inodes.

server4 `/var/tmp`: 111011270656 available bytes; 93.81% used; 114372802 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
