# V2R cluster inventory

2026-09-24T00:26:18.493391+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325552148480 available bytes; 81.84% used; 112500638 free inodes.

server1 `/home`: 325552148480 available bytes; 81.84% used; 112500638 free inodes.

server1 `/tmp`: 325552148480 available bytes; 81.84% used; 112500638 free inodes.

server1 `/var/tmp`: 325552148480 available bytes; 81.84% used; 112500638 free inodes.

server1 `/mnt/raid5`: 1159651057664 available bytes; 94.68% used; 337735183 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40997797888 available bytes; 97.71% used; 110432356 free inodes.

server2 `/home`: 40997797888 available bytes; 97.71% used; 110432356 free inodes.

server2 `/tmp`: 40997797888 available bytes; 97.71% used; 110432356 free inodes.

server2 `/var/tmp`: 40997797888 available bytes; 97.71% used; 110432356 free inodes.

server2 `/mnt/raid5`: 532904894464 available bytes; 96.32% used; 445203437 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292314132480 available bytes; 83.69% used; 114192308 free inodes.

server3 `/home`: 292314124288 available bytes; 83.69% used; 114192307 free inodes.

server3 `/data`: 82243526656 available bytes; 98.86% used; 225844300 free inodes.

server3 `/tmp`: 292314124288 available bytes; 83.69% used; 114192307 free inodes.

server3 `/var/tmp`: 292314124288 available bytes; 83.69% used; 114192307 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106086375424 available bytes; 94.08% used; 114350447 free inodes.

server4 `/home`: 106086375424 available bytes; 94.08% used; 114350447 free inodes.

server4 `/data`: 292915167232 available bytes; 95.95% used; 225414579 free inodes.

server4 `/tmp`: 106086375424 available bytes; 94.08% used; 114350447 free inodes.

server4 `/var/tmp`: 106086375424 available bytes; 94.08% used; 114350447 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
