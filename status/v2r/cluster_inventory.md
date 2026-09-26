# V2R cluster inventory

2026-09-26T16:47:39.410829+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318125645824 available bytes; 82.25% used; 112473834 free inodes.

server1 `/home`: 318125645824 available bytes; 82.25% used; 112473834 free inodes.

server1 `/tmp`: 318125645824 available bytes; 82.25% used; 112473834 free inodes.

server1 `/var/tmp`: 318125645824 available bytes; 82.25% used; 112473834 free inodes.

server1 `/mnt/raid5`: 654089826304 available bytes; 97.00% used; 337531262 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18024046592 available bytes; 98.99% used; 110367553 free inodes.

server2 `/home`: 18024046592 available bytes; 98.99% used; 110367553 free inodes.

server2 `/tmp`: 18024046592 available bytes; 98.99% used; 110367553 free inodes.

server2 `/var/tmp`: 18024046592 available bytes; 98.99% used; 110367553 free inodes.

server2 `/mnt/raid5`: 607222497280 available bytes; 95.80% used; 444970767 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81275109376 available bytes; 95.46% used; 114065345 free inodes.

server3 `/home`: 81275109376 available bytes; 95.46% used; 114065345 free inodes.

server3 `/data`: 1349249814528 available bytes; 81.35% used; 225830016 free inodes.

server3 `/tmp`: 81275109376 available bytes; 95.46% used; 114065345 free inodes.

server3 `/var/tmp`: 81275109376 available bytes; 95.46% used; 114065345 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105953153024 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105953153024 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410530451456 available bytes; 94.33% used; 224824570 free inodes.

server4 `/tmp`: 105953153024 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105953153024 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
