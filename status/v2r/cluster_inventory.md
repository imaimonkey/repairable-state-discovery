# V2R cluster inventory

2026-09-23T23:30:38.950102+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325656698880 available bytes; 81.83% used; 112501494 free inodes.

server1 `/home`: 325656698880 available bytes; 81.83% used; 112501494 free inodes.

server1 `/tmp`: 325656698880 available bytes; 81.83% used; 112501494 free inodes.

server1 `/var/tmp`: 325656698880 available bytes; 81.83% used; 112501494 free inodes.

server1 `/mnt/raid5`: 1370771812352 available bytes; 93.71% used; 337739645 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41037594624 available bytes; 97.71% used; 110432569 free inodes.

server2 `/home`: 41037594624 available bytes; 97.71% used; 110432569 free inodes.

server2 `/tmp`: 41037594624 available bytes; 97.71% used; 110432569 free inodes.

server2 `/var/tmp`: 41037594624 available bytes; 97.71% used; 110432569 free inodes.

server2 `/mnt/raid5`: 533928939520 available bytes; 96.31% used; 445205470 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292867198976 available bytes; 83.66% used; 114214453 free inodes.

server3 `/home`: 292867198976 available bytes; 83.66% used; 114214453 free inodes.

server3 `/data`: 82309926912 available bytes; 98.86% used; 225845762 free inodes.

server3 `/tmp`: 292867198976 available bytes; 83.66% used; 114214453 free inodes.

server3 `/var/tmp`: 292867198976 available bytes; 83.66% used; 114214453 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106228199424 available bytes; 94.07% used; 114352339 free inodes.

server4 `/home`: 106228199424 available bytes; 94.07% used; 114352339 free inodes.

server4 `/data`: 293076717568 available bytes; 95.95% used; 225423824 free inodes.

server4 `/tmp`: 106228199424 available bytes; 94.07% used; 114352339 free inodes.

server4 `/var/tmp`: 106228199424 available bytes; 94.07% used; 114352339 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
