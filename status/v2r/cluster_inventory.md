# V2R cluster inventory

2026-09-26T08:30:37.344080+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318747127808 available bytes; 82.22% used; 112475801 free inodes.

server1 `/home`: 318747127808 available bytes; 82.22% used; 112475801 free inodes.

server1 `/tmp`: 318747127808 available bytes; 82.22% used; 112475801 free inodes.

server1 `/var/tmp`: 318747127808 available bytes; 82.22% used; 112475801 free inodes.

server1 `/mnt/raid5`: 219098738688 available bytes; 98.99% used; 337538931 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22318637056 available bytes; 98.75% used; 110403908 free inodes.

server2 `/home`: 22318637056 available bytes; 98.75% used; 110403908 free inodes.

server2 `/tmp`: 22318637056 available bytes; 98.75% used; 110403908 free inodes.

server2 `/var/tmp`: 22318637056 available bytes; 98.75% used; 110403908 free inodes.

server2 `/mnt/raid5`: 255693254656 available bytes; 98.23% used; 445024835 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82677985280 available bytes; 95.39% used; 114110807 free inodes.

server3 `/home`: 82677985280 available bytes; 95.39% used; 114110807 free inodes.

server3 `/data`: 123913682944 available bytes; 98.29% used; 225828879 free inodes.

server3 `/tmp`: 82677985280 available bytes; 95.39% used; 114110807 free inodes.

server3 `/var/tmp`: 82677985280 available bytes; 95.39% used; 114110807 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106064105472 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106064105472 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89369964544 available bytes; 98.76% used; 224883398 free inodes.

server4 `/tmp`: 106064105472 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106064105472 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
