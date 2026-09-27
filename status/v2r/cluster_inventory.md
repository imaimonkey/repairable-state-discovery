# V2R cluster inventory

2026-09-27T05:49:00.370804+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314498002944 available bytes; 82.46% used; 112440829 free inodes.

server1 `/home`: 314498002944 available bytes; 82.46% used; 112440829 free inodes.

server1 `/tmp`: 314498002944 available bytes; 82.46% used; 112440829 free inodes.

server1 `/var/tmp`: 314498002944 available bytes; 82.46% used; 112440829 free inodes.

server1 `/mnt/raid5`: 634730766336 available bytes; 97.09% used; 337400014 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17628176384 available bytes; 99.02% used; 110365008 free inodes.

server2 `/home`: 17628176384 available bytes; 99.02% used; 110365008 free inodes.

server2 `/tmp`: 17628176384 available bytes; 99.02% used; 110365008 free inodes.

server2 `/var/tmp`: 17628176384 available bytes; 99.02% used; 110365008 free inodes.

server2 `/mnt/raid5`: 574345388032 available bytes; 96.03% used; 444876872 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78581223424 available bytes; 95.61% used; 114062907 free inodes.

server3 `/home`: 78581223424 available bytes; 95.61% used; 114062907 free inodes.

server3 `/data`: 1333326483456 available bytes; 81.57% used; 225765984 free inodes.

server3 `/tmp`: 78581223424 available bytes; 95.61% used; 114062907 free inodes.

server3 `/var/tmp`: 78581223424 available bytes; 95.61% used; 114062907 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110999183360 available bytes; 93.81% used; 114372897 free inodes.

server4 `/home`: 110999183360 available bytes; 93.81% used; 114372897 free inodes.

server4 `/data`: 374547836928 available bytes; 94.82% used; 224771228 free inodes.

server4 `/tmp`: 110999183360 available bytes; 93.81% used; 114372897 free inodes.

server4 `/var/tmp`: 110999183360 available bytes; 93.81% used; 114372897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
