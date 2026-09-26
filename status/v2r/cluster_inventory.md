# V2R cluster inventory

2026-09-26T16:53:44.908611+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315638730752 available bytes; 82.39% used; 112446012 free inodes.

server1 `/home`: 315638730752 available bytes; 82.39% used; 112446012 free inodes.

server1 `/tmp`: 315638730752 available bytes; 82.39% used; 112446012 free inodes.

server1 `/var/tmp`: 315638730752 available bytes; 82.39% used; 112446012 free inodes.

server1 `/mnt/raid5`: 645896192000 available bytes; 97.04% used; 337469725 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 18023845888 available bytes; 98.99% used; 110367559 free inodes.

server2 `/home`: 18023845888 available bytes; 98.99% used; 110367559 free inodes.

server2 `/tmp`: 18023845888 available bytes; 98.99% used; 110367559 free inodes.

server2 `/var/tmp`: 18023845888 available bytes; 98.99% used; 110367559 free inodes.

server2 `/mnt/raid5`: 607058710528 available bytes; 95.81% used; 444970607 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 81273298944 available bytes; 95.46% used; 114065346 free inodes.

server3 `/home`: 81273298944 available bytes; 95.46% used; 114065346 free inodes.

server3 `/data`: 1349289963520 available bytes; 81.35% used; 225829431 free inodes.

server3 `/tmp`: 81273298944 available bytes; 95.46% used; 114065346 free inodes.

server3 `/var/tmp`: 81273298944 available bytes; 95.46% used; 114065346 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105953017856 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105953017856 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410524205056 available bytes; 94.33% used; 224824520 free inodes.

server4 `/tmp`: 105953017856 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105953017856 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
