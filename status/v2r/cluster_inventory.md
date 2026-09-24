# V2R cluster inventory

2026-09-24T01:04:59.465138+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325524873216 available bytes; 81.84% used; 112500217 free inodes.

server1 `/home`: 325524873216 available bytes; 81.84% used; 112500217 free inodes.

server1 `/tmp`: 325524873216 available bytes; 81.84% used; 112500217 free inodes.

server1 `/var/tmp`: 325524873216 available bytes; 81.84% used; 112500217 free inodes.

server1 `/mnt/raid5`: 999723704320 available bytes; 95.41% used; 337734855 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40968445952 available bytes; 97.71% used; 110432192 free inodes.

server2 `/home`: 40968445952 available bytes; 97.71% used; 110432192 free inodes.

server2 `/tmp`: 40968445952 available bytes; 97.71% used; 110432192 free inodes.

server2 `/var/tmp`: 40968445952 available bytes; 97.71% used; 110432192 free inodes.

server2 `/mnt/raid5`: 531691048960 available bytes; 96.33% used; 445202145 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292375089152 available bytes; 83.68% used; 114188628 free inodes.

server3 `/home`: 292375089152 available bytes; 83.68% used; 114188628 free inodes.

server3 `/data`: 82085072896 available bytes; 98.87% used; 225843151 free inodes.

server3 `/tmp`: 292375089152 available bytes; 83.68% used; 114188628 free inodes.

server3 `/var/tmp`: 292375089152 available bytes; 83.68% used; 114188628 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106012487680 available bytes; 94.08% used; 114349421 free inodes.

server4 `/home`: 106012487680 available bytes; 94.08% used; 114349421 free inodes.

server4 `/data`: 292722188288 available bytes; 95.95% used; 225405418 free inodes.

server4 `/tmp`: 106012487680 available bytes; 94.08% used; 114349421 free inodes.

server4 `/var/tmp`: 106012487680 available bytes; 94.08% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
