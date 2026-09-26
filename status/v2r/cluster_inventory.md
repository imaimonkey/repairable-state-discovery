# V2R cluster inventory

2026-09-26T07:38:44.513514+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318768209920 available bytes; 82.22% used; 112476289 free inodes.

server1 `/home`: 318768209920 available bytes; 82.22% used; 112476289 free inodes.

server1 `/tmp`: 318768209920 available bytes; 82.22% used; 112476289 free inodes.

server1 `/var/tmp`: 318768209920 available bytes; 82.22% used; 112476289 free inodes.

server1 `/mnt/raid5`: 219224322048 available bytes; 98.99% used; 337539212 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22315925504 available bytes; 98.76% used; 110403925 free inodes.

server2 `/home`: 22315925504 available bytes; 98.76% used; 110403925 free inodes.

server2 `/tmp`: 22315925504 available bytes; 98.76% used; 110403925 free inodes.

server2 `/var/tmp`: 22315925504 available bytes; 98.76% used; 110403925 free inodes.

server2 `/mnt/raid5`: 270931914752 available bytes; 98.13% used; 445026373 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82680205312 available bytes; 95.39% used; 114110897 free inodes.

server3 `/home`: 82680205312 available bytes; 95.39% used; 114110897 free inodes.

server3 `/data`: 123975499776 available bytes; 98.29% used; 225820921 free inodes.

server3 `/tmp`: 82680205312 available bytes; 95.39% used; 114110897 free inodes.

server3 `/var/tmp`: 82680205312 available bytes; 95.39% used; 114110897 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106074206208 available bytes; 94.08% used; 114348170 free inodes.

server4 `/home`: 106074206208 available bytes; 94.08% used; 114348170 free inodes.

server4 `/data`: 105862299648 available bytes; 98.54% used; 224922672 free inodes.

server4 `/tmp`: 106074206208 available bytes; 94.08% used; 114348170 free inodes.

server4 `/var/tmp`: 106074206208 available bytes; 94.08% used; 114348170 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
