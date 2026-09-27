# V2R cluster inventory

2026-09-27T12:35:48.365352+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304684036096 available bytes; 83.00% used; 112401392 free inodes.

server1 `/home`: 304684036096 available bytes; 83.00% used; 112401392 free inodes.

server1 `/tmp`: 304684036096 available bytes; 83.00% used; 112401392 free inodes.

server1 `/var/tmp`: 304684036096 available bytes; 83.00% used; 112401392 free inodes.

server1 `/mnt/raid5`: 634591391744 available bytes; 97.09% used; 337424227 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13431934976 available bytes; 99.25% used; 110352605 free inodes.

server2 `/home`: 13431934976 available bytes; 99.25% used; 110352605 free inodes.

server2 `/tmp`: 13431934976 available bytes; 99.25% used; 110352605 free inodes.

server2 `/var/tmp`: 13431934976 available bytes; 99.25% used; 110352605 free inodes.

server2 `/mnt/raid5`: 566706958336 available bytes; 96.08% used; 444735184 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78543245312 available bytes; 95.62% used; 114062860 free inodes.

server3 `/home`: 78543245312 available bytes; 95.62% used; 114062860 free inodes.

server3 `/data`: 1331761074176 available bytes; 81.59% used; 225758218 free inodes.

server3 `/tmp`: 78543245312 available bytes; 95.62% used; 114062860 free inodes.

server3 `/var/tmp`: 78543245312 available bytes; 95.62% used; 114062860 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111020126208 available bytes; 93.80% used; 114372805 free inodes.

server4 `/home`: 111020126208 available bytes; 93.80% used; 114372805 free inodes.

server4 `/data`: 352200126464 available bytes; 95.13% used; 224727853 free inodes.

server4 `/tmp`: 111020126208 available bytes; 93.80% used; 114372805 free inodes.

server4 `/var/tmp`: 111020126208 available bytes; 93.80% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
