# V2R cluster inventory

2026-09-27T04:27:41.146213+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314907684864 available bytes; 82.43% used; 112443033 free inodes.

server1 `/home`: 314907684864 available bytes; 82.43% used; 112443033 free inodes.

server1 `/tmp`: 314907684864 available bytes; 82.43% used; 112443033 free inodes.

server1 `/var/tmp`: 314907684864 available bytes; 82.43% used; 112443033 free inodes.

server1 `/mnt/raid5`: 636066193408 available bytes; 97.08% used; 337400352 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17623920640 available bytes; 99.02% used; 110365003 free inodes.

server2 `/home`: 17623920640 available bytes; 99.02% used; 110365003 free inodes.

server2 `/tmp`: 17623920640 available bytes; 99.02% used; 110365003 free inodes.

server2 `/var/tmp`: 17623920640 available bytes; 99.02% used; 110365003 free inodes.

server2 `/mnt/raid5`: 575840501760 available bytes; 96.02% used; 444879469 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78696624128 available bytes; 95.61% used; 114062929 free inodes.

server3 `/home`: 78696624128 available bytes; 95.61% used; 114062929 free inodes.

server3 `/data`: 1335096963072 available bytes; 81.55% used; 225759221 free inodes.

server3 `/tmp`: 78696624128 available bytes; 95.61% used; 114062929 free inodes.

server3 `/var/tmp`: 78696624128 available bytes; 95.61% used; 114062929 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111018201088 available bytes; 93.80% used; 114372937 free inodes.

server4 `/home`: 111018201088 available bytes; 93.80% used; 114372937 free inodes.

server4 `/data`: 382131957760 available bytes; 94.72% used; 224780559 free inodes.

server4 `/tmp`: 111018201088 available bytes; 93.80% used; 114372937 free inodes.

server4 `/var/tmp`: 111018201088 available bytes; 93.80% used; 114372937 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
