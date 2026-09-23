# V2R cluster inventory

2026-09-23T23:53:48.661351+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325584150528 available bytes; 81.84% used; 112500978 free inodes.

server1 `/home`: 325584150528 available bytes; 81.84% used; 112500978 free inodes.

server1 `/tmp`: 325584150528 available bytes; 81.84% used; 112500978 free inodes.

server1 `/var/tmp`: 325584150528 available bytes; 81.84% used; 112500978 free inodes.

server1 `/mnt/raid5`: 1293228298240 available bytes; 94.07% used; 337735426 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41022640128 available bytes; 97.71% used; 110432470 free inodes.

server2 `/home`: 41022640128 available bytes; 97.71% used; 110432470 free inodes.

server2 `/tmp`: 41022640128 available bytes; 97.71% used; 110432470 free inodes.

server2 `/var/tmp`: 41022640128 available bytes; 97.71% used; 110432470 free inodes.

server2 `/mnt/raid5`: 533724479488 available bytes; 96.31% used; 445204569 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292808134656 available bytes; 83.66% used; 114214059 free inodes.

server3 `/home`: 292808134656 available bytes; 83.66% used; 114214059 free inodes.

server3 `/data`: 82283380736 available bytes; 98.86% used; 225844947 free inodes.

server3 `/tmp`: 292808134656 available bytes; 83.66% used; 114214059 free inodes.

server3 `/var/tmp`: 292808134656 available bytes; 83.66% used; 114214059 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106152452096 available bytes; 94.08% used; 114351491 free inodes.

server4 `/home`: 106152452096 available bytes; 94.08% used; 114351491 free inodes.

server4 `/data`: 292959637504 available bytes; 95.95% used; 225416964 free inodes.

server4 `/tmp`: 106152452096 available bytes; 94.08% used; 114351491 free inodes.

server4 `/var/tmp`: 106152452096 available bytes; 94.08% used; 114351491 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
