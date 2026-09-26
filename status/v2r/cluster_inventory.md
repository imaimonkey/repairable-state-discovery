# V2R cluster inventory

2026-09-26T08:12:18.930126+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318747549696 available bytes; 82.22% used; 112475790 free inodes.

server1 `/home`: 318747549696 available bytes; 82.22% used; 112475790 free inodes.

server1 `/tmp`: 318747549696 available bytes; 82.22% used; 112475790 free inodes.

server1 `/var/tmp`: 318747549696 available bytes; 82.22% used; 112475790 free inodes.

server1 `/mnt/raid5`: 219149836288 available bytes; 98.99% used; 337539034 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22313201664 available bytes; 98.76% used; 110403905 free inodes.

server2 `/home`: 22313201664 available bytes; 98.76% used; 110403905 free inodes.

server2 `/tmp`: 22313201664 available bytes; 98.76% used; 110403905 free inodes.

server2 `/var/tmp`: 22313201664 available bytes; 98.76% used; 110403905 free inodes.

server2 `/mnt/raid5`: 256229179392 available bytes; 98.23% used; 445025234 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82679291904 available bytes; 95.39% used; 114110814 free inodes.

server3 `/home`: 82679291904 available bytes; 95.39% used; 114110814 free inodes.

server3 `/data`: 123919626240 available bytes; 98.29% used; 225829306 free inodes.

server3 `/tmp`: 82679291904 available bytes; 95.39% used; 114110814 free inodes.

server3 `/var/tmp`: 82679291904 available bytes; 95.39% used; 114110814 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106064715776 available bytes; 94.08% used; 114348149 free inodes.

server4 `/home`: 106064715776 available bytes; 94.08% used; 114348149 free inodes.

server4 `/data`: 89390735360 available bytes; 98.76% used; 224883490 free inodes.

server4 `/tmp`: 106064715776 available bytes; 94.08% used; 114348149 free inodes.

server4 `/var/tmp`: 106064715776 available bytes; 94.08% used; 114348149 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
