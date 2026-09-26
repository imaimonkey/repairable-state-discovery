# V2R cluster inventory

2026-09-26T07:57:03.369103+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318751952896 available bytes; 82.22% used; 112476269 free inodes.

server1 `/home`: 318751952896 available bytes; 82.22% used; 112476269 free inodes.

server1 `/tmp`: 318751952896 available bytes; 82.22% used; 112476269 free inodes.

server1 `/var/tmp`: 318751952896 available bytes; 82.22% used; 112476269 free inodes.

server1 `/mnt/raid5`: 219176693760 available bytes; 98.99% used; 337539107 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22320410624 available bytes; 98.75% used; 110403905 free inodes.

server2 `/home`: 22320410624 available bytes; 98.75% used; 110403905 free inodes.

server2 `/tmp`: 22320410624 available bytes; 98.75% used; 110403905 free inodes.

server2 `/var/tmp`: 22320410624 available bytes; 98.75% used; 110403905 free inodes.

server2 `/mnt/raid5`: 256716910592 available bytes; 98.23% used; 445026166 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82679930880 available bytes; 95.39% used; 114110848 free inodes.

server3 `/home`: 82679930880 available bytes; 95.39% used; 114110848 free inodes.

server3 `/data`: 123898523648 available bytes; 98.29% used; 225820586 free inodes.

server3 `/tmp`: 82679930880 available bytes; 95.39% used; 114110848 free inodes.

server3 `/var/tmp`: 82679930880 available bytes; 95.39% used; 114110848 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106073616384 available bytes; 94.08% used; 114348156 free inodes.

server4 `/home`: 106073616384 available bytes; 94.08% used; 114348156 free inodes.

server4 `/data`: 105651425280 available bytes; 98.54% used; 224922414 free inodes.

server4 `/tmp`: 106073616384 available bytes; 94.08% used; 114348156 free inodes.

server4 `/var/tmp`: 106073616384 available bytes; 94.08% used; 114348156 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
