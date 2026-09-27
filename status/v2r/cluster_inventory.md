# V2R cluster inventory

2026-09-27T04:37:25.935091+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314904498176 available bytes; 82.43% used; 112443032 free inodes.

server1 `/home`: 314904498176 available bytes; 82.43% used; 112443032 free inodes.

server1 `/tmp`: 314904498176 available bytes; 82.43% used; 112443032 free inodes.

server1 `/var/tmp`: 314904498176 available bytes; 82.43% used; 112443032 free inodes.

server1 `/mnt/raid5`: 636061831168 available bytes; 97.08% used; 337400320 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17631289344 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17631289344 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17631289344 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17631289344 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 576628215808 available bytes; 96.02% used; 444879374 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78694916096 available bytes; 95.61% used; 114062926 free inodes.

server3 `/home`: 78694916096 available bytes; 95.61% used; 114062926 free inodes.

server3 `/data`: 1335063076864 available bytes; 81.55% used; 225759112 free inodes.

server3 `/tmp`: 78694916096 available bytes; 95.61% used; 114062926 free inodes.

server3 `/var/tmp`: 78694916096 available bytes; 95.61% used; 114062926 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111009558528 available bytes; 93.81% used; 114372934 free inodes.

server4 `/home`: 111009558528 available bytes; 93.81% used; 114372934 free inodes.

server4 `/data`: 382118084608 available bytes; 94.72% used; 224780554 free inodes.

server4 `/tmp`: 111009558528 available bytes; 93.81% used; 114372934 free inodes.

server4 `/var/tmp`: 111009558528 available bytes; 93.81% used; 114372934 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
