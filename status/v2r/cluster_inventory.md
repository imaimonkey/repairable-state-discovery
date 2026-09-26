# V2R cluster inventory

2026-09-26T08:29:05.878143+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318747590656 available bytes; 82.22% used; 112475803 free inodes.

server1 `/home`: 318747590656 available bytes; 82.22% used; 112475803 free inodes.

server1 `/tmp`: 318747590656 available bytes; 82.22% used; 112475803 free inodes.

server1 `/var/tmp`: 318747590656 available bytes; 82.22% used; 112475803 free inodes.

server1 `/mnt/raid5`: 219108499456 available bytes; 98.99% used; 337538953 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22318862336 available bytes; 98.75% used; 110403908 free inodes.

server2 `/home`: 22318862336 available bytes; 98.75% used; 110403908 free inodes.

server2 `/tmp`: 22318862336 available bytes; 98.75% used; 110403908 free inodes.

server2 `/var/tmp`: 22318862336 available bytes; 98.75% used; 110403908 free inodes.

server2 `/mnt/raid5`: 255762952192 available bytes; 98.23% used; 445025011 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82678341632 available bytes; 95.39% used; 114110809 free inodes.

server3 `/home`: 82678341632 available bytes; 95.39% used; 114110809 free inodes.

server3 `/data`: 123914493952 available bytes; 98.29% used; 225828900 free inodes.

server3 `/tmp`: 82678341632 available bytes; 95.39% used; 114110809 free inodes.

server3 `/var/tmp`: 82678341632 available bytes; 95.39% used; 114110809 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106064171008 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106064171008 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89370976256 available bytes; 98.76% used; 224883404 free inodes.

server4 `/tmp`: 106064171008 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106064171008 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
