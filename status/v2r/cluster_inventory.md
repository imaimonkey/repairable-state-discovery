# V2R cluster inventory

2026-09-24T18:53:56.889256+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323996934144 available bytes; 81.93% used; 112481453 free inodes.

server1 `/home`: 323996934144 available bytes; 81.93% used; 112481453 free inodes.

server1 `/tmp`: 323996934144 available bytes; 81.93% used; 112481453 free inodes.

server1 `/var/tmp`: 323996934144 available bytes; 81.93% used; 112481453 free inodes.

server1 `/mnt/raid5`: 416266600448 available bytes; 98.09% used; 337636606 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54469869568 available bytes; 96.96% used; 110411937 free inodes.

server2 `/home`: 54469869568 available bytes; 96.96% used; 110411937 free inodes.

server2 `/tmp`: 54469869568 available bytes; 96.96% used; 110411937 free inodes.

server2 `/var/tmp`: 54469869568 available bytes; 96.96% used; 110411937 free inodes.

server2 `/mnt/raid5`: 475361566720 available bytes; 96.72% used; 445160153 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84407762944 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84407762944 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152666402816 available bytes; 97.89% used; 225800118 free inodes.

server3 `/tmp`: 84407762944 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84407762944 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105661296640 available bytes; 94.10% used; 114348484 free inodes.

server4 `/home`: 105661296640 available bytes; 94.10% used; 114348484 free inodes.

server4 `/data`: 89945759744 available bytes; 98.76% used; 225267470 free inodes.

server4 `/tmp`: 105661296640 available bytes; 94.10% used; 114348484 free inodes.

server4 `/var/tmp`: 105661296640 available bytes; 94.10% used; 114348484 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
