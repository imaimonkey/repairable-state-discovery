# V2R cluster inventory

2026-09-27T12:57:09.511226+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304680026112 available bytes; 83.00% used; 112401386 free inodes.

server1 `/home`: 304680026112 available bytes; 83.00% used; 112401386 free inodes.

server1 `/tmp`: 304680026112 available bytes; 83.00% used; 112401386 free inodes.

server1 `/var/tmp`: 304680026112 available bytes; 83.00% used; 112401386 free inodes.

server1 `/mnt/raid5`: 634594951168 available bytes; 97.09% used; 337424230 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13413408768 available bytes; 99.25% used; 110351849 free inodes.

server2 `/home`: 13413408768 available bytes; 99.25% used; 110351849 free inodes.

server2 `/tmp`: 13413408768 available bytes; 99.25% used; 110351849 free inodes.

server2 `/var/tmp`: 13413408768 available bytes; 99.25% used; 110351849 free inodes.

server2 `/mnt/raid5`: 538869579776 available bytes; 96.28% used; 444734282 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78577385472 available bytes; 95.62% used; 114062858 free inodes.

server3 `/home`: 78577385472 available bytes; 95.62% used; 114062858 free inodes.

server3 `/data`: 1331515797504 available bytes; 81.60% used; 225757939 free inodes.

server3 `/tmp`: 78577385472 available bytes; 95.62% used; 114062858 free inodes.

server3 `/var/tmp`: 78577385472 available bytes; 95.62% used; 114062858 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111011237888 available bytes; 93.81% used; 114372802 free inodes.

server4 `/home`: 111011237888 available bytes; 93.81% used; 114372802 free inodes.

server4 `/data`: 351834370048 available bytes; 95.14% used; 224727829 free inodes.

server4 `/tmp`: 111011237888 available bytes; 93.81% used; 114372802 free inodes.

server4 `/var/tmp`: 111011237888 available bytes; 93.81% used; 114372802 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
