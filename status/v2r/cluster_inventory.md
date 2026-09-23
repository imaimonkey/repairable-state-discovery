# V2R cluster inventory

2026-09-23T20:27:38.903848+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325735587840 available bytes; 81.83% used; 112501759 free inodes.

server1 `/home`: 325735587840 available bytes; 81.83% used; 112501759 free inodes.

server1 `/tmp`: 325735587840 available bytes; 81.83% used; 112501759 free inodes.

server1 `/var/tmp`: 325735587840 available bytes; 81.83% used; 112501759 free inodes.

server1 `/mnt/raid5`: 1388274716672 available bytes; 93.63% used; 337740966 free inodes.
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41141702656 available bytes; 97.70% used; 110432810 free inodes.

server2 `/home`: 41141702656 available bytes; 97.70% used; 110432810 free inodes.

server2 `/tmp`: 41141702656 available bytes; 97.70% used; 110432810 free inodes.

server2 `/var/tmp`: 41141702656 available bytes; 97.70% used; 110432810 free inodes.

server2 `/mnt/raid5`: 540446052352 available bytes; 96.27% used; 445210509 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292829003776 available bytes; 83.66% used; 114205485 free inodes.

server3 `/home`: 292829003776 available bytes; 83.66% used; 114205485 free inodes.

server3 `/data`: 52602482688 available bytes; 99.27% used; 225843710 free inodes.

server3 `/tmp`: 292829003776 available bytes; 83.66% used; 114205485 free inodes.

server3 `/var/tmp`: 292829003776 available bytes; 83.66% used; 114205485 free inodes.
| server4 | True | ['0', '1', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106527711232 available bytes; 94.06% used; 114356192 free inodes.

server4 `/home`: 106527711232 available bytes; 94.06% used; 114356192 free inodes.

server4 `/data`: 0 available bytes; 100.00% used; 225457590 free inodes.

server4 `/tmp`: 106527711232 available bytes; 94.06% used; 114356192 free inodes.

server4 `/var/tmp`: 106527711232 available bytes; 94.06% used; 114356192 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
