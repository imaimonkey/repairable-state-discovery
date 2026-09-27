# V2R cluster inventory

2026-09-27T04:49:36.873795+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314897510400 available bytes; 82.43% used; 112443037 free inodes.

server1 `/home`: 314897510400 available bytes; 82.43% used; 112443037 free inodes.

server1 `/tmp`: 314897510400 available bytes; 82.43% used; 112443037 free inodes.

server1 `/var/tmp`: 314897510400 available bytes; 82.43% used; 112443037 free inodes.

server1 `/mnt/raid5`: 636060123136 available bytes; 97.08% used; 337400337 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17628184576 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17628184576 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17628184576 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17628184576 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 576260894720 available bytes; 96.02% used; 444878823 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78698295296 available bytes; 95.61% used; 114062913 free inodes.

server3 `/home`: 78698295296 available bytes; 95.61% used; 114062913 free inodes.

server3 `/data`: 1333989535744 available bytes; 81.56% used; 225758907 free inodes.

server3 `/tmp`: 78698295296 available bytes; 95.61% used; 114062913 free inodes.

server3 `/var/tmp`: 78698295296 available bytes; 95.61% used; 114062913 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111000875008 available bytes; 93.81% used; 114372934 free inodes.

server4 `/home`: 111000875008 available bytes; 93.81% used; 114372934 free inodes.

server4 `/data`: 382114119680 available bytes; 94.72% used; 224780529 free inodes.

server4 `/tmp`: 111000875008 available bytes; 93.81% used; 114372934 free inodes.

server4 `/var/tmp`: 111000875008 available bytes; 93.81% used; 114372934 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
