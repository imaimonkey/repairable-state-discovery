# V2R cluster inventory

2026-09-23T22:47:04.207714+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325745332224 available bytes; 81.83% used; 112501727 free inodes.

server1 `/home`: 325745332224 available bytes; 81.83% used; 112501727 free inodes.

server1 `/tmp`: 325745332224 available bytes; 81.83% used; 112501727 free inodes.

server1 `/var/tmp`: 325745332224 available bytes; 81.83% used; 112501727 free inodes.

server1 `/mnt/raid5`: 1388115390464 available bytes; 93.63% used; 337739964 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41072910336 available bytes; 97.71% used; 110432622 free inodes.

server2 `/home`: 41072910336 available bytes; 97.71% used; 110432622 free inodes.

server2 `/tmp`: 41072910336 available bytes; 97.71% used; 110432622 free inodes.

server2 `/var/tmp`: 41072910336 available bytes; 97.71% used; 110432622 free inodes.

server2 `/mnt/raid5`: 535634685952 available bytes; 96.30% used; 445206378 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292546330624 available bytes; 83.67% used; 114193389 free inodes.

server3 `/home`: 292546330624 available bytes; 83.67% used; 114193389 free inodes.

server3 `/data`: 82437165056 available bytes; 98.86% used; 225846896 free inodes.

server3 `/tmp`: 292546330624 available bytes; 83.67% used; 114193389 free inodes.

server3 `/var/tmp`: 292546330624 available bytes; 83.67% used; 114193389 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106326626304 available bytes; 94.07% used; 114353923 free inodes.

server4 `/home`: 106326626304 available bytes; 94.07% used; 114353923 free inodes.

server4 `/data`: 300111781888 available bytes; 95.85% used; 225434573 free inodes.

server4 `/tmp`: 106326626304 available bytes; 94.07% used; 114353923 free inodes.

server4 `/var/tmp`: 106326626304 available bytes; 94.07% used; 114353923 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
