# V2R cluster inventory

2026-09-27T05:23:07.082081+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314757382144 available bytes; 82.44% used; 112442998 free inodes.

server1 `/home`: 314757382144 available bytes; 82.44% used; 112442998 free inodes.

server1 `/tmp`: 314757382144 available bytes; 82.44% used; 112442998 free inodes.

server1 `/var/tmp`: 314757382144 available bytes; 82.44% used; 112442998 free inodes.

server1 `/mnt/raid5`: 634729639936 available bytes; 97.09% used; 337400116 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17628241920 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17628241920 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17628241920 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17628241920 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 575306145792 available bytes; 96.02% used; 444877774 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78575935488 available bytes; 95.62% used; 114062907 free inodes.

server3 `/home`: 78575935488 available bytes; 95.62% used; 114062907 free inodes.

server3 `/data`: 1332916985856 available bytes; 81.58% used; 225758002 free inodes.

server3 `/tmp`: 78575935488 available bytes; 95.62% used; 114062907 free inodes.

server3 `/var/tmp`: 78575935488 available bytes; 95.62% used; 114062907 free inodes.
| server4 | True | ['6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110999842816 available bytes; 93.81% used; 114372910 free inodes.

server4 `/home`: 110999842816 available bytes; 93.81% used; 114372910 free inodes.

server4 `/data`: 377449193472 available bytes; 94.78% used; 224773071 free inodes.

server4 `/tmp`: 110999842816 available bytes; 93.81% used; 114372910 free inodes.

server4 `/var/tmp`: 110999842816 available bytes; 93.81% used; 114372910 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
