# V2R cluster inventory

2026-09-27T04:23:43.603904+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314908823552 available bytes; 82.43% used; 112443035 free inodes.

server1 `/home`: 314908823552 available bytes; 82.43% used; 112443035 free inodes.

server1 `/tmp`: 314908823552 available bytes; 82.43% used; 112443035 free inodes.

server1 `/var/tmp`: 314908823552 available bytes; 82.43% used; 112443035 free inodes.

server1 `/mnt/raid5`: 636073308160 available bytes; 97.08% used; 337400365 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17530429440 available bytes; 99.02% used; 110364987 free inodes.

server2 `/home`: 17530429440 available bytes; 99.02% used; 110364987 free inodes.

server2 `/tmp`: 17530429440 available bytes; 99.02% used; 110364987 free inodes.

server2 `/var/tmp`: 17530425344 available bytes; 99.02% used; 110364987 free inodes.

server2 `/mnt/raid5`: 577035538432 available bytes; 96.01% used; 444879883 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78696173568 available bytes; 95.61% used; 114062932 free inodes.

server3 `/home`: 78696173568 available bytes; 95.61% used; 114062932 free inodes.

server3 `/data`: 1335166111744 available bytes; 81.55% used; 225759258 free inodes.

server3 `/tmp`: 78696173568 available bytes; 95.61% used; 114062932 free inodes.

server3 `/var/tmp`: 78696173568 available bytes; 95.61% used; 114062932 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111018287104 available bytes; 93.80% used; 114372940 free inodes.

server4 `/home`: 111018287104 available bytes; 93.80% used; 114372940 free inodes.

server4 `/data`: 382147833856 available bytes; 94.72% used; 224780570 free inodes.

server4 `/tmp`: 111018287104 available bytes; 93.80% used; 114372940 free inodes.

server4 `/var/tmp`: 111018287104 available bytes; 93.80% used; 114372940 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
