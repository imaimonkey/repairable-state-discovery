# V2R cluster inventory

2026-09-27T02:55:22.017165+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315085934592 available bytes; 82.42% used; 112443399 free inodes.

server1 `/home`: 315085934592 available bytes; 82.42% used; 112443399 free inodes.

server1 `/tmp`: 315085934592 available bytes; 82.42% used; 112443399 free inodes.

server1 `/var/tmp`: 315085934592 available bytes; 82.42% used; 112443399 free inodes.

server1 `/mnt/raid5`: 636812517376 available bytes; 97.08% used; 337401399 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17636241408 available bytes; 99.02% used; 110365010 free inodes.

server2 `/home`: 17636241408 available bytes; 99.02% used; 110365010 free inodes.

server2 `/tmp`: 17636241408 available bytes; 99.02% used; 110365010 free inodes.

server2 `/var/tmp`: 17636241408 available bytes; 99.02% used; 110365010 free inodes.

server2 `/mnt/raid5`: 580260667392 available bytes; 95.99% used; 444884006 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78709645312 available bytes; 95.61% used; 114062956 free inodes.

server3 `/home`: 78709645312 available bytes; 95.61% used; 114062956 free inodes.

server3 `/data`: 1336577081344 available bytes; 81.53% used; 225761900 free inodes.

server3 `/tmp`: 78709645312 available bytes; 95.61% used; 114062956 free inodes.

server3 `/var/tmp`: 78709645312 available bytes; 95.61% used; 114062956 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111035650048 available bytes; 93.80% used; 114373246 free inodes.

server4 `/home`: 111035650048 available bytes; 93.80% used; 114373246 free inodes.

server4 `/data`: 396902694912 available bytes; 94.51% used; 224781312 free inodes.

server4 `/tmp`: 111035650048 available bytes; 93.80% used; 114373246 free inodes.

server4 `/var/tmp`: 111035650048 available bytes; 93.80% used; 114373246 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
