# V2R cluster inventory

2026-09-23T23:50:16.255272+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325588504576 available bytes; 81.84% used; 112501026 free inodes.

server1 `/home`: 325588504576 available bytes; 81.84% used; 112501026 free inodes.

server1 `/tmp`: 325588504576 available bytes; 81.84% used; 112501026 free inodes.

server1 `/var/tmp`: 325588504576 available bytes; 81.84% used; 112501026 free inodes.

server1 `/mnt/raid5`: 1308344258560 available bytes; 94.00% used; 337735730 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41025028096 available bytes; 97.71% used; 110432483 free inodes.

server2 `/home`: 41025028096 available bytes; 97.71% used; 110432483 free inodes.

server2 `/tmp`: 41025028096 available bytes; 97.71% used; 110432483 free inodes.

server2 `/var/tmp`: 41025028096 available bytes; 97.71% used; 110432483 free inodes.

server2 `/mnt/raid5`: 533835513856 available bytes; 96.31% used; 445204699 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292810182656 available bytes; 83.66% used; 114214057 free inodes.

server3 `/home`: 292810182656 available bytes; 83.66% used; 114214057 free inodes.

server3 `/data`: 82291990528 available bytes; 98.86% used; 225845028 free inodes.

server3 `/tmp`: 292810182656 available bytes; 83.66% used; 114214057 free inodes.

server3 `/var/tmp`: 292810182656 available bytes; 83.66% used; 114214057 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106169057280 available bytes; 94.08% used; 114351619 free inodes.

server4 `/home`: 106169057280 available bytes; 94.08% used; 114351619 free inodes.

server4 `/data`: 292963631104 available bytes; 95.95% used; 225417920 free inodes.

server4 `/tmp`: 106169057280 available bytes; 94.08% used; 114351619 free inodes.

server4 `/var/tmp`: 106169057280 available bytes; 94.08% used; 114351619 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
