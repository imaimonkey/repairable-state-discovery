# V2R cluster inventory

2026-09-27T03:07:33.167104+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315086041088 available bytes; 82.42% used; 112443039 free inodes.

server1 `/home`: 315086041088 available bytes; 82.42% used; 112443039 free inodes.

server1 `/tmp`: 315086041088 available bytes; 82.42% used; 112443039 free inodes.

server1 `/var/tmp`: 315086041088 available bytes; 82.42% used; 112443039 free inodes.

server1 `/mnt/raid5`: 636810235904 available bytes; 97.08% used; 337401386 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17634238464 available bytes; 99.02% used; 110365005 free inodes.

server2 `/home`: 17634238464 available bytes; 99.02% used; 110365005 free inodes.

server2 `/tmp`: 17634238464 available bytes; 99.02% used; 110365005 free inodes.

server2 `/var/tmp`: 17634238464 available bytes; 99.02% used; 110365005 free inodes.

server2 `/mnt/raid5`: 579866902528 available bytes; 95.99% used; 444883407 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78706257920 available bytes; 95.61% used; 114062940 free inodes.

server3 `/home`: 78706257920 available bytes; 95.61% used; 114062940 free inodes.

server3 `/data`: 1336547508224 available bytes; 81.53% used; 225761750 free inodes.

server3 `/tmp`: 78706257920 available bytes; 95.61% used; 114062940 free inodes.

server3 `/var/tmp`: 78706257920 available bytes; 95.61% used; 114062940 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111028830208 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111028830208 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 395234971648 available bytes; 94.54% used; 224781027 free inodes.

server4 `/tmp`: 111028830208 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111028830208 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
