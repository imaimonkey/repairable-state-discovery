# V2R cluster inventory

2026-09-24T06:44:02.022245+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324489076736 available bytes; 81.90% used; 112491530 free inodes.

server1 `/home`: 324489076736 available bytes; 81.90% used; 112491530 free inodes.

server1 `/tmp`: 324489076736 available bytes; 81.90% used; 112491530 free inodes.

server1 `/var/tmp`: 324489076736 available bytes; 81.90% used; 112491530 free inodes.

server1 `/mnt/raid5`: 517573017600 available bytes; 97.63% used; 337723687 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57872289792 available bytes; 96.77% used; 110431193 free inodes.

server2 `/home`: 57872289792 available bytes; 96.77% used; 110431193 free inodes.

server2 `/tmp`: 57872289792 available bytes; 96.77% used; 110431193 free inodes.

server2 `/var/tmp`: 57872289792 available bytes; 96.77% used; 110431193 free inodes.

server2 `/mnt/raid5`: 519821422592 available bytes; 96.41% used; 445191557 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126796513280 available bytes; 92.92% used; 114175210 free inodes.

server3 `/home`: 126796513280 available bytes; 92.92% used; 114175210 free inodes.

server3 `/data`: 139360448512 available bytes; 98.07% used; 225835461 free inodes.

server3 `/tmp`: 126796513280 available bytes; 92.92% used; 114175210 free inodes.

server3 `/var/tmp`: 126796513280 available bytes; 92.92% used; 114175210 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105804685312 available bytes; 94.10% used; 114349240 free inodes.

server4 `/home`: 105804685312 available bytes; 94.10% used; 114349240 free inodes.

server4 `/data`: 316208435200 available bytes; 95.63% used; 225368692 free inodes.

server4 `/tmp`: 105804685312 available bytes; 94.10% used; 114349240 free inodes.

server4 `/var/tmp`: 105804685312 available bytes; 94.10% used; 114349240 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
