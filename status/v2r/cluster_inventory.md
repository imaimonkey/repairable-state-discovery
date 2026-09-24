# V2R cluster inventory

2026-09-24T00:55:40.862918+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325528846336 available bytes; 81.84% used; 112500321 free inodes.

server1 `/home`: 325528846336 available bytes; 81.84% used; 112500321 free inodes.

server1 `/tmp`: 325528846336 available bytes; 81.84% used; 112500321 free inodes.

server1 `/var/tmp`: 325528846336 available bytes; 81.84% used; 112500321 free inodes.

server1 `/mnt/raid5`: 1038126604288 available bytes; 95.24% used; 337734811 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40974188544 available bytes; 97.71% used; 110432231 free inodes.

server2 `/home`: 40974188544 available bytes; 97.71% used; 110432231 free inodes.

server2 `/tmp`: 40974188544 available bytes; 97.71% used; 110432231 free inodes.

server2 `/var/tmp`: 40974188544 available bytes; 97.71% used; 110432231 free inodes.

server2 `/mnt/raid5`: 531993747456 available bytes; 96.32% used; 445202520 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292703842304 available bytes; 83.67% used; 114211347 free inodes.

server3 `/home`: 292703842304 available bytes; 83.67% used; 114211347 free inodes.

server3 `/data`: 82158854144 available bytes; 98.86% used; 225843348 free inodes.

server3 `/tmp`: 292703842304 available bytes; 83.67% used; 114211347 free inodes.

server3 `/var/tmp`: 292703842304 available bytes; 83.67% used; 114211347 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106027950080 available bytes; 94.08% used; 114349661 free inodes.

server4 `/home`: 106027950080 available bytes; 94.08% used; 114349661 free inodes.

server4 `/data`: 292876427264 available bytes; 95.95% used; 225414551 free inodes.

server4 `/tmp`: 106027950080 available bytes; 94.08% used; 114349661 free inodes.

server4 `/var/tmp`: 106027950080 available bytes; 94.08% used; 114349661 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
