# V2R cluster inventory

2026-09-24T07:24:54.494778+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324451393536 available bytes; 81.90% used; 112491186 free inodes.

server1 `/home`: 324451393536 available bytes; 81.90% used; 112491186 free inodes.

server1 `/tmp`: 324451393536 available bytes; 81.90% used; 112491186 free inodes.

server1 `/var/tmp`: 324451393536 available bytes; 81.90% used; 112491186 free inodes.

server1 `/mnt/raid5`: 517412540416 available bytes; 97.63% used; 337722811 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57851330560 available bytes; 96.77% used; 110431112 free inodes.

server2 `/home`: 57851330560 available bytes; 96.77% used; 110431112 free inodes.

server2 `/tmp`: 57851330560 available bytes; 96.77% used; 110431112 free inodes.

server2 `/var/tmp`: 57851330560 available bytes; 96.77% used; 110431112 free inodes.

server2 `/mnt/raid5`: 518426882048 available bytes; 96.42% used; 445180900 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126728826880 available bytes; 92.93% used; 114173029 free inodes.

server3 `/home`: 126728826880 available bytes; 92.93% used; 114173029 free inodes.

server3 `/data`: 139029225472 available bytes; 98.08% used; 225834230 free inodes.

server3 `/tmp`: 126728826880 available bytes; 92.93% used; 114173029 free inodes.

server3 `/var/tmp`: 126728826880 available bytes; 92.93% used; 114173029 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780940800 available bytes; 94.10% used; 114349193 free inodes.

server4 `/home`: 105780940800 available bytes; 94.10% used; 114349193 free inodes.

server4 `/data`: 286561341440 available bytes; 96.04% used; 225366884 free inodes.

server4 `/tmp`: 105780940800 available bytes; 94.10% used; 114349193 free inodes.

server4 `/var/tmp`: 105780940800 available bytes; 94.10% used; 114349193 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
