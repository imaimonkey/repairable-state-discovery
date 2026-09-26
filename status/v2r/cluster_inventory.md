# V2R cluster inventory

2026-09-26T02:23:19.609471+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318420287488 available bytes; 82.24% used; 112476288 free inodes.

server1 `/home`: 318420287488 available bytes; 82.24% used; 112476288 free inodes.

server1 `/tmp`: 318420287488 available bytes; 82.24% used; 112476288 free inodes.

server1 `/var/tmp`: 318420287488 available bytes; 82.24% used; 112476288 free inodes.

server1 `/mnt/raid5`: 344982757376 available bytes; 98.42% used; 337546183 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22936457216 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22936457216 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22936457216 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22936457216 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 289189507072 available bytes; 98.00% used; 445054802 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84317450240 available bytes; 95.29% used; 114152370 free inodes.

server3 `/home`: 84317450240 available bytes; 95.29% used; 114152370 free inodes.

server3 `/data`: 124789166080 available bytes; 98.28% used; 225817109 free inodes.

server3 `/tmp`: 84317450240 available bytes; 95.29% used; 114152370 free inodes.

server3 `/var/tmp`: 84317450240 available bytes; 95.29% used; 114152370 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106126864384 available bytes; 94.08% used; 114349423 free inodes.

server4 `/home`: 106126864384 available bytes; 94.08% used; 114349423 free inodes.

server4 `/data`: 130902405120 available bytes; 98.19% used; 224915756 free inodes.

server4 `/tmp`: 106126864384 available bytes; 94.08% used; 114349423 free inodes.

server4 `/var/tmp`: 106126864384 available bytes; 94.08% used; 114349423 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
