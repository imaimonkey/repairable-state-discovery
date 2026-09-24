# V2R cluster inventory

2026-09-24T07:03:07.383615+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324482113536 available bytes; 81.90% used; 112491350 free inodes.

server1 `/home`: 324482113536 available bytes; 81.90% used; 112491350 free inodes.

server1 `/tmp`: 324482113536 available bytes; 81.90% used; 112491350 free inodes.

server1 `/var/tmp`: 324482113536 available bytes; 81.90% used; 112491350 free inodes.

server1 `/mnt/raid5`: 517429350400 available bytes; 97.63% used; 337722837 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57862213632 available bytes; 96.77% used; 110431175 free inodes.

server2 `/home`: 57862213632 available bytes; 96.77% used; 110431175 free inodes.

server2 `/tmp`: 57862213632 available bytes; 96.77% used; 110431175 free inodes.

server2 `/var/tmp`: 57862213632 available bytes; 96.77% used; 110431175 free inodes.

server2 `/mnt/raid5`: 519220002816 available bytes; 96.41% used; 445190900 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126756519936 available bytes; 92.93% used; 114175145 free inodes.

server3 `/home`: 126756519936 available bytes; 92.93% used; 114175145 free inodes.

server3 `/data`: 139179945984 available bytes; 98.08% used; 225834711 free inodes.

server3 `/tmp`: 126756519936 available bytes; 92.93% used; 114175145 free inodes.

server3 `/var/tmp`: 126756519936 available bytes; 92.93% used; 114175145 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105790304256 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105790304256 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 301689524224 available bytes; 95.83% used; 225367660 free inodes.

server4 `/tmp`: 105790304256 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105790304256 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
