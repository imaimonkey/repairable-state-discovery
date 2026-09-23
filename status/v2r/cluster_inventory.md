# V2R cluster inventory

2026-09-23T21:24:19.299281+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325719150592 available bytes; 81.83% used; 112501428 free inodes.

server1 `/home`: 325719150592 available bytes; 81.83% used; 112501428 free inodes.

server1 `/tmp`: 325719150592 available bytes; 81.83% used; 112501428 free inodes.

server1 `/var/tmp`: 325719150592 available bytes; 81.83% used; 112501428 free inodes.

server1 `/mnt/raid5`: 1388135149568 available bytes; 93.63% used; 337739964 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41109942272 available bytes; 97.71% used; 110432685 free inodes.

server2 `/home`: 41109942272 available bytes; 97.71% used; 110432685 free inodes.

server2 `/tmp`: 41109942272 available bytes; 97.71% used; 110432685 free inodes.

server2 `/var/tmp`: 41109942272 available bytes; 97.71% used; 110432685 free inodes.

server2 `/mnt/raid5`: 538699243520 available bytes; 96.28% used; 445208814 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292955721728 available bytes; 83.65% used; 114208564 free inodes.

server3 `/home`: 292955721728 available bytes; 83.65% used; 114208564 free inodes.

server3 `/data`: 52293070848 available bytes; 99.28% used; 225848917 free inodes.

server3 `/tmp`: 292955721728 available bytes; 83.65% used; 114208564 free inodes.

server3 `/var/tmp`: 292955721728 available bytes; 83.65% used; 114208564 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106484977664 available bytes; 94.06% used; 114356015 free inodes.

server4 `/home`: 106484977664 available bytes; 94.06% used; 114356015 free inodes.

server4 `/data`: 300373532672 available bytes; 95.85% used; 225452086 free inodes.

server4 `/tmp`: 106484977664 available bytes; 94.06% used; 114356015 free inodes.

server4 `/var/tmp`: 106484977664 available bytes; 94.06% used; 114356015 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
