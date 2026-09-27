# V2R cluster inventory

2026-09-27T02:21:50.863343+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315158806528 available bytes; 82.42% used; 112443328 free inodes.

server1 `/home`: 315158806528 available bytes; 82.42% used; 112443328 free inodes.

server1 `/tmp`: 315158806528 available bytes; 82.42% used; 112443328 free inodes.

server1 `/var/tmp`: 315158806528 available bytes; 82.42% used; 112443328 free inodes.

server1 `/mnt/raid5`: 637263626240 available bytes; 97.08% used; 337401673 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17636651008 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17636651008 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17636651008 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17636651008 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 580690784256 available bytes; 95.99% used; 444885156 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78709878784 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78709878784 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1337717444608 available bytes; 81.51% used; 225762461 free inodes.

server3 `/tmp`: 78709878784 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78709878784 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111036661760 available bytes; 93.80% used; 114373264 free inodes.

server4 `/home`: 111036661760 available bytes; 93.80% used; 114373264 free inodes.

server4 `/data`: 400321990656 available bytes; 94.47% used; 224781691 free inodes.

server4 `/tmp`: 111036661760 available bytes; 93.80% used; 114373264 free inodes.

server4 `/var/tmp`: 111036661760 available bytes; 93.80% used; 114373264 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
