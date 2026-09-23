# V2R cluster inventory

2026-09-23T23:47:10.876188+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325593063424 available bytes; 81.84% used; 112501052 free inodes.

server1 `/home`: 325593063424 available bytes; 81.84% used; 112501052 free inodes.

server1 `/tmp`: 325593063424 available bytes; 81.84% used; 112501052 free inodes.

server1 `/var/tmp`: 325593063424 available bytes; 81.84% used; 112501052 free inodes.

server1 `/mnt/raid5`: 1305987284992 available bytes; 94.01% used; 337735755 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41033392128 available bytes; 97.71% used; 110432498 free inodes.

server2 `/home`: 41033392128 available bytes; 97.71% used; 110432498 free inodes.

server2 `/tmp`: 41033392128 available bytes; 97.71% used; 110432498 free inodes.

server2 `/var/tmp`: 41033392128 available bytes; 97.71% used; 110432498 free inodes.

server2 `/mnt/raid5`: 533919985664 available bytes; 96.31% used; 445204764 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292810674176 available bytes; 83.66% used; 114214057 free inodes.

server3 `/home`: 292810674176 available bytes; 83.66% used; 114214057 free inodes.

server3 `/data`: 82295009280 available bytes; 98.86% used; 225845079 free inodes.

server3 `/tmp`: 292810674176 available bytes; 83.66% used; 114214057 free inodes.

server3 `/var/tmp`: 292810674176 available bytes; 83.66% used; 114214057 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106176282624 available bytes; 94.07% used; 114351731 free inodes.

server4 `/home`: 106176282624 available bytes; 94.07% used; 114351731 free inodes.

server4 `/data`: 292978937856 available bytes; 95.95% used; 225418920 free inodes.

server4 `/tmp`: 106176282624 available bytes; 94.07% used; 114351731 free inodes.

server4 `/var/tmp`: 106176282624 available bytes; 94.07% used; 114351731 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
