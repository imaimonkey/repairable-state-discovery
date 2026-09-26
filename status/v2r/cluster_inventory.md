# V2R cluster inventory

2026-09-26T08:37:52.090734+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318745399296 available bytes; 82.22% used; 112475800 free inodes.

server1 `/home`: 318745399296 available bytes; 82.22% used; 112475800 free inodes.

server1 `/tmp`: 318745399296 available bytes; 82.22% used; 112475800 free inodes.

server1 `/var/tmp`: 318745399296 available bytes; 82.22% used; 112475800 free inodes.

server1 `/mnt/raid5`: 219085246464 available bytes; 98.99% used; 337538904 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22320631808 available bytes; 98.75% used; 110403904 free inodes.

server2 `/home`: 22320631808 available bytes; 98.75% used; 110403904 free inodes.

server2 `/tmp`: 22320631808 available bytes; 98.75% used; 110403904 free inodes.

server2 `/var/tmp`: 22320631808 available bytes; 98.75% used; 110403904 free inodes.

server2 `/mnt/raid5`: 255489953792 available bytes; 98.23% used; 445024588 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82679619584 available bytes; 95.39% used; 114110821 free inodes.

server3 `/home`: 82679619584 available bytes; 95.39% used; 114110821 free inodes.

server3 `/data`: 123901087744 available bytes; 98.29% used; 225828681 free inodes.

server3 `/tmp`: 82679619584 available bytes; 95.39% used; 114110821 free inodes.

server3 `/var/tmp`: 82679619584 available bytes; 95.39% used; 114110821 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106063904768 available bytes; 94.08% used; 114348137 free inodes.

server4 `/home`: 106063904768 available bytes; 94.08% used; 114348137 free inodes.

server4 `/data`: 89370185728 available bytes; 98.76% used; 224883413 free inodes.

server4 `/tmp`: 106063904768 available bytes; 94.08% used; 114348137 free inodes.

server4 `/var/tmp`: 106063904768 available bytes; 94.08% used; 114348137 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
