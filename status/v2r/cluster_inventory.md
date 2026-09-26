# V2R cluster inventory

2026-09-26T16:29:35.918344+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318131712000 available bytes; 82.25% used; 112473895 free inodes.

server1 `/home`: 318131712000 available bytes; 82.25% used; 112473895 free inodes.

server1 `/tmp`: 318131712000 available bytes; 82.25% used; 112473895 free inodes.

server1 `/var/tmp`: 318131712000 available bytes; 82.25% used; 112473895 free inodes.

server1 `/mnt/raid5`: 654102810624 available bytes; 97.00% used; 337531410 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18029768704 available bytes; 98.99% used; 110367537 free inodes.

server2 `/home`: 18029768704 available bytes; 98.99% used; 110367537 free inodes.

server2 `/tmp`: 18029768704 available bytes; 98.99% used; 110367537 free inodes.

server2 `/var/tmp`: 18029768704 available bytes; 98.99% used; 110367537 free inodes.

server2 `/mnt/raid5`: 607748354048 available bytes; 95.80% used; 444971393 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81577259008 available bytes; 95.45% used; 114077211 free inodes.

server3 `/home`: 81577259008 available bytes; 95.45% used; 114077211 free inodes.

server3 `/data`: 1349336010752 available bytes; 81.35% used; 225830717 free inodes.

server3 `/tmp`: 81577259008 available bytes; 95.45% used; 114077211 free inodes.

server3 `/var/tmp`: 81577259008 available bytes; 95.45% used; 114077211 free inodes.
| server4 | True | ['0', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953533952 available bytes; 94.09% used; 114347865 free inodes.

server4 `/home`: 105953533952 available bytes; 94.09% used; 114347865 free inodes.

server4 `/data`: 410613645312 available bytes; 94.33% used; 224824693 free inodes.

server4 `/tmp`: 105953533952 available bytes; 94.09% used; 114347865 free inodes.

server4 `/var/tmp`: 105953533952 available bytes; 94.09% used; 114347865 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
