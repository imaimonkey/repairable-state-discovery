# V2R cluster inventory

2026-09-23T22:02:51.946926+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325709963264 available bytes; 81.83% used; 112501413 free inodes.

server1 `/home`: 325709963264 available bytes; 81.83% used; 112501413 free inodes.

server1 `/tmp`: 325709963264 available bytes; 81.83% used; 112501413 free inodes.

server1 `/var/tmp`: 325709963264 available bytes; 81.83% used; 112501413 free inodes.

server1 `/mnt/raid5`: 1388118585344 available bytes; 93.63% used; 337739883 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41101619200 available bytes; 97.71% used; 110432652 free inodes.

server2 `/home`: 41101619200 available bytes; 97.71% used; 110432652 free inodes.

server2 `/tmp`: 41101619200 available bytes; 97.71% used; 110432652 free inodes.

server2 `/var/tmp`: 41101619200 available bytes; 97.71% used; 110432652 free inodes.

server2 `/mnt/raid5`: 537496018944 available bytes; 96.29% used; 445207452 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293044867072 available bytes; 83.65% used; 114223379 free inodes.

server3 `/home`: 293044867072 available bytes; 83.65% used; 114223379 free inodes.

server3 `/data`: 82453139456 available bytes; 98.86% used; 225847830 free inodes.

server3 `/tmp`: 293044867072 available bytes; 83.65% used; 114223379 free inodes.

server3 `/var/tmp`: 293044867072 available bytes; 83.65% used; 114223379 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106443788288 available bytes; 94.06% used; 114355523 free inodes.

server4 `/home`: 106443788288 available bytes; 94.06% used; 114355523 free inodes.

server4 `/data`: 300196241408 available bytes; 95.85% used; 225444469 free inodes.

server4 `/tmp`: 106443788288 available bytes; 94.06% used; 114355523 free inodes.

server4 `/var/tmp`: 106443788288 available bytes; 94.06% used; 114355523 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
