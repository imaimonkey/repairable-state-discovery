# V2R cluster inventory

2026-09-26T05:10:34.998514+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318398869504 available bytes; 82.24% used; 112476282 free inodes.

server1 `/home`: 318398869504 available bytes; 82.24% used; 112476282 free inodes.

server1 `/tmp`: 318398869504 available bytes; 82.24% used; 112476282 free inodes.

server1 `/var/tmp`: 318398869504 available bytes; 82.24% used; 112476282 free inodes.

server1 `/mnt/raid5`: 319174082560 available bytes; 98.54% used; 337543689 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22927564800 available bytes; 98.72% used; 110406192 free inodes.

server2 `/home`: 22927564800 available bytes; 98.72% used; 110406192 free inodes.

server2 `/tmp`: 22927564800 available bytes; 98.72% used; 110406192 free inodes.

server2 `/var/tmp`: 22927564800 available bytes; 98.72% used; 110406192 free inodes.

server2 `/mnt/raid5`: 263596691456 available bytes; 98.18% used; 445049300 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84080340992 available bytes; 95.31% used; 114165711 free inodes.

server3 `/home`: 84080340992 available bytes; 95.31% used; 114165711 free inodes.

server3 `/data`: 124604801024 available bytes; 98.28% used; 225825267 free inodes.

server3 `/tmp`: 84080340992 available bytes; 95.31% used; 114165711 free inodes.

server3 `/var/tmp`: 84080340992 available bytes; 95.31% used; 114165711 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106095493120 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106095493120 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 106994049024 available bytes; 98.52% used; 224929217 free inodes.

server4 `/tmp`: 106095493120 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106095493120 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
