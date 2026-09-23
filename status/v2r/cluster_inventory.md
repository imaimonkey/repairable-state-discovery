# V2R cluster inventory

2026-09-23T23:47:36.709929+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325591642112 available bytes; 81.84% used; 112501055 free inodes.

server1 `/home`: 325591642112 available bytes; 81.84% used; 112501055 free inodes.

server1 `/tmp`: 325591642112 available bytes; 81.84% used; 112501055 free inodes.

server1 `/var/tmp`: 325591642112 available bytes; 81.84% used; 112501055 free inodes.

server1 `/mnt/raid5`: 1298941054976 available bytes; 94.04% used; 337735731 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41027301376 available bytes; 97.71% used; 110432492 free inodes.

server2 `/home`: 41027301376 available bytes; 97.71% used; 110432492 free inodes.

server2 `/tmp`: 41027301376 available bytes; 97.71% used; 110432492 free inodes.

server2 `/var/tmp`: 41027301376 available bytes; 97.71% used; 110432492 free inodes.

server2 `/mnt/raid5`: 533914775552 available bytes; 96.31% used; 445204760 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292810620928 available bytes; 83.66% used; 114214057 free inodes.

server3 `/home`: 292810620928 available bytes; 83.66% used; 114214057 free inodes.

server3 `/data`: 82294140928 available bytes; 98.86% used; 225845062 free inodes.

server3 `/tmp`: 292810620928 available bytes; 83.66% used; 114214057 free inodes.

server3 `/var/tmp`: 292810620928 available bytes; 83.66% used; 114214057 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106175254528 available bytes; 94.08% used; 114351715 free inodes.

server4 `/home`: 106175254528 available bytes; 94.08% used; 114351715 free inodes.

server4 `/data`: 292976779264 available bytes; 95.95% used; 225418776 free inodes.

server4 `/tmp`: 106175254528 available bytes; 94.08% used; 114351715 free inodes.

server4 `/var/tmp`: 106175254528 available bytes; 94.08% used; 114351715 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
