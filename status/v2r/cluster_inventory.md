# V2R cluster inventory

2026-09-24T03:57:12.484384+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324732022784 available bytes; 81.88% used; 112493613 free inodes.

server1 `/home`: 324732022784 available bytes; 81.88% used; 112493613 free inodes.

server1 `/tmp`: 324732022784 available bytes; 81.88% used; 112493613 free inodes.

server1 `/var/tmp`: 324732022784 available bytes; 81.88% used; 112493613 free inodes.

server1 `/mnt/raid5`: 411799404544 available bytes; 98.11% used; 337724789 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40814460928 available bytes; 97.72% used; 110430900 free inodes.

server2 `/home`: 40814460928 available bytes; 97.72% used; 110430900 free inodes.

server2 `/tmp`: 40814460928 available bytes; 97.72% used; 110430900 free inodes.

server2 `/var/tmp`: 40814460928 available bytes; 97.72% used; 110430900 free inodes.

server2 `/mnt/raid5`: 526399840256 available bytes; 96.36% used; 445197227 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292383158272 available bytes; 83.68% used; 114201257 free inodes.

server3 `/home`: 292383158272 available bytes; 83.68% used; 114201257 free inodes.

server3 `/data`: 33867718656 available bytes; 99.53% used; 225842452 free inodes.

server3 `/tmp`: 292383158272 available bytes; 83.68% used; 114201257 free inodes.

server3 `/var/tmp`: 292383158272 available bytes; 83.68% used; 114201257 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105791496192 available bytes; 94.10% used; 114349501 free inodes.

server4 `/home`: 105791496192 available bytes; 94.10% used; 114349501 free inodes.

server4 `/data`: 258349514752 available bytes; 96.43% used; 225382430 free inodes.

server4 `/tmp`: 105791496192 available bytes; 94.10% used; 114349501 free inodes.

server4 `/var/tmp`: 105791496192 available bytes; 94.10% used; 114349501 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
