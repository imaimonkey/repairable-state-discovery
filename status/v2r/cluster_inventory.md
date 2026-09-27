# V2R cluster inventory

2026-09-27T11:05:54.297933+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 303610118144 available bytes; 83.06% used; 112415267 free inodes.

server1 `/home`: 303610118144 available bytes; 83.06% used; 112415267 free inodes.

server1 `/tmp`: 303610118144 available bytes; 83.06% used; 112415267 free inodes.

server1 `/var/tmp`: 303610118144 available bytes; 83.06% used; 112415267 free inodes.

server1 `/mnt/raid5`: 635403124736 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16436482048 available bytes; 99.08% used; 110353739 free inodes.

server2 `/home`: 16436482048 available bytes; 99.08% used; 110353739 free inodes.

server2 `/tmp`: 16436482048 available bytes; 99.08% used; 110353739 free inodes.

server2 `/var/tmp`: 16436482048 available bytes; 99.08% used; 110353739 free inodes.

server2 `/mnt/raid5`: 570756829184 available bytes; 96.06% used; 444737762 free inodes.
| server3 | True | ['0', '2'] | [] | reference_compatible=True |

server3 `/`: 78544982016 available bytes; 95.62% used; 114062818 free inodes.

server3 `/home`: 78544982016 available bytes; 95.62% used; 114062818 free inodes.

server3 `/data`: 1332005720064 available bytes; 81.59% used; 225760254 free inodes.

server3 `/tmp`: 78544982016 available bytes; 95.62% used; 114062818 free inodes.

server3 `/var/tmp`: 78544982016 available bytes; 95.62% used; 114062818 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111030890496 available bytes; 93.80% used; 114372822 free inodes.

server4 `/home`: 111030890496 available bytes; 93.80% used; 114372822 free inodes.

server4 `/data`: 362758737920 available bytes; 94.99% used; 224764604 free inodes.

server4 `/tmp`: 111030890496 available bytes; 93.80% used; 114372822 free inodes.

server4 `/var/tmp`: 111030890496 available bytes; 93.80% used; 114372822 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
