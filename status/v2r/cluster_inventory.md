# V2R cluster inventory

2026-09-27T08:07:35.624907+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314468667392 available bytes; 82.46% used; 112440802 free inodes.

server1 `/home`: 314468667392 available bytes; 82.46% used; 112440802 free inodes.

server1 `/tmp`: 314468667392 available bytes; 82.46% used; 112440802 free inodes.

server1 `/var/tmp`: 314468667392 available bytes; 82.46% used; 112440802 free inodes.

server1 `/mnt/raid5`: 634650017792 available bytes; 97.09% used; 337400006 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17614979072 available bytes; 99.02% used; 110365014 free inodes.

server2 `/home`: 17614979072 available bytes; 99.02% used; 110365014 free inodes.

server2 `/tmp`: 17614979072 available bytes; 99.02% used; 110365014 free inodes.

server2 `/var/tmp`: 17614979072 available bytes; 99.02% used; 110365014 free inodes.

server2 `/mnt/raid5`: 570274783232 available bytes; 96.06% used; 444872997 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78572519424 available bytes; 95.62% used; 114062877 free inodes.

server3 `/home`: 78572519424 available bytes; 95.62% used; 114062877 free inodes.

server3 `/data`: 1332870856704 available bytes; 81.58% used; 225763689 free inodes.

server3 `/tmp`: 78572519424 available bytes; 95.62% used; 114062877 free inodes.

server3 `/var/tmp`: 78572519424 available bytes; 95.62% used; 114062877 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111061135360 available bytes; 93.80% used; 114372881 free inodes.

server4 `/home`: 111061135360 available bytes; 93.80% used; 114372881 free inodes.

server4 `/data`: 368329826304 available bytes; 94.91% used; 224770906 free inodes.

server4 `/tmp`: 111061135360 available bytes; 93.80% used; 114372881 free inodes.

server4 `/var/tmp`: 111061135360 available bytes; 93.80% used; 114372881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
