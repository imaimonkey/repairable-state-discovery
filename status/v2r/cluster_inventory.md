# V2R cluster inventory

2026-09-23T22:13:14.265770+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325705371648 available bytes; 81.83% used; 112501407 free inodes.

server1 `/home`: 325705371648 available bytes; 81.83% used; 112501407 free inodes.

server1 `/tmp`: 325705371648 available bytes; 81.83% used; 112501407 free inodes.

server1 `/var/tmp`: 325705371648 available bytes; 81.83% used; 112501407 free inodes.

server1 `/mnt/raid5`: 1388110020608 available bytes; 93.63% used; 337739870 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41094131712 available bytes; 97.71% used; 110432649 free inodes.

server2 `/home`: 41094131712 available bytes; 97.71% used; 110432649 free inodes.

server2 `/tmp`: 41094131712 available bytes; 97.71% used; 110432649 free inodes.

server2 `/var/tmp`: 41094131712 available bytes; 97.71% used; 110432649 free inodes.

server2 `/mnt/raid5`: 537192882176 available bytes; 96.29% used; 445207513 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292732928000 available bytes; 83.66% used; 114202087 free inodes.

server3 `/home`: 292732928000 available bytes; 83.66% used; 114202087 free inodes.

server3 `/data`: 82445185024 available bytes; 98.86% used; 225847646 free inodes.

server3 `/tmp`: 292732928000 available bytes; 83.66% used; 114202087 free inodes.

server3 `/var/tmp`: 292732928000 available bytes; 83.66% used; 114202087 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106420641792 available bytes; 94.06% used; 114355155 free inodes.

server4 `/home`: 106420641792 available bytes; 94.06% used; 114355155 free inodes.

server4 `/data`: 300151672832 available bytes; 95.85% used; 225441378 free inodes.

server4 `/tmp`: 106420641792 available bytes; 94.06% used; 114355155 free inodes.

server4 `/var/tmp`: 106420641792 available bytes; 94.06% used; 114355155 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
