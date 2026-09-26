# V2R cluster inventory

2026-09-26T08:32:08.889795+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318746931200 available bytes; 82.22% used; 112475801 free inodes.

server1 `/home`: 318746931200 available bytes; 82.22% used; 112475801 free inodes.

server1 `/tmp`: 318746931200 available bytes; 82.22% used; 112475801 free inodes.

server1 `/var/tmp`: 318746931200 available bytes; 82.22% used; 112475801 free inodes.

server1 `/mnt/raid5`: 219100114944 available bytes; 98.99% used; 337538931 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22320578560 available bytes; 98.75% used; 110403906 free inodes.

server2 `/home`: 22320578560 available bytes; 98.75% used; 110403906 free inodes.

server2 `/tmp`: 22320578560 available bytes; 98.75% used; 110403906 free inodes.

server2 `/var/tmp`: 22320578560 available bytes; 98.75% used; 110403906 free inodes.

server2 `/mnt/raid5`: 255646273536 available bytes; 98.23% used; 445024673 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82678427648 available bytes; 95.39% used; 114110809 free inodes.

server3 `/home`: 82678427648 available bytes; 95.39% used; 114110809 free inodes.

server3 `/data`: 123912228864 available bytes; 98.29% used; 225828839 free inodes.

server3 `/tmp`: 82678427648 available bytes; 95.39% used; 114110809 free inodes.

server3 `/var/tmp`: 82678427648 available bytes; 95.39% used; 114110809 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106064084992 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106064084992 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89368870912 available bytes; 98.76% used; 224883396 free inodes.

server4 `/tmp`: 106064084992 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106064084992 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
