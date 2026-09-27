# V2R cluster inventory

2026-09-27T12:03:47.835292+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304693465088 available bytes; 83.00% used; 112401451 free inodes.

server1 `/home`: 304693465088 available bytes; 83.00% used; 112401451 free inodes.

server1 `/tmp`: 304693465088 available bytes; 83.00% used; 112401451 free inodes.

server1 `/var/tmp`: 304693465088 available bytes; 83.00% used; 112401451 free inodes.

server1 `/mnt/raid5`: 634682904576 available bytes; 97.09% used; 337424394 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16408125440 available bytes; 99.08% used; 110352887 free inodes.

server2 `/home`: 16408125440 available bytes; 99.08% used; 110352887 free inodes.

server2 `/tmp`: 16408125440 available bytes; 99.08% used; 110352887 free inodes.

server2 `/var/tmp`: 16408125440 available bytes; 99.08% used; 110352887 free inodes.

server2 `/mnt/raid5`: 569200836608 available bytes; 96.07% used; 444735978 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78543679488 available bytes; 95.62% used; 114062869 free inodes.

server3 `/home`: 78543679488 available bytes; 95.62% used; 114062869 free inodes.

server3 `/data`: 1331863859200 available bytes; 81.59% used; 225758781 free inodes.

server3 `/tmp`: 78543679488 available bytes; 95.62% used; 114062869 free inodes.

server3 `/var/tmp`: 78543679488 available bytes; 95.62% used; 114062869 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111029252096 available bytes; 93.80% used; 114372805 free inodes.

server4 `/home`: 111029252096 available bytes; 93.80% used; 114372805 free inodes.

server4 `/data`: 352781209600 available bytes; 95.12% used; 224727998 free inodes.

server4 `/tmp`: 111029252096 available bytes; 93.80% used; 114372805 free inodes.

server4 `/var/tmp`: 111029252096 available bytes; 93.80% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
