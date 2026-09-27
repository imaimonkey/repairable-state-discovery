# V2R cluster inventory

2026-09-27T12:11:24.739991+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304693944320 available bytes; 83.00% used; 112401523 free inodes.

server1 `/home`: 304693944320 available bytes; 83.00% used; 112401523 free inodes.

server1 `/tmp`: 304693944320 available bytes; 83.00% used; 112401523 free inodes.

server1 `/var/tmp`: 304693944320 available bytes; 83.00% used; 112401523 free inodes.

server1 `/mnt/raid5`: 634680856576 available bytes; 97.09% used; 337424377 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16407363584 available bytes; 99.08% used; 110352886 free inodes.

server2 `/home`: 16407363584 available bytes; 99.08% used; 110352886 free inodes.

server2 `/tmp`: 16407363584 available bytes; 99.08% used; 110352886 free inodes.

server2 `/var/tmp`: 16407363584 available bytes; 99.08% used; 110352886 free inodes.

server2 `/mnt/raid5`: 568983035904 available bytes; 96.07% used; 444735622 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78542770176 available bytes; 95.62% used; 114062864 free inodes.

server3 `/home`: 78542770176 available bytes; 95.62% used; 114062864 free inodes.

server3 `/data`: 1331796557824 available bytes; 81.59% used; 225758558 free inodes.

server3 `/tmp`: 78542770176 available bytes; 95.62% used; 114062864 free inodes.

server3 `/var/tmp`: 78542770176 available bytes; 95.62% used; 114062864 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111029080064 available bytes; 93.80% used; 114372805 free inodes.

server4 `/home`: 111029080064 available bytes; 93.80% used; 114372805 free inodes.

server4 `/data`: 352622239744 available bytes; 95.13% used; 224727983 free inodes.

server4 `/tmp`: 111029080064 available bytes; 93.80% used; 114372805 free inodes.

server4 `/var/tmp`: 111029080064 available bytes; 93.80% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
