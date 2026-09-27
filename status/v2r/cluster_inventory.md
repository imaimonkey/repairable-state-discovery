# V2R cluster inventory

2026-09-27T13:39:54.901368+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304672555008 available bytes; 83.00% used; 112401375 free inodes.

server1 `/home`: 304672555008 available bytes; 83.00% used; 112401375 free inodes.

server1 `/tmp`: 304672555008 available bytes; 83.00% used; 112401375 free inodes.

server1 `/var/tmp`: 304672555008 available bytes; 83.00% used; 112401375 free inodes.

server1 `/mnt/raid5`: 634890313728 available bytes; 97.09% used; 337424241 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13408403456 available bytes; 99.25% used; 110351818 free inodes.

server2 `/home`: 13408403456 available bytes; 99.25% used; 110351818 free inodes.

server2 `/tmp`: 13408403456 available bytes; 99.25% used; 110351818 free inodes.

server2 `/var/tmp`: 13408403456 available bytes; 99.25% used; 110351818 free inodes.

server2 `/mnt/raid5`: 528458379264 available bytes; 96.35% used; 444733063 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 78567170048 available bytes; 95.62% used; 114062770 free inodes.

server3 `/home`: 78567170048 available bytes; 95.62% used; 114062770 free inodes.

server3 `/data`: 1330873511936 available bytes; 81.61% used; 225757455 free inodes.

server3 `/tmp`: 78567170048 available bytes; 95.62% used; 114062770 free inodes.

server3 `/var/tmp`: 78567170048 available bytes; 95.62% used; 114062770 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111010222080 available bytes; 93.81% used; 114372795 free inodes.

server4 `/home`: 111010222080 available bytes; 93.81% used; 114372795 free inodes.

server4 `/data`: 351100833792 available bytes; 95.15% used; 224727496 free inodes.

server4 `/tmp`: 111010222080 available bytes; 93.81% used; 114372795 free inodes.

server4 `/var/tmp`: 111010222080 available bytes; 93.81% used; 114372795 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
