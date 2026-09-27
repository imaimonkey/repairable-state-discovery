# V2R cluster inventory

2026-09-27T02:53:50.618423+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314959613952 available bytes; 82.43% used; 112443374 free inodes.

server1 `/home`: 314959613952 available bytes; 82.43% used; 112443374 free inodes.

server1 `/tmp`: 314959613952 available bytes; 82.43% used; 112443374 free inodes.

server1 `/var/tmp`: 314959613952 available bytes; 82.43% used; 112443374 free inodes.

server1 `/mnt/raid5`: 636812460032 available bytes; 97.08% used; 337401409 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17636384768 available bytes; 99.02% used; 110365008 free inodes.

server2 `/home`: 17636384768 available bytes; 99.02% used; 110365008 free inodes.

server2 `/tmp`: 17636384768 available bytes; 99.02% used; 110365008 free inodes.

server2 `/var/tmp`: 17636384768 available bytes; 99.02% used; 110365008 free inodes.

server2 `/mnt/raid5`: 580305907712 available bytes; 95.99% used; 444884188 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78708965376 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78708965376 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1336590929920 available bytes; 81.53% used; 225762005 free inodes.

server3 `/tmp`: 78708965376 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78708965376 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111035682816 available bytes; 93.80% used; 114373246 free inodes.

server4 `/home`: 111035682816 available bytes; 93.80% used; 114373246 free inodes.

server4 `/data`: 396904062976 available bytes; 94.51% used; 224781323 free inodes.

server4 `/tmp`: 111035682816 available bytes; 93.80% used; 114373246 free inodes.

server4 `/var/tmp`: 111035682816 available bytes; 93.80% used; 114373246 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
