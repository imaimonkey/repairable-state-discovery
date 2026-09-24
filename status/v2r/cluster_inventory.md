# V2R cluster inventory

2026-09-24T00:47:57.001834+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325535834112 available bytes; 81.84% used; 112500404 free inodes.

server1 `/home`: 325535834112 available bytes; 81.84% used; 112500404 free inodes.

server1 `/tmp`: 325535834112 available bytes; 81.84% used; 112500404 free inodes.

server1 `/var/tmp`: 325535834112 available bytes; 81.84% used; 112500404 free inodes.

server1 `/mnt/raid5`: 1069451239424 available bytes; 95.09% used; 337734952 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40980660224 available bytes; 97.71% used; 110432271 free inodes.

server2 `/home`: 40980660224 available bytes; 97.71% used; 110432271 free inodes.

server2 `/tmp`: 40980660224 available bytes; 97.71% used; 110432271 free inodes.

server2 `/var/tmp`: 40980660224 available bytes; 97.71% used; 110432271 free inodes.

server2 `/mnt/raid5`: 532236189696 available bytes; 96.32% used; 445202898 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292341972992 available bytes; 83.69% used; 114188827 free inodes.

server3 `/home`: 292341972992 available bytes; 83.69% used; 114188827 free inodes.

server3 `/data`: 82215780352 available bytes; 98.86% used; 225843543 free inodes.

server3 `/tmp`: 292341972992 available bytes; 83.69% used; 114188827 free inodes.

server3 `/var/tmp`: 292341972992 available bytes; 83.69% used; 114188827 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106049613824 available bytes; 94.08% used; 114349874 free inodes.

server4 `/home`: 106049613824 available bytes; 94.08% used; 114349874 free inodes.

server4 `/data`: 292918394880 available bytes; 95.95% used; 225414576 free inodes.

server4 `/tmp`: 106049613824 available bytes; 94.08% used; 114349874 free inodes.

server4 `/var/tmp`: 106049613824 available bytes; 94.08% used; 114349874 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
