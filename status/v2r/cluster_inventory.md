# V2R cluster inventory

2026-09-27T02:47:44.521969+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315083718656 available bytes; 82.42% used; 112443415 free inodes.

server1 `/home`: 315083718656 available bytes; 82.42% used; 112443415 free inodes.

server1 `/tmp`: 315083718656 available bytes; 82.42% used; 112443415 free inodes.

server1 `/var/tmp`: 315083718656 available bytes; 82.42% used; 112443415 free inodes.

server1 `/mnt/raid5`: 636848369664 available bytes; 97.08% used; 337401559 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17626439680 available bytes; 99.02% used; 110365008 free inodes.

server2 `/home`: 17626439680 available bytes; 99.02% used; 110365008 free inodes.

server2 `/tmp`: 17626439680 available bytes; 99.02% used; 110365008 free inodes.

server2 `/var/tmp`: 17626439680 available bytes; 99.02% used; 110365008 free inodes.

server2 `/mnt/raid5`: 580461514752 available bytes; 95.99% used; 444883984 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78710304768 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78710304768 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1336604643328 available bytes; 81.53% used; 225762102 free inodes.

server3 `/tmp`: 78710304768 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78710304768 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111035895808 available bytes; 93.80% used; 114373255 free inodes.

server4 `/home`: 111035895808 available bytes; 93.80% used; 114373255 free inodes.

server4 `/data`: 396953067520 available bytes; 94.51% used; 224781460 free inodes.

server4 `/tmp`: 111035895808 available bytes; 93.80% used; 114373255 free inodes.

server4 `/var/tmp`: 111035895808 available bytes; 93.80% used; 114373255 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
