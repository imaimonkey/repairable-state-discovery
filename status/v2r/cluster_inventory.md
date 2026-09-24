# V2R cluster inventory

2026-09-24T00:04:38.385414+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325578002432 available bytes; 81.84% used; 112500864 free inodes.

server1 `/home`: 325578002432 available bytes; 81.84% used; 112500864 free inodes.

server1 `/tmp`: 325578002432 available bytes; 81.84% used; 112500864 free inodes.

server1 `/var/tmp`: 325578002432 available bytes; 81.84% used; 112500864 free inodes.

server1 `/mnt/raid5`: 1248497184768 available bytes; 94.27% used; 337735410 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41010802688 available bytes; 97.71% used; 110432430 free inodes.

server2 `/home`: 41010802688 available bytes; 97.71% used; 110432430 free inodes.

server2 `/tmp`: 41010802688 available bytes; 97.71% used; 110432430 free inodes.

server2 `/var/tmp`: 41010802688 available bytes; 97.71% used; 110432430 free inodes.

server2 `/mnt/raid5`: 533463097344 available bytes; 96.31% used; 445203997 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292789407744 available bytes; 83.66% used; 114213300 free inodes.

server3 `/home`: 292789407744 available bytes; 83.66% used; 114213300 free inodes.

server3 `/data`: 82264788992 available bytes; 98.86% used; 225844698 free inodes.

server3 `/tmp`: 292789407744 available bytes; 83.66% used; 114213300 free inodes.

server3 `/var/tmp`: 292789407744 available bytes; 83.66% used; 114213300 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106128928768 available bytes; 94.08% used; 114351115 free inodes.

server4 `/home`: 106128928768 available bytes; 94.08% used; 114351115 free inodes.

server4 `/data`: 292917288960 available bytes; 95.95% used; 225414607 free inodes.

server4 `/tmp`: 106128928768 available bytes; 94.08% used; 114351115 free inodes.

server4 `/var/tmp`: 106128928768 available bytes; 94.08% used; 114351115 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
